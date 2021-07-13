import pandas as pd
import sqlite3



banco = sqlite3.connect(r'D:\felip\Documents\Eng\banco py\Retrabalho.db')

estoque = pd.read_sql_query("SELECT * FROM estoque",banco)
entrada = pd.read_sql_query("SELECT * FROM entrada",banco)
saida = pd.read_sql_query("SELECT * FROM saida",banco)

banco.commit()
