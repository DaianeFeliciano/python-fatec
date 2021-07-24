# soma dos números ímparas entre a e b
import os
import sys
i = 0
soma = 0

def Informativo():
    informativo = '\033[1;92m \n**Digite a seguir 2 números inteiros para saber a ' \
                  'soma dos ímpares entre eles**\033[m '
    print(informativo)
    return informativo


def LerA():
    a = int(input('Digite o primeiro número: '))
    return a


def LerB():
    b = int(input('Digite o segundo número: '))
    return b


def CalcularImpar(a, b):
    i = 0
    soma = 0
    for i in range(a, b):
        if i % 2 != 0:
            soma = soma + i

    print('A soma dos números ímpares entre {} e {} é {}'.format(a,b,soma))
    return soma

def Informativo2():
    informativo2 = '\033[1;35m \n**Digite a seguir um número inteiro para saber o seu Fatorial**\033[m'
    print(informativo2)
    return

# calcular Fatorial
def LerNum():
    Num = int(input('Digite um número: '))
    return Num


def CalcularFatorial(Num):
    Aux = 1
    for n in range(1, Num + 1):
        Aux = Aux * n
    print('O fatorial de  {} é  {}'.format(Num,Aux))
    return Aux

def Aviso():
    aviso = '\033[1;31m\n**Dados armazenados com sucesso! Clique na ' \
            'opção 2 para saber o resultado!**\033[m'
    print(aviso)
    return aviso

def controleCapital ():

    itemMenu = 0

    linhasMenu = '\n\033[1;96m**Menu de Controle**\033[m'
    linhasMenu += '\n 1 Ler'
    linhasMenu += '\n 2 Calcular e Mostrar'
    linhasMenu += '\n 3 Sair'
    linhasMenu += '\n Item: '

    while True:

        itemMenu = int(input(linhasMenu))

        if itemMenu == 1:
            infor = Informativo()
            LA = LerA()
            LB = LerB()
            infor2 = Informativo2()
            LN = LerNum()
            avisado = Aviso()

        elif itemMenu == 2:
            impar = CalcularImpar(LA,LB)
            fatorial = CalcularFatorial(LN)
            print('	\033[1;31m\nCalculado com sucesso!\033[m')

        elif itemMenu == 1 and itemMenu == 2:
            print('	\033[1;31m\n Digite 1 para leitura de dados para novo cálculo ou 2 '
                  'para sair da aplicação!\033[m')


        elif itemMenu == 3:
            print('\n\033[1;31mO programa foi finalizado\033[m')

            break

    sys.exit()

controleCapital()