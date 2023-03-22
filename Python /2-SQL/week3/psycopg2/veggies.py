import psycopg2

conn = psycopg2.connect(
    """
    dbname=week3 user=postgress host=localhost port=5432
    """
)
conn.set_session(autocommit=True)


#open a cursor to perform database operations 

cur = conn.cursor()

cur.execute(
    """
    DROP TABLE IF EXISTS veggies
    
    """

)
cur.execute(
    """
    CREATE TABLE veggies(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    color TEXT NOT NULL
    )
    """
)