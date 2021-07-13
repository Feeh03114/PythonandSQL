import pandas as pd
import sqlite3
list = ['Produto','Descricao']
x = pd.read_excel(r'D:\felip\Área de Trabalho\fabio\dados-default.xlsx', 'dados')

banco = sqlite3.connect('Felipe.db')

cursor = banco.cursor()
i=0
row = len(x.index)

print(row)

for i in range(int(row)):
   finalcodigo =(str(x['Produto'] [i])).replace('1210040','')
   cursor.execute("INSERT INTO dados VALUES('"+ finalcodigo +"','"+ str(x['Produto'] [i]) +"','"+ str(x['Descricao'] [i]) +"')")  # inserir dados default
banco.commit()
