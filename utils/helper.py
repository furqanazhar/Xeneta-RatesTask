import json
from datetime import datetime


def convert_response_to_json(data):
    return json.loads(json.dumps(data, default=str, indent=2))

def check_date_format(date):
    try:
        acceptedFormat = "%Y-%m-%d"
        return bool(datetime.strftime(date, acceptedFormat)) 
    except ValueError:
        return False

def check_date_difference(date_from, date_to):
    if date_from > date_to:
        return False
    else:
        return True