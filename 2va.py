from time import sleep
import os
import random

#próximas funções é da interface
def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def cabeçalho2(txt):
    print(txt.center(42))


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\m\033[31nEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def menu1(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc


def menu2(lista):
    cabeçalho2('\033[35mALTERNATIVAS\033[m')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc


while True:
    resposta = menu1(['Começar jogo', 'Adicionar perguntas', 'Sair'])
    if resposta == 1:
        cabeçalho('Começar jogo')
        while True:
            decisao = int(input('digite 1 para começar/continuar ou 2 para voltar ao menu: '))
            if decisao == 1:
                file = open('perguntas.txt', 'r')
                Counter = 0

                Content = file.read()
                CoList = Content.split('\n')

                for i in CoList:
                    if i:
                        Counter += 1

                k = Counter

                s = random.randrange(1,k)

                with open('perguntas.txt') as f:
                    data = f.readlines()[s]
                    line = data.rstrip('\n')
                    dados = []
                    dados.append(line)

                with open('alternativas.txt') as a:
                    data1 = a.readlines()[s]
                    line1 = data1.rstrip('\n')
                    line_1 = line1.split(' ')
                    dados1 = []
                    dados1.append(line_1)
                with open('resposta.txt') as re:
                    data2 = re.readlines()[s]
                    line2 = data2.rstrip('\n')
                    line_2 = line2.split(' ')
                    dados2 = []
                    dados2.append(line_2)
                    line3 = int(line2)

                sleep(1)

                print(f'\n{line}')
                resposta1 =int(input(f'\n ALTERNATIVAS\n\n {line1}\n\nResponda com o número inteiro correspondente: '))
                sleep(1)

                if resposta1 == line3:

                    print('\nParabéns você acertou!!!')
                else:
                    print('\nque pena você errou')
                print(linha())
            else:
                break
        continue

    elif resposta == 2:
        cabeçalho('Adicionar perguntas')
        adiconar = input('Digite a pergunta que deseja adicionar: ')
        with open('perguntas.txt', 'a') as addpergunta:
            addpergunta.write(f'\n{adiconar}')

        adiconaral = input('Digite as alternativas da pergunta: ')
        with open('alternativas.txt', 'a') as addalternativas:
            addalternativas.write(f'\n{adiconaral}')

        adiconarre = input('Digite o número que coresponde a resposta correta: ')
        with open('resposta.txt', 'a') as addresposta:
            addresposta.write(f'\n{adiconarre}')
    elif resposta == 3:
        cabeçalho('Saindo do jogo... Até a próxima!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(2)

