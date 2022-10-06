import PySimpleGUI as sg

#Gerando todo o layout utilizando a biblioteca PySimpleGUI
def criar_app():
    sg.theme('DarkBlue4')
    linha = [
        [sg.Checkbox(''),sg.Input('')]
    ]
    
    Layout = [  
        [sg.Frame('Tarefas',linha, key='container')],
        [sg.Button('Nova Tarefa'),sg.Button('Resetar')]
        ]

    return sg.Window('To do List', Layout, finalize=True)

#Gerar a janela da aplicação
janela = criar_app()
#Gerar as regras
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break

    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''),sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = criar_app()

