import pyodbc
import sqlalchemy
import pandas as pd


engine = sqlalchemy.create_engine("mssql+pyodbc://desarrollo:123@localhost/Hurtos?driver=ODBC+Driver+17+for+SQL+Server")

df = pd.read_sql_query('SELECT * FROM Armas',engine)
df.to_sql("Armas2", engine, if_exists='replace')
list_Armas= engine.execute('SELECT * FROM Armas2').fetchall()

print(list_Armas)