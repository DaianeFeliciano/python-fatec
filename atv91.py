import os
import sys
import math

def lerCompri():

    comprimento = float(input('\nDigite o comprimento:'))
    return comprimento

def getCalcularD(comprimento):
    diametro = (comprimento/3.14)
    return diametro

def getCalcularR(diametro):
    raio = diametro/ 2
    return raio

def getCalcularA(raio):
    area = pow(raio,2)*3.14
    return area

def exibir(diametro,raio,area):

    print("Diametro: {:.2f}\n Raio: {:.2f} \n Area: {:.2f}".format(diametro,raio,area))

def controle():
    itemMenu = 0

    linhasMenu = '\n*** Menu de Controle ***'
    linhasMenu += '\n1 Ler...'
    linhasMenu += '\n2 Calcular...'
    linhasMenu += '\n3 Mostrar...'
    linhasMenu += '\n4 Sair...'
    linhasMenu += '\nSelecione operação:'

    while True:

        itemMenu = int(input(linhasMenu))

        if itemMenu == 1:
            compri = lerCompri()

        elif itemMenu == 2:
            diamet = getCalcularD(compri)
            rai = getCalcularR(diamet)
            are = getCalcularA(rai)
            print('\nCalculado com sucesso!')


        elif itemMenu == 3:
            exibir(diamet, rai, are)

        elif itemMenu == 4:
            print('\nO programa foi finalizado')

            break

    sys.exit

controle()