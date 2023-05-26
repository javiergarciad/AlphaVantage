

from app.models import DailyBar
from datetime import datetime, timedelta
import __main__


def populate_fake_bars(ticket, n):
    all_bars = []
    end_date = datetime.today()
    start_date = end_date - timedelta(days=n)
    for i in range(n):
        bar = DailyBar(
            ticket=ticket,
            date=start_date + timedelta(days=i),
            open=100,
            high=100,
            low=100,
            close=100,
            volume=100,
        )
        all_bars.append(bar)

    return all_bars


if  __main__ == '__main__':

    data = populate_fake_bars(ticket='AAPL', n=10)
    print(data)
