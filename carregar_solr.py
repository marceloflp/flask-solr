import psycopg2
import pysolr

solr = pysolr.Solr('http://localhost:8983/solr/cbo', always_commit=True)

conn = psycopg2.connect(
    dbname='bd_postgres',
    user='postgres',
    password='admin',
    host='localhost',
    port='5432'
)
cur = conn.cursor()
cur.execute("SELECT codigo, titulo FROM cbo")
rows = cur.fetchall()

solr_docs = [{"id": r[0], "codigo": r[0], "titulo": r[1]} for r in rows]

solr.add(solr_docs)
print(f"{len(solr_docs)} registros adicionados ao Solr.")

cur.close()
conn.close()
