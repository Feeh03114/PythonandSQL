import sqlite3
import os.path
from datetime import datetime

print("If you don't want to put the address, the database file will go to the folder where this script is being conducted")
endereco = input('Location where you want to store the database: ')

print("\nPlease enter the name of the database because without the name it will not be possible to create it")
namedate = input('Name of database: ')


''' Inicio da verificacao de se o arquivo existe e que local ele esta'''
if (endereco != "" and namedate != ""):
    exist = os.path.isfile(endereco + '\\' + namedate + '.db')
    if(exist != False):
        banco = sqlite3.connect(endereco + '\\' + namedate + '.db')
    else:
        exit()
elif (namedate != ""):
    exist = os.path.isfile(namedate + '.db')
    if(exist != False):
        banco = sqlite3.connect(namedate + '.db')
    else:
        exit() 
else:
    exit()
''' Fim da verificacao'''


cursor = banco.cursor()

saida = ''
while (saida.upper() != 'N'):
    print("\n\n---------------------------------------------------")
    print("\n\nWelcome to the stock entry and exit program")
    finalcodigo = input("Final do código: ")
    codigo = cursor.execute("SELECT Codigo FROM dados WHERE Codigorodape = '" + finalcodigo + "'").fetchone()# Pegar código completo
    nome = cursor.execute("SELECT Name FROM dados WHERE Codigorodape = '" + finalcodigo + "'").fetchone()  # Pegar nome do produto
    if(nome[0] == ""):
        nome = input("Produto: ")
        codigo = cursor.execute("SELECT Codigo FROM dados WHERE Name = '" + nome[0] + "'").fetchone()# Pegar código completo  
    lt = input("Lote: ")
    op = input("OP: ")
    quant = input("Quantia: ")
    qt = quant.replace(",", ".")
    dt = datetime.strptime(input("Data: "), '%d/%m/%Y').strftime("%Y/%m/%d")

    acao = input("In?(Y or N) ")

    if (acao.upper() == "Y"):

        RNC = input("RNC: ")  # dado a mais para entrada e estoque (Numero da não conformidade)
        MT = input("Motivo: ")  # dado a mais para entrada e estoque (Qual foi a não conformidade)
        obs = input("Observação: ")  # dado a mais para entrada e estoque (Algo a mais)

        cursor.execute("INSERT INTO entrada VALUES('"+ codigo[0] +"','"+ nome[0] +"','" + lt + "','" + op + "','" + qt + "','" + RNC + "','" + MT + "','" + obs + "','" + str(dt) + "')")  # Inserir no banco entrada
        cursor.execute("INSERT INTO estoque VALUES('"+ codigo[0] +"','"+ nome[0] +"','" + lt + "','" + op + "','" + qt + "','" + RNC + "','" + MT + "','" + obs + "')")  # Inserir no banco estoque

        banco.commit()  # Fechar banco
    else:

        cursor.execute("INSERT INTO saida VALUES('"+ codigo[0] +"','" + nome[0] + "','" + lt + "','" + op + "'," + qt + ",'" + str(dt) + "')")  # Atualizar banco de saida

        valor = cursor.execute("SELECT quantia FROM estoque WHERE OP = '" + op + "'").fetchone()  # Pegar a quantia disponivel
        print("Amount available from stock: ", float(valor[0]))  # printar a quantia disponivel

        Rvalor = float(valor[0]) - float(qt)  # Converte os valor de String para Float e faz a subtração do que foi tirado
        qt = str(Rvalor).replace(",", ".")  # Converte o valor da subtração em String e tira a ',' para '.'
        cursor.execute("UPDATE estoque SET quantia = '" + qt + "' WHERE OP = '" + op + "'")  # Atualizar quantia com base na OP

        valor = cursor.execute("SELECT quantia FROM estoque WHERE OP = '" + op + "'").fetchone()  # Pegar a quantia atualizada

        print("Updated amount for ", valor[0])  # printar a quantia atualizada

        banco.commit()  # Fechar banco

    saida = input("Do you want to stay in the program?(Y or N) ")
else:
    print("\n\nProgram terminated successfully! ")
    print("\nThank you for using our program! ")
