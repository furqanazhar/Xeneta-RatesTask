from datetime import date
import json
import traceback
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from utils.helper import convert_response_to_json, check_date_difference
from typing import List
from database.sqlhelper import Database

router = APIRouter()
db = Database()


@router.get('/rates', response_description='Get daily average rates between origin and destination ports/regions')
async def get_daily_average_rates(date_from: date, date_to: date, origin: str, destination: str):
    try:
        isValidDifference = check_date_difference(date_from, date_to)
        if not isValidDifference:
            response_payload = {'error': 'Date_From cannot be greater than Date_To'}
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=response_payload)
        output = await db.get_average_rates(date_from, date_to, origin, destination)

        response_payload = {
            'message': 'Successfully retrieved resource',
            'data': convert_response_to_json(output)
        }
        return JSONResponse(status_code=status.HTTP_200_OK, content=response_payload)
    except Exception as ex:
        response_payload = {
            'message': 'Failed to retrieve resource',
            'error': convert_response_to_json(ex)
        }
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=response_payload)
