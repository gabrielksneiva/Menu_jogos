#Classe Adivinhação, cria o jogo Adivinhação.
class Adivinhacao:
    #Função escolha, analisa a escolha do jogador e trata alguns erros possíveis.
    def escolha(self):
        for j in range(49, 0, -1):
            try:
                escolha = int(input("Escolha: "))
                i = True
                while i == True:
                    i =self.valida_escolha(escolha)
                    if i == True:
                        print("Erro, por favor digite um valor válido!")
                        escolha = int(input("Escolha: "))
                break
            except:
                print("Erro, caractere inválido!")
                print(f"Digite novamente (você só tem mais {j} chances de digitar um valor correto!) ")
        return escolha
    #Função valida_escolha, valida se a escolha do usuário é pertinente.
    def valida_escolha(self, opcao):
        if opcao == 1 or opcao == 2 or opcao == 3:
            i = False
        else:
            i = True
        return i
    #Função escolher_dificuldade, mostra as opções de dificuldade e retorna a dificuldade escolhida (também trata os erros)
    def escolher_dificuldade(self):
        estetica('                 DIFICULDADE                 ')
        print("""
        Você escolheu jogar!
        Escolha entre as dificuldades abaixo:
        1 - Fácil
        2 - Médio
        3 - Difícil
        """)
        for i in range(49,0, -1):
            try:
                escolha_dif = self.escolha()
                if escolha_dif == 1:
                    dificuldade = 'fácil'
                elif escolha_dif == 2:
                    dificuldade = 'médio'
                else:
                    dificuldade =  'difícil'
                break
            except:
                print("Erro, caractere inválido!")
                print(f"Digite novamente (você só tem mais {i} chances de digitar um valor correto!) ")
        return dificuldade
    #Função jogo, é o jogo em si, onde se divide as dificuldades, gerando um inteiro aleatório e pede para o jogador tentar adivinhar.
    def jogo(self, dif):
        from random import randint
        if dif == 'fácil':
            x = randint(1, 10)
            n = 0
            while n < 3:
                advinhar = int(input("Tente adivinhar um número entre 1 e 10: "))
                if advinhar < 1 or advinhar > 10:
                    print("Por favor, escolha um valor entre 1 e 10")
                else:
                    if x == advinhar:
                        break
                    else:
                        n = n + 1
            if n == 3:
                print("")
                print("Que pena! Você perdeu!\n" + f"O número era {x}")
            else:
                print("")
                print("Você ganhou!!!!!!!\n" + f"O número era {x}")
        elif dif == 'médio':
            x = randint(1, 50)
            n = 0
            while n < 3:
                advinhar = int(input("Tente adivinhar um número entre 1 e 50: "))
                if advinhar < 1 or advinhar > 50:
                    print("Por favor, escolha um valor entre 1 e 50")
                else:
                    if x == advinhar:
                        break
                    else:
                        n = n + 1
            if n == 3:
                print("")
                print("Que pena! Você perdeu!\n" + f"O número era {x}")
            else:
                print("")
                print("Você ganhou!!!!!!!\n" + f"O número era {x}")
        else:
            x = randint(1, 100)
            n = 0
            while n < 3:
                advinhar = int(input("Tente adivinhar um número entre 1 e 100: "))
                if advinhar < 1 or advinhar > 100:
                    print("Por favor, escolha um valor entre 1 e 100")
                else:
                    if x == advinhar:
                        break
                    else:
                        n = n +1
            if n == 3:
                print("")
                print("Que pena! Você perdeu!\n" + f"O número era {x}")
            else:
                print("")
                print("Você ganhou!!!!!!!\n" + f"O número era {x}")
    #Função regras, imprimi as regras do jogo para o usuário.
    def regras(self):
        estetica('                                                 REGRAS                                                 ')
        print("""
        As regras do jogo são:
        1. Você terá 3 chances de acertar um valor definido pela dificuldade escolhida.
        2. Caso você acerte, o programa recomeçará imediatamente.
        3. Ao final das 3 tentativas, o programa exibirá uma mensagem dizendo se você ganhou ou perdeu.
        """)
    #Função sair, leva o usuário de volta para o menu principal.
    def sair(self):
        menu()
    #Função texto_inicio, cria o menu do jogo.
    def texto_inicio(self):
        estetica('                 JOGO DA ADIVINHAÇÃO                 ')
        print("""
        Boas vindas ao jogo da adivinhação!
        Escolha uma das opções abaixo para continuar:
        1 - Jogar
        2 - Regras
        3 - Sair do jogo
        """)

    #Função main, é o motor da Classe/Jogo Adivinhação.
    def main(self):
        self.texto_inicio()
        opcao = self.escolha()
        while opcao == 1 or opcao == 2:
            if opcao == 1:
                self.jogo(self.escolher_dificuldade())
            elif opcao == 2:
                self.regras()
            self.texto_inicio()
            opcao = self.escolha()
        self.sair()

#Cria a Classe Dados, ou seja, cria o jogo Dados, onde dois dados ou apenas um, são jogados e retornam os valores de suas faces.
class Dados:
    #Função jogar, joga os dados e retorna as faces dependendo da opção escolhida pelo jogador.
    def jogar(self, opcao):
        from random import randint
        face1 = randint(1, 6)
        face2 = randint(1, 6)
        faces = [face1, face2]
        if opcao == 1:
            return faces
        elif opcao == 2:
            return faces[0]
        else:
            return 'Erro na função jogar'
    #Função mostrar, mostra o valor de cada face dos dados jogados.
    def mostrar(self, face1, face2 = 0):
        estetica(f"O dado 1 teve como resultado a face {face1}")
        print("")
        if face2 != 0:
            estetica(f"O dado 2 teve como resultado a face {face2}")
    #Função iniciar, é o menu do jogo Dados.
    def iniciar(self):
        estetica('                 DADOS                 ')
        print("""
        Olá, seja bem-vindo ao programa "Dados"!
        A seguir está o menu de opções para este programa:
        1 - Jogar os dois dados
        2 - Jogar somente um dado
        3 - Sair do jogo
        """)
        i = True
        while i == True:
            opcao = int(input("Escolha: "))
            i = self.valida_escolha(opcao)
            if i == True:
                estetica("Erro, por favor digite um valor válido!")
        return opcao
    #Função sair, executa novamente o menu principal
    def sair(self):
        menu()
    #Função valida_escolha, serve para validar a escolha do jogador E fechar o laço while.
    def valida_escolha(self, opcao):
        if opcao == 1 or opcao == 2 or opcao == 3:
            i = False
        else:
            i = True
        return i
    #Função main, é o motor da Classe/Jogo Dados.
    def main(self):
        escolha = self.iniciar()
        while escolha == 1 or escolha == 2:
            if escolha == 1:
                faces = self.jogar(escolha)
                self.mostrar(faces[0], faces[1])
            else:
                face1 = self.jogar(escolha)
                self.mostrar(face1)
            escolha = self.iniciar()
        self.sair()
def estetica(msg):
    print('=' * len(msg))
    print(msg)
    print('=' * len(msg))
def menu():
    estetica('                 MENU PRINCIPAL                 ')
    print("""
    Seja bem vindo ao menu de jogos!
    Escolha a baixo qual jogo você quer iniciar!
    1 - Jogo da Adivinhação
    2 - Jogo dos Dados
    3 - Sair do programa
    """)
    dados = Dados()
    adv = Adivinhacao()
    escolha = adv.escolha()
    if escolha == 1:
        adv.main()
    elif escolha == 2:
        dados.main()
    else:
        print('\nSee you soon!!!')

        exit()


#Programa Principal

