from datetime import date, timedelta, datetime
from utils.helper import check_date_difference
from database.sqlhelper import Database
import pytest


def test_check_date_diff():
    date_from = date.today() - timedelta(days = 4)
    date_to = date.today()
    assert check_date_difference(date_from, date_to) == True

    date_from = date.today()
    date_to = date.today() - timedelta(days = 4)
    assert check_date_difference(date_from, date_to) == False

@pytest.mark.asyncio
async def test_avg_rates():
    db = Database()
    format = '%Y-%m-%d'
    date_from = datetime.strptime('2016-01-01', format)
    date_to = datetime.strptime('2016-01-01', format)
    source = 'CNGGZ'
    destination = 'ETLL'
    result = await db.get_average_rates(date_from, date_to, source, destination)
    assert result == []
