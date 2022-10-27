"""This module consists of reusable methods"""

def check_date_difference(date_from, date_to):
    """This method verfies validity of date difference"""
    if date_from > date_to:
        return False
    return True
