import pandas as pd
import numpy as np
import psycopg2
from psycopg2.extras import execute_values


df = pd.read_csv('./data/cbo2002-ocupacao.csv', 
                 sep=';', 
                 encoding='iso-8859-1') 

conn = psycopg2.connect(
    dbname='bd_postgres',
    user='postgres',
    password='admin',
    host='localhost',
    port='5432'
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS cbo (
    codigo VARCHAR(20) PRIMARY KEY,
    titulo TEXT
)
""")
conn.commit()

records = [tuple(int(x) if isinstance(x, np.int64) else x for x in record) 
           for record in df.to_records(index=False)]

execute_values(cur,
    "INSERT INTO cbo (codigo, titulo) VALUES %s ON CONFLICT (codigo) DO NOTHING",
    records
)
conn.commit()
cur.close()
conn.close()
print("Registros adicionados ao Postgres com sucesso!")
