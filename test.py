import sqlite3
banco = sqlite3.connect('Felipe.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE dados (Codigorodape text, Codigo text, Name text)")
cursor.execute("CREATE TABLE estoque (Codigo text, Name text, lote text, OP text, quantia float)")
cursor.execute("CREATE TABLE saida (Codigo text, Name text, lote text, OP text, quantia float,data date)")
cursor.execute("CREATE TABLE entrada (Codigo text, Name text, lote text, OP text, quantia float,data date)")

banco.commit()
