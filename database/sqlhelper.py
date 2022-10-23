import psycopg2

class Database:

    def __init__(self):
        self.database = psycopg2.connect(
                        host="localhost",
                        database="postgres",
                        user="postgres",
                        password="ratestask")


    async def get_average_rates(self):
        cursor = self.database.cursor()
        cursor.execute("SELECT * FROM ports")
        result = cursor.fetchall()
        return result