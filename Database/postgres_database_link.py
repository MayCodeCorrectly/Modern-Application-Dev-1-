import psycopg2
import os
import sys

conn = None

try:
    conn = psycopg2.connect(
        database = 'University',
        user = 'postgres',
        password = "S@NDEEP@#$2005",
        host = '127.0.0.1',
        port = '5432'
    )
    print("Database connected successfully")

    cur = conn.cursor()
    cur.execute("select * from instructor")
    result = cur.fetchall()
    # print(result)
    for instance in result:
        print(instance)
    
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()