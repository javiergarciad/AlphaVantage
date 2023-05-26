from datetime import datetime

from sqlalchemy import DECIMAL
from app import db


class Base(db.Model):
    __abstract__ = True
    pass


class DailyBar(Base):
    """
    Represents a daily bar in the database.
    """

    __tablename__ = "daily_bar"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    symbol = db.Column(db.String(10), db.ForeignKey("symbol.symbol"), nullable=False)
    open = db.Column(DECIMAL(10, 6), nullable=False)
    high = db.Column(DECIMAL(10, 6), nullable=False)
    low = db.Column(DECIMAL(10, 6), nullable=False)
    close = db.Column(DECIMAL(10, 6), nullable=False)
    volume = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"{self.date} - {self.symbol}: O:{self.open:.2f}, H:{self.high:.2f}, \
            L:{self.low:.2f}, C:{self.close:.2f}, Vol:{self.volume:.0f}, \
            Last Updated: {self.updated:%d-%m-%Y %H:%M:%S}"

    def to_list(self):
        return [self.date, self.symbol, self.open, self.high, self.low, self.close, self.volume]


class Symbol(Base):
    """
    Represents a symbol in the database.
    """

    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"{self.symbol}"
