from PySimpleGUI import PySimpleGUI as sg

#Layout
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario', size=(10,1))],
    [sg.Text('Senha  '), sg.Input(key='senha', password_char='*', size=(10,1))],
    [sg.Checkbox('Salvar o Loging?')],
    [sg.Button('Entrar')]
]
#Janela
janela = sg.Window('Tela de login', layout)

#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Lucas' and valores['senha'] == '123456':
            print('Bem vindo Lucas')
        else:
            print('Acesso Negado')