import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root: @localhost:3306/Cadastro')
df = pd.read_sql_table('estudos',engine)


