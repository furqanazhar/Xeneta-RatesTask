import psycopg2
import os

class Database:

    def __init__(self):
        self.database = psycopg2.connect(
                        host="localhost",
                        database="postgres",
                        user="postgres",
                        password="ratestask")


    async def get_average_rates(self, date_from, date_to, origin, destination):
        try:
            path = os.path.join('database','scripts','get_daily_rates.sql')
            with open(path, 'r') as file:
                with self.database.cursor() as cursor:
                    cursor.execute(file.read(), {'origin': origin, 'destination': destination, 'date_from': date_from, 'date_to': date_to})
                    result = cursor.fetchall()
                    average_prices = [dict(zip(['day', 'average_price'], price)) for price in result]
            return average_prices
        except Exception as ex:
            return ex
        