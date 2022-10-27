"""This module runs the unit tests"""

from datetime import date, timedelta, datetime
import pytest
from utils.helper import check_date_difference
from database.sqlhelper import Database



def test_check_date_diff():
    """This method runs the unit test for check_date_difference"""
    date_from = date.today() - timedelta(days = 4)
    date_to = date.today()
    assert check_date_difference(date_from, date_to) is True

    date_from = date.today()
    date_to = date.today() - timedelta(days = 4)
    assert check_date_difference(date_from, date_to) is False


@pytest.mark.asyncio
async def test_avg_rates():
    """This method runs the unit test for get_average_rates"""
    database = Database()
    date_format = '%Y-%m-%d'
    date_from = datetime.strptime('2016-01-01', date_format)
    date_to = datetime.strptime('2016-01-01', date_format)
    source = 'CNGGZ'
    destination = 'ETLL'
    result = await database.get_average_rates(date_from, date_to, source, destination)
    assert result == []
