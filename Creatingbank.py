import sqlite3
from sqlite3.dbapi2 import Cursor


banco = sqlite3.connect('Dados.db')


cursor = banco.cursor()
exiting= 's'
while exiting != 'N' or exiting != 'n':
    print('Create bank')
    nametable = input('Name of table: ')
    namecolumn = input('Name of colunm: ')
    typecolunm = input('Type of colunm: ')
    cursor.execute("CREATE TABLE '"+nametable+"' ('"+namecolumn+" "+typecolunm+"')")
    cont = input('Do you want to place more columns?(Y or N) ')
    if cont == "Y" or cont == "y" :
        while but !='Y' or but != "y":
             namecolumn = input('Name of colunm: ')
            typecolunm = input('Type of colunm: ')
            cursor.execute("ALTER TABLE '"+nametable+"' ADD '"+namecolumn+" "+typecolunm+"'"
            but = input("Do you want to continue adding columns?(Y or N) ")
    banco.commit() # Fechar banco
    exiting = input("Do you want to continue in the program?(Y or N) ")
else:
    print("Program terminated successfully! ")
    print("Thank you for using our program! ")