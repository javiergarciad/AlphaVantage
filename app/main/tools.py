import datetime
import os
from time import sleep

import sqlalchemy
from app import db
from config import Config
from app.models import Symbol, DailyBar

import yfinance as yf


def db_info():
    """
    Returns the database information
    """
    location = Config.DB_LOCATION
    symbols = len(Symbol.query.all())
    records = len(DailyBar.query.all())
    stmt = db.select(DailyBar.updated).order_by(sqlalchemy.desc(DailyBar.updated))
    last_update = db.session.execute(stmt).scalar()

    return {
        "location": location,
        "symbols": symbols,
        "records": records,
        "last_update": last_update,
    }


def tickets_in_db():
    """
    Returns a list of all symbols in the database
    """
    stmt = sqlalchemy.select(Symbol.symbol)
    qry = db.session.execute(stmt).all()
    if qry is None:
        return []
    else:
        return [symbol.symbol for symbol in qry]


def get_daily_bars_in_db(ticket):
    """
    get the daily bars for a given symbol in the database
    ordered descend.
    """
    stmt = (
        sqlalchemy.select(DailyBar)
        .where(DailyBar.symbol == ticket)
        .order_by(sqlalchemy.desc(DailyBar.date))
    )
    qry = db.session.execute(stmt).scalars()
    if qry is None:
        return []
    else:
        return [bar for bar in qry]


def period_to_start_date(period):
    """
    Convert a period to a date in the past, starting today
    """
    current = datetime.date.today()

    if period == "1d":
        return current - datetime.timedelta(days=1)
    elif period == "5d":
        return current - datetime.timedelta(days=5)
    elif period == "1mo":
        return current - datetime.timedelta(days=30)
    elif period == "3mo":
        return current - datetime.timedelta(days=30)
    elif period == "1y":
        return current.replace(year=current.year - 1)
    elif period == "2y":
        return current.replace(year=current.year - 2)
    elif period == "5y":
        return current.replace(year=current.year - 5)
    elif period == "10y":
        return current.replace(year=current.year - 10)
    elif period == "ytd":
        return current.replace(day=1, month=1)
    else:
        raise ValueError(f"Invalid period: {period}")


def update_database(period):
    """
    Updates the database with daily bars for all symbols

    """
    # get a list of all tickets in the database
    tks = tickets_in_db()
    start_date = period_to_start_date(period)
    end_date = datetime.date.today()

    ans = []
    for i, tk in enumerate(tks):
        print(f"Updating {i+1}/{len(tks)}")
        # deleting all bars for symbol
        delete_daily_bars(tk)
        # update
        tk_ans = get_daily_bars(tk, start_date, end_date)
        ans.append({"ticket": tk, "success": tk_ans})
        # pause to avoid rate limiting
        sleep(2)

    return ans


def get_daily_bars(ticket, start_date, end_date):
    """
    Returns the daily bars for a given symbol
    """
    tk = yf.Ticker(ticket)

    # get historical market data
    hist = tk.history(start=start_date, end=end_date)


    # chack if dataframe is empty
    if hist.empty:
        return False


    # drop some columns that we don store
    hist.drop(["Dividends", "Stock Splits"], inplace=True, axis=1)
    # add some columsn the model have
    hist["date"] = hist.index
    hist["symbol"] = ticket
    hist["created"] = datetime.datetime.now()
    hist["updated"] = datetime.datetime.now()
    # lower case the column names
    hist.columns = [c.lower() for c in hist.columns]

    # bulk insert the dataframe to the database
    bars = hist.to_dict(orient="records")
    db.session.execute(sqlalchemy.insert(DailyBar), bars)
    db.session.commit()
    return True


def delete_daily_bars(ticket):
    """
    Delete all dailybars for a ticket in the database
    """
    stmt = sqlalchemy.delete(DailyBar).where(DailyBar.symbol == ticket)
    db.session.execute(stmt)
    db.session.commit()
    return True
