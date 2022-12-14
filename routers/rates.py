"""This module contains endpoints"""

from datetime import date
from urllib import response
from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from utils.helper import check_date_difference
from database.sqlhelper import Database

router = APIRouter()
db = Database()


@router.get('/rates', response_description='Get daily average rates')
async def get_daily_average_rates(date_from: date, date_to: date, origin: str, destination: str):
    """This HTTP GET request calculates daily average rates"""
    try:
        is_valid_difference = check_date_difference(date_from, date_to)
        if not is_valid_difference:
            response_payload = 'Date_From cannot be greater than Date_To'
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=response_payload)
        output = await db.get_average_rates(date_from, date_to, origin, destination)
        response_payload = jsonable_encoder(output)
        return JSONResponse(status_code=status.HTTP_200_OK, content=response_payload)
    except Exception as ex:
        response_payload = jsonable_encoder(ex)
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=response_payload)
