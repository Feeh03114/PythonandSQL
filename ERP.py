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
        [sg.Checkbox("remember Server?")],
        [sg.Button('OK'),sg.Button('Cancel')]
    ]
    return sg.Window('Configuração Servidor',layout=configserver,finalize=True)

def window_Home():
    home = [
        [sg.Text('Welcome to the stock entry and exit program')],
        [sg.Text('End of code:'),sg.Input(code,key='finalcode')],
        [sg.Text('Product:'),sg.Input(produt,key='productname')],
        [sg.Text('Lote:'),sg.Input(key='lt1')],
        [sg.Text('OP:'),sg.Input(key='op1')],
        [sg.Text('Amount:'),sg.Input(key='qt1')],
        [sg.Text('Date:'),sg.Input(key='dt1')],
        [sg.Radio("In",'type',key='Y'),sg.Radio("Out",'type',key='N')],
        [sg.Button('Continue'),sg.Button('Cancel')]
    ]
    return sg.Window('Tela Inicial',layout=home,finalize=True)

def window_In_data():
    in_data = [
        [sg.Text('RNC:'),sg.Input(key='rnc1')],
        [sg.Text('Reason:'),sg.Input(key='mt1')],
        [sg.Text('Comments:'),sg.Input(key='obs1')],
        [sg.Button('Insert'),sg.Button('Cancel')]
    ]
    return sg.Window('Entrada de dados',layout=in_data,finalize=True)

'''def exit_confirmation_window():
    exit_confirmation = [
        [sg.Text('Endereco:'),sg.Input(default_location,key='local')],
        [sg.Text('Namedate:'),sg.Input(default_namedate,key='namedate')],
        [sg.Checkbox("remember Server?")],
        [sg.Button('OK'),sg.Button('Cancel')]
    ]
    return sg.Window('Entrada de dados',layout=exit_confirmation,finalize=True)'''






'''Checks functions'''
def check_server(endereco,namedate):
    ''' Inicio da verificacao de se o arquivo existe e que local ele esta'''
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
        check_server(default_location,default_namedate)


def check_user(user,passw):
    userdada = bank.execute("SELECT usernames FROM users WHERE usernames = '" + user + "'").fetchone()  # Pegar a user
    passworddata = bank.execute("SELECT password FROM users WHERE usernames = '" + user + "'").fetchone()  # Pegar a password

    if user== userdada[0] and passw == passworddata[0]:
        return True
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




Janela1, Janela2, Janela3, Janela4, Janela5 = window_configserver(),None, None, None, None

while True:
    window,event,val = sg.read_all_windows()

    if window == Janela1:
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'OK':
            bank = check_server(val['local'],val['namedate'])
            Janela2 = window_login()
            Janela1.hide()

    elif window == Janela2:
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Login':
            active = check_user(val['username'],val['password'])
            if active:
                Janela3 = window_Home()
                Janela2.hide()

    elif window == Janela3:
        dates = add_code(val['finalcode'])
        code = dates[1].replace('1210040','')
        produt = dates[0]
        print(produt,code)
        Janela3['productname'].Update(produt)
        Janela3['finalcode'].Update(code)
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
            print(val('finalcode'))
        if event == 'Continue':
            if val['Y']:
                Janela4 = window_In_data()
                Janela2.hide()
    elif window == Janela4:
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Cancel':
            Janela4.close()
            Janela3.un_hider()
        elif event == 'Insert':
            Insert_database(dates[1],dates[0],val['lt1'],val['op1'],val['qt1'],val['rnc1'],val['mt1'],val['obs1'],val['dt1'])


