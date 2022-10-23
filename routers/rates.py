import json
import traceback
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from models.rates import Rates
from utils.helper import convert_response_to_json
from typing import List
from database.sqlhelper import Database

router = APIRouter()
db = Database()

@router.get('/rates', response_description='Get daily average rates between origin and destination ports/regions')
async def get_daily_average_rates(rates: Rates):
    try:
        payload = {
            'message': 'Successfully retrieved resource',
            'data': convert_response_to_json(rates)
        }
        return JSONResponse(status_code=status.HTTP_200_OK, content=payload)
    except Exception as ex:
        payload = {
            'message': 'Failed to retrieve resource',
            'error': convert_response_to_json(ex)
        }
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=payload)

