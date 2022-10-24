import psycopg2

class Database:

    def __init__(self):
        self.database = psycopg2.connect(
                        host="localhost",
                        database="postgres",
                        user="postgres",
                        password="ratestask")


    async def get_average_rates(self, date_from, date_to, origin, destination):
        cursor = self.database.cursor()
        query = """
            SELECT p.day, ROUND(AVG(p.price),2) AS average_price
            FROM prices p
            WHERE p.orig_code = %s
            AND p.dest_code = %s
            AND p.day >= %s
            AND p.day <= %s
            GROUP BY p.day
        """
        cursor.execute(query, (origin, destination, date_from, date_to))
        result = cursor.fetchall()
        return result
        