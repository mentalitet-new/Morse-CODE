import psycopg2

password = input()
conn = psycopg2.connect(f'dbname=job_srv user=postgres password={password} host=localhost port=5432')
cur = conn.cursor()

cur.execute('SELECT * FROM information')

rec = cur.fetchall()
print(rec)