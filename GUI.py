import PySimpleGUI as sg


def janela_menu_principal():
    sg.theme('Reddit')
    layout = [
        [sg.Text('                  Menu Principal')],
        [sg.Text('Seja bem vindo ao menu de jogos!')],
        [sg.Text('Escolha a baixo qual jogo você quer iniciar!')],
        [sg.Button('Jogo da adivinhação')],
        [sg.Button('Jogo dos dados')],
        [sg.Button('Sair do programa')]
    ]
    return sg.Window('Menu Principal', layout, finalize=True)

def janela_erro():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Você digitou um valor inválido, por favor, digite um número inteiro dentre os especificados!')],
        [sg.Button('Okay')]
    ]
    return sg.Window('ERRO!', layout, finalize = True)

def janela_adivinhacao():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Boas vindas ao jogo da adivinhação!')],
        [sg.Text('Escolha uma das opções abaixo para continuar:')],
        [sg.Button('Jogar')],
        [sg.Button('Regras')],
        [sg.Button('Retornar ao menu principal')]
    ]
    return sg.Window('Jogo da Adivinhação', layout, finalize=True)


def janela_dificuldades():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Você escolheu jogar!')],
        [sg.Text('Escolha entre as dificuldades abaixo:')],
        [sg.Button('Fácil')],
        [sg.Button('Médio')],
        [sg.Button('Difícil')],
        [sg.Button('Retornar')],
    ]
    return sg.Window('Dificuldade do jogo da adivinhação', layout, finalize=True)


def janela_errou():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Que pena! Você errou')],
        [sg.Button('Recomeçar')]
    ]
    return sg.Window('Vitória', layout, finalize=True)


def janela_acertou():
    sg.theme('Reddit')
    layout = [
        [sg.Text('PARABÉNS! Você acertou')],
        [sg.Button('Concluído')]
    ]
    return sg.Window('Vitória', layout, finalize=True)


def gera_aleatorio(dificuldade):
    from random import randint
    if dificuldade == 1:
        x = randint(1,10)
        return x
    elif dificuldade == 2:
        x = randint (1,50)
        return x
    elif dificuldade == 3:
        x = randint(1, 100)
        return x
    else:
        return 'Erro'

def janela_facil():
    sg.theme('Reddit')
    from random import randint
    layout = [
        [sg.Text('Digite um número de 1 a 10:')],
        [sg.Text('Valor'), sg.Input(key='Valor')],
        [sg.Button('Enviar')]
    ]
    return sg.Window('Dificuldade Fácil', layout, finalize=True)

def janela_medio():
    sg.theme('Reddit')
    from random import randint
    layout = [
        [sg.Text('Digite um número de 1 a 50:')],
        [sg.Text('Valor'), sg.Input(key='Valor')],
        [sg.Button('Enviar')]
    ]
    return sg.Window('Dificuldade Médio', layout, finalize=True)

def janela_dificil():
    sg.theme('Reddit')
    from random import randint
    layout = [
        [sg.Text('Digite um número de 1 a 100:')],
        [sg.Text('Valor'), sg.Input(key='Valor')],
        [sg.Button('Enviar')]
    ]
    return sg.Window('Dificuldade Difícil', layout, finalize=True)


def janela_regras():
    sg.theme('Reddit')
    layout = [
        [sg.Text('As regras do jogo são:')],
        [sg.Text('1. Você terá 1 chance de acertar um valor definido pela dificuldade escolhida.')],
        [sg.Text('2. Caso você digite um número errado, o programa lhe avisará e fechará.')],
        [sg.Text('3. Ao final da tentativa, o programa exibirá uma mensagem dizendo se você ganhou ou perdeu.')],
        [sg.Button('Retornar')]
    ]
    return sg.Window('Regras do jogo da adivinhação', layout, finalize=True)


def janela_dados():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Olá, seja bem-vindo ao jogo "Dados"!')],
        [sg.Text('Escolha uma das opções abaixo para continuar:')],
        [sg.Button('Jogar os dois dados')],
        [sg.Button('Jogar somente um dado')],
        [sg.Button('Retornar ao menu principal')]
    ]
    return sg.Window('Jogo dos Dados', layout, finalize=True)


def janela_joga2dados():
    sg.theme('Reddit')
    from main import Dados
    dados = Dados()
    faces = dados.jogar(1)
    face1 = faces[0]
    face2 = faces[1]
    layout = [
        [sg.Text(f'A face 1 deu {face1} e a face 2 deu {face2}')],
        [sg.Button('Concluído')]
    ]
    return sg.Window('Jogou 2 dados', layout, finalize=True)


def janela_joga1dado():
    sg.theme('Reddit')
    from main import Dados
    dados = Dados()
    faces = dados.jogar(1)
    face1 = faces[0]
    layout = [
        [sg.Text(f'O resultado foi {face1}')],
        [sg.Button('Concluído')]
    ]
    return sg.Window('Jogou 1 dado', layout, finalize=True)


# Criar janelas
janela_p, janela_a, janela_d, janela_r, janela_dif, janela_j_dd, janela_j_d, janela_j_a, janela_dif_f, janela_dif_m, janela_dif_d, janela_ac, janela_er, janela_es, janela_error = janela_menu_principal(), None, None, None, None, None, None, None, None, None, None, None, None, None, None

# Criar um loop de leitura de eventos
while True:
    window, event, values = sg.read_all_windows()
    # Janela for fechada
    if window == janela_p and event == sg.WIN_CLOSED:
        break
    if window == janela_a and event == sg.WIN_CLOSED:
        janela_a.hide()
        janela_p.un_hide()
    if window == janela_d and event == sg.WIN_CLOSED:
        janela_d.hide()
        janela_p.un_hide()
    if window == janela_r and event == sg.WIN_CLOSED:
        janela_r.hide()
        janela_p.un_hide()
    if window == janela_dif and event == sg.WIN_CLOSED:
        janela_dif.hide()
        janela_p.un_hide()
    if window == janela_j_dd and event == sg.WIN_CLOSED:
        janela_j_dd.hide()
        janela_p.un_hide()
    if window == janela_j_d and event == sg.WIN_CLOSED:
        janela_j_d.hide()
        janela_p.un_hide()
    if window == janela_j_a and event == sg.WIN_CLOSED:
        janela_j_a.hide()
        janela_p.un_hide()
    if window == janela_dif_f and event == sg.WIN_CLOSED:
        janela_dif_f.hide()
        janela_p.un_hide()
    if window == janela_dif_m and event == sg.WIN_CLOSED:
        janela_dif_m.hide()
        janela_p.un_hide()
    if window == janela_dif_d and event == sg.WIN_CLOSED:
        janela_dif_d.hide()
        janela_p.un_hide()
    #Menu principal
    if window == janela_p and event == 'Jogo da adivinhação':
        janela_a = janela_adivinhacao()
        janela_p.hide()

    if window == janela_error and event == 'Okay':
        janela_error.hide()
        janela_dif.un_hide()

    if window == janela_p and event == 'Jogo dos dados':
        janela_d = janela_dados()
        janela_p.hide()

    if window == janela_p and event == 'Sair do programa':
        break
    # Janela do jogo Adivinhação
    if window == janela_a and event == 'Jogar':
        janela_dif = janela_dificuldades()
        janela_a.hide()

    if window == janela_dif and event == 'Fácil':
        janela_dif.hide()
        janela_dif_f = janela_facil()
    if window == janela_dif_f and event == 'Enviar':
        if type(values['Valor']) != int:
            janela_dif_f.hide()
            janela_error=janela_erro()
        elif values['Valor']<1 or values['Valor']>10:
            janela_dif_f.hide()
            janela_error = janela_erro()
        else:
            if values['Valor'] == gera_aleatorio(1):
                janela_dif_f.hide()
                janela_ac = janela_acertou()
            else:
                janela_dif_f.hide()
                janela_er = janela_errou()

    if window == janela_dif and event == 'Médio':
        janela_dif.hide()
        janela_dif_m = janela_medio()
    if window == janela_dif_m and event == 'Enviar':
        if type(values['Valor']) != int:
            janela_dif_m.hide()
            janela_error=janela_erro()
        elif values['Valor'] < 1 or values['Valor'] > 50:
            janela_dif_m.hide()
            janela_error = janela_erro()
        else:
            if values['Valor'] == gera_aleatorio(2):
                janela_dif_m.hide()
                janela_ac = janela_acertou()
            else:
                janela_dif_m.hide()
                janela_er = janela_errou()

    if window == janela_dif and event == 'Difícil':
        janela_dif.hide()
        janela_dif_d = janela_dificil()
    if window == janela_dif_d and event == 'Enviar':
        if type(values['Valor']) != int:
            janela_dif_d.hide()
            janela_error=janela_erro()
        elif values['Valor']<1 or values['Valor']>100:
            janela_dif_d.hide()
            janela_error = janela_erro()
        else:
            if values['Valor'] == gera_aleatorio(3):
                janela_dif_d.hide()
                janela_ac = janela_acertou()
            else:
                janela_dif_d.hide()
                janela_er = janela_errou()


    if window == janela_er and event == 'Recomeçar':
        janela_er.hide()
        janela_dif.un_hide()


    if window == janela_a and event == 'Regras':
        janela_r = janela_regras()
        janela_a.hide()

    if window == janela_r and event == 'Retornar':
        janela_r.hide()
        janela_a.un_hide()

    if window == janela_a and event == 'Retornar ao menu principal':
        janela_a.hide()
        janela_p.un_hide()

    if window == janela_dif and event == 'Retornar':
        janela_dif.hide()
        janela_a.un_hide()
    # Janela do jogo DADOS

    if window == janela_d and event == 'Jogar os dois dados':
        janela_j_dd = janela_joga2dados()
    if window == janela_j_dd and event == 'Concluído':
        janela_j_dd.hide()
        janela_d.un_hide()

    if window == janela_d and event == 'Jogar somente um dado':
        janela_j_d = janela_joga1dado()

    if window == janela_j_d and event == 'Concluído':
        janela_j_d.hide()
        janela_d.un_hide()

    if window == janela_d and event == 'Retornar ao menu principal':
        janela_d.hide()
        janela_p.un_hide()
