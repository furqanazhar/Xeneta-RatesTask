"""This module runs the unit tests"""

from datetime import date, timedelta, datetime
from decimal import Decimal
import pytest
from fastapi.encoders import jsonable_encoder
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
async def test_invalid_destination():
    """This method runs the unit test for invalid destination location"""
    database = Database()
    date_format = '%Y-%m-%d'
    date_from = datetime.strptime('2016-01-01', date_format)
    date_to = datetime.strptime('2016-01-01', date_format)
    source = 'CNGGZ'
    destination = 'ETLL'
    result = await database.get_average_rates(date_from, date_to, source, destination)
    assert result == []


@pytest.mark.asyncio
async def test_valid_destination():
    """This method runs the unit test for valid destination location"""
    database = Database()
    date_format = '%Y-%m-%d'
    date_from = datetime.strptime('2016-01-01', date_format)
    date_to = datetime.strptime('2016-01-01', date_format)
    source = 'CNGGZ'
    destination = 'BEANR'
    result = await database.get_average_rates(date_from, date_to, source, destination)
    assert jsonable_encoder(result) == [{"day": "2016-01-01","average_price": 1128.33}]


@pytest.mark.asyncio
async def test_null_avg_rate():
    """This method runs the unit test for null avg rate"""
    database = Database()
    date_format = '%Y-%m-%d'
    date_from = datetime.strptime('2016-01-01', date_format)
    date_to = datetime.strptime('2016-01-01', date_format)
    source = 'CNGGZ'
    destination = 'NOFRK'
    result = await database.get_average_rates(date_from, date_to, source, destination)
    assert jsonable_encoder(result) == [{"day": "2016-01-01","average_price": None}]
