#calcular quantidade de números pares
import os
import sys
i = 0
soma = 0

def Lern():
    n = int(input('Digite um número: '))
    return n


def Calpar(n):
    par = 0
    for i in range(par,n+1):
        if i % 2 == 0:
            par = par +1

    return par

def Calimpar(n):
    impar = 0
    for i in range(impar, n+1):
        if i % 2 != 0:
                impar = impar + 1
    return impar

def Exibir(Calpar, Calimpar):

    print('Quantidade de número par: {}'.format(Calpar))
    print('Quantidade de número impar: {} '.format(Calimpar))


def controle ():

    itemMenu = 0

    linhasMenu = '\n\033[1;96m**Menu de Controle**\033[m'
    linhasMenu += '\n 1 Ler'
    linhasMenu += '\n 2 Calcular'
    linhasMenu += '\n 3 Exibir'
    linhasMenu += '\n 4 Sair'
    linhasMenu += '\n Item: '

    while itemMenu != 4:

        itemMenu = int(input(linhasMenu))

        if itemMenu == 1:

            ln = Lern()

        elif itemMenu == 2:

            calp =  Calpar(ln)
            calim = Calimpar(ln)

        elif itemMenu == 3:

            Exibir(calp,calim)
            break

    sys.exit()

controle()