import PySimpleGUI as sg
import sqlite3
import os.path
import datetime

sg.theme('Dark Blue 3')

default_location = 'D:\\felip\\Documents\\Eng\\banco py\\bank'
default_namedate = 'Dada'

produt = ''
code = ''

def window_login():
    login_user = [
        [sg.Text('User:'),sg.Input(key='username')],
        [sg.Text('Password:'),sg.Input(key='password',password_char='*')],
        [sg.Checkbox("remember user?")],
        [sg.Button('Login'),sg.Button('Cancel')]
    ]
    return sg.Window('Login User',layout=login_user,finalize=True)

def window_configserver():
    configserver = [
        [sg.Text('Endereco:'),sg.Input(default_location,key='local')],
        [sg.Text('Namedate:'),sg.Input(default_namedate,key='namedate')],
        [sg.Checkbox("remember Server?",key='newserver')],
        [sg.Button('OK'),sg.Button('Cancel')]
    ]
    return sg.Window('Server Configuration',layout=configserver,finalize=True)

def window_Box():
    box = [
        [sg.Text('Welcome to the cashier')],
        [sg.Text('End of code:'),sg.Input(code,key='finalcode'),sg.Text('Product:'),sg.Input(produt,key='productname'),sg.Text('Amount:'),sg.Input(key='qt1'),sg.Button('Insert')],
        [sg.text('Total:'),sg.Text(key='valuetotal'),sg.Button('Pay'),sg.Button('Delete item'),sg.Button('Return',visible='False')]
        [sg.Output(key='out_itens')],
    ]
    return sg.Window('Box Screen',layout=box,finalize=True)

def window_In_data():
    in_data = [
        [sg.Text('End of code:'),sg.Input(code,key='finalcode'),sg.Text('Product:'),sg.Input(produt,key='productname'),sg.Text('Amount:'),sg.Input(key='qt1')],
        [sg.Text('Lote:'),sg.Input(key='lt1'),sg.Text('Sublote:'),sg.Input(key='sub'),sg.Text('Nota Fiscal:'),sg.Input(key='NFe'),sg.Text('Data:'),sg.Input(key='dtin')],
        [sg.Button('Insert'),sg.Button('Cancel')]
    ]
    return sg.Window('Input Screen',layout=in_data,finalize=True)

def window_Home():
    home = [
        []
    ]



'''def exit_confirmation_window():
    exit_confirmation = [
        [sg.Text('Endereco:'),sg.Input(default_location,key='local')],
        [sg.Text('Namedate:'),sg.Input(default_namedate,key='namedate')],
        [sg.Checkbox("remember Server?")],
        [sg.Button('OK'),sg.Button('Cancel')]
    ]
    return sg.Window('Entrada de dados',layout=exit_confirmation,finalize=True)'''





'''Checks functions'''
def check_server(endereco,namedate,default_location,default_namedate,to_remember):
    ''' Inicio da verificacao de se o arquivo existe e que local ele esta'''
    endereco2 = 'C:\box server address'
    namedate2 = 'server_address'
    exist2 = os.path.isfile(endereco2 + '\\' + namedate2 + '.txt')
    if exist2:
        server = open(endereco2 + '\\' + namedate2 + '.txt','r')
        endereco = exist = os.path.isfile(endereco+'.db')
        exist = os.path.isfile(endereco + '.db')
        if exist != False:
                banco = sqlite3.connect(endereco +'.db')
                return banco.cursor()
    elif endereco != default_location and namedate == default_namedate and to_remember == True:
        exist = os.path.isfile(endereco)
        if exist:
            arquivo = open(endereco2 + '\\' + namedate2 + '.txt', "w")
            arquivo.write(endereco + '\\' + namedate)
        else:
            os.mkdir(endereco2)
            exist = os.path.isfile(endereco)
            if exist:
                arquivo = open(endereco2 + '\\' + namedate2 + '.txt', "w")
                arquivo.write(endereco + '\\' + namedate)
                exist = os.path.isfile(endereco + '\\' + namedate + '.db')
                if(exist != False):
                    banco = sqlite3.connect(endereco + '\\' + namedate + '.db')
                    return banco.cursor()
                else:
                    exit()
                
    else:
        if (endereco != "" and namedate != ""):
            exist = os.path.isfile(endereco + '\\' + namedate + '.db')
            if(exist != False):
                banco = sqlite3.connect(endereco + '\\' + namedate + '.db')
                return banco.cursor()
            else:
                exit()
        elif (namedate != ""):
            exist = os.path.isfile(namedate + '.db')
            if(exist != False):
                banco = sqlite3.connect(namedate + '.db')
                return banco.cursor()
            else:
                exit() 
        else:
            banco = sqlite3.connect(endereco + '\\' + namedate + '.db')
            creatingbank(banco)
            return banco.cursor()

def creatingbank(banco):
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE users (usernames text, password text, typeaccess text)")
    cursor.execute("CREATE TABLE dados (Codigorodape text, Codigo text, Name text,preço float,quantia number)")
    cursor.execute("CREATE TABLE estoque (Codigo text, Name text, lote text, OP text, quantia float)")
    cursor.execute("CREATE TABLE saida (Codigo text, Name text, lote text, OP text, quantia float,typepay text,user text,data date)")
    cursor.execute("CREATE TABLE entrada (Codigo text, Name text, lote text, sublote text, quantia float,notafiscal text,user text,datain date,datasystem date)")



def check_user(user,passw):
    userdada = bank.execute("SELECT usernames FROM users WHERE usernames = '" + user + "'").fetchone()  # Pegar a user
    passworddata = bank.execute("SELECT password FROM users WHERE usernames = '" + user + "'").fetchone()  # Pegar a password
    typeuser = bank.execute("SELECT typeaccess FROM users WHERE usernames = '" + user + "'").fetchone()

    if user== userdada[0] and passw == passworddata[0]:
        return True,typeuser[0]
    else: 
        sg.popup('Senha ou Usuário incorretos!!!\nPor favor, corrigir ou conversar com o TI')


''' Fim da verificacao'''

def add_code(finalcodigo):
    if finalcodigo != '':
        codigo = bank.execute("SELECT Codigo FROM dados WHERE Codigorodape = '" + finalcodigo + "'").fetchone()# Pegar código completo
        nome = bank.execute("SELECT Name FROM dados WHERE Codigorodape = '" + finalcodigo + "'").fetchone()  # Pegar nome do produto
        if(nome[0] == ""):
            nome = input("Produto: ")
            codigo = bank.execute("SELECT Codigo FROM dados WHERE Name = '" + nome[0] + "'").fetchone()# Pegar código completo 
            return nome, codigo
        else:
            return nome[0], codigo[0]

def Insert_database(codigo,nome,lote,op,quant,RNC,MT,obs,dt):
    dt = datetime.strptime(dt, '%d/%m/%Y').strftime("%Y/%m/%d")
    qt = quant.replace(",", ".")
    cursor.execute("INSERT INTO entrada VALUES('"+ codigo +"','"+ nome +"','" + lote + "','" + op + "','" + qt + "','" + RNC + "','" + MT + "','" + obs + "','" + str(dt) + "')")  # Inserir no banco entrada
    cursor.execute("INSERT INTO estoque VALUES('"+ codigo +"','"+ nome +"','" + lote + "','" + op + "','" + qt + "','" + RNC + "','" + MT + "','" + obs + "')")  # Inserir no banco estoque

    banco.commit()  # Fechar banco






Janela1, Janela2, Janela3, Janela4, Janela5, Janela6 = window_configserver(),None, None, None, None, None

while True:
    window,event,val = sg.read_all_windows()

    if window == Janela1:
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'OK':
            bank = check_server(val['local'],val['namedate'],default_location,default_namedate,val['newserver'])
            Janela2 = window_login()
            Janela1.hide()

    elif window == Janela2:
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Login':
            active = check_user(val['username'],val['password'])
            if active[0] and active[1] == '1':
                Janela3 = window_Box()
                Janela2.hide()
            elif active[0] and active[1] == '2':
                Janela4 = window_In_data()
                Janela2.hide()
            elif active[0] and active[1] == '3':
                Janela5 = window_Home()
                Janela2.hide()

    elif window == Janela3:
        dates = add_code(val['finalcode'])
        code = dates[1].replace('1210040','')
        produt = dates[0]
        Janela3['productname'].Update(produt)
        Janela3['finalcode'].Update(code)
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Cancel':
            Janela4.close()
            Janela3.un_hider()
        elif event == 'Insert':
            Insert_output(dates[1],dates[0],val['lt1'],val['op1'],val['qt1'],val['rnc1'],val['mt1'],val['obs1'],val['dt1'])
        elif event == 'Pay':
            Insert_database_pay(dates[1],dates[0],val['lt1'],val['op1'],val['qt1'],val['rnc1'],val['mt1'],val['obs1'],val['dt1'])
        elif event == 'Delete item':
            delete_item()

    elif window == Janela4:
        dates = add_code(val['finalcode'])
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Cancel':
            Janela4.close()
            Janela3.un_hider()
        elif event == 'Insert':
            Insert_database(dates[1],dates[0],val['lt1'],val['op1'],val['qt1'],val['rnc1'],val['mt1'],val['obs1'],val['dt1'])

    elif windows == Janela5:
        if event == sg.WIN_CLOSED:
            break
        elif event == ''


