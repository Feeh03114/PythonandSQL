import sqlite3
banco = sqlite3.connect('Felipe.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE estoque (Name text, lote text, OP text, quantia float)")
cursor.execute("CREATE TABLE saida (Name text, lote text, OP text, quantia float,data date)")
cursor.execute("CREATE TABLE entrada (Name text, lote text, OP text, quantia float,data date)")

banco.commit()