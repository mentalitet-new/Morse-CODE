import psycopg2
import json

with open("data.json", "r") as read:
    data = json.load(read)

conn = psycopg2.connect(f'dbname={data["dbname"]} user={data["user"]} '
                        f'password={data["password"]} '
                        f'host={data["host"]} '
                        f'port={data["port"]} ')
cur = conn.cursor()

cur.execute('SELECT * FROM information')

rec = cur.fetchall()
print(rec)