import sqlite3
from datetime import datetime
from sqlite3.dbapi2 import Cursor


    banco = sqlite3.connect('Dados.db')


    Cursor = banco.cursor()

'''cursor.execute("CREATE TABLE estoque (Name text, lote text, OP text, quantia float)")
cursor.execute("CREATE TABLE saida (Name text, lote text, OP text, quantia float,data date)")
cursor.execute("CREATE TABLE entrada (Name text, lote text, OP text, quantia float,data date)")'''

    saida = ''
    while saida != 'N' or saida != 'n':
            print("Bem-Vindo ao programa de Retrabalho")

            nome = input("Produto: ")
            lt = input("Lote: ")
            op = input("OP: ")
            quant = input("Quantia: ")
            qt = quant.replace(",",".")
            dt = datetime.strptime(input("Data: "), '%d/%m/%Y').strftime("%Y/%m/%d")



            acao = input("Entrada? ")

            if acao == "Sim" or acao == "sim" or acao == "yes" or acao == "Yes" or acao == "S" or acao == "s" or acao == "Y" or acao == "y" :

                RNC = input("RNC: ") #dado a mais para entrada e estoque (Numero da não conformidade)
                MT = input("Motivo: ") #dado a mais para entrada e estoque (Qual foi a não conformidade)
                obs = input("Observação: ")#dado a mais para entrada e estoque (Algo a mais)

                cursor.execute("INSERT INTO entrada VALUES('"+nome+"','"+lt+"','"+op+"','"+qt+"','"+RNC+"','"+MT+"','"+obs+"','"+str(dt)+"')")# Inserir no banco entrada
                cursor.execute("INSERT INTO estoque VALUES('"+nome+"','"+lt+"','"+op+"','"+qt+"','"+RNC+"','"+MT+"','"+obs+"')")# Inserir no banco estoque

                banco.commit()# Fechar banco
            else:

                cursor.execute("INSERT INTO saida VALUES('"+nome+"','"+lt+"','"+op+"',"+qt+",'"+str(dt)+"')")# Atualizar banco de saida

                valor = cursor.execute("SELECT quantia FROM estoque WHERE OP = '"+op+"'").fetchone() #Pegar a quantia disponivel
                print("Valor disponivel no estoque: ",float(valor[0]))  # printar a quantia disponivel


                Rvalor = float(valor[0]) - float(qt) # Converte os valor de String para Float e faz a subtração do que foi tirado
                qt = str(Rvalor).replace(",",".") # Converte o valor da subtração em String e tira a ',' para '.'
                cursor.execute("UPDATE estoque SET quantia = '"+qt+"' WHERE OP = '"+op+"'") # Atualizar quantia com base na OP

                valor2 = cursor.execute("SELECT quantia FROM estoque WHERE OP = '"+op+"'").fetchone() #Pegar a quantia atualizada
                print("Quatia atualizada para ",valor2[0]) # printar a quantia atualizada

                banco.commit() # Fechar banco

            saida = input("Deseja continuar no programa?(Y or N) ")
    else:
        print("Programa encerrado com sucesso! ")
        print("Obrigado por usar nosso programa! ")