import sqlite3
from sqlite3.dbapi2 import Cursor
print("If you don't want to put the address, the database file will go to the folder where this script is being conducted")
endereco = input('Location where you want to store the database: ')
print("Please enter the name of the database because without the name it will not be possible to create it")
namedate = input('Name of database: ')
if (endereco != "" and namedate != ""):
    banco = sqlite3.connect(endereco+'\\'+namedate+'.db')
elif (namedate != ""):
    banco = sqlite3.connect(namedate + '.db')
else:
    exit()

cursor = banco.cursor()
exiting = 's'
while (exiting.upper()  != 'N'):
    but = 's'
    print('Create bank')
    nametable = input('Name of table: ')
    namecolumn = input('Name of colunm: ')
    typecolunm = input('Type of colunm: ')
    cursor.execute("CREATE TABLE '"+nametable+"' ('"+namecolumn+" "+typecolunm+"')")
    cont = input('Do you want to place more columns?(Y or N)')
    if (cont.upper() == "Y"):
        while (but.upper() != 'N'):
            namecolumn = input('Name of colunm: ')
            typecolunm = input('Type of colunm: ')
            cursor.execute("ALTER TABLE '"+nametable+"' ADD "+namecolumn+" "+typecolunm)
            but = input("\nDo you want to continue adding columns?(Y or N) ")
    exiting = input("\nDo you want to continue in the program?(Y or N) ")
else:
    banco.commit()  # Fechar banco
    print("\n\nProgram terminated successfully! ")
    print("Thank you for using our program! ")