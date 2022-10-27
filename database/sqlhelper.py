"""This module handles interaction with database"""
import os
import psycopg2


class Database:
    """This class represents a database"""
    def __init__(self):
        self.database = psycopg2.connect(
                        host="localhost",
                        database="postgres",
                        user="postgres",
                        password="ratestask")


    async def get_average_rates(self, date_from, date_to, origin, destination):
        """This method returns average daily rates between origin and destination regions"""
        try:
            path = os.path.join('database','scripts','get_daily_rates.sql')
            with open(path, 'r', encoding="utf-8") as file:
                with self.database.cursor() as cursor:
                    cursor.execute(file.read(), {'origin': origin, 'destination': destination,
                                                 'date_from': date_from, 'date_to': date_to})
                    result = cursor.fetchall()
                    average_prices = [dict(zip(['day', 'average_price'], price)) for price in result]
            return average_prices
        except Exception as ex:
            return ex
        