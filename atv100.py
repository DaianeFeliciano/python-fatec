import os
import sys

def lerMontante ():

    Montante = float(input('\n Digite o valor do Montante: ' ))
    return Montante

def getCalcularCapital (Montante):
    Juros   = (5/100)
    Periodo = (2 * 12)
    ValorCapital = Montante/(1+(Juros * Periodo))
    return ValorCapital

def exibirCapital (ValorCapital):

    print('O valor do Capital aplicado é de: R$ {:.2f}'.format(ValorCapital))

def controleCapital ():

    itemMenu = 0

    linhasMenu = '\n**Menu Cálculo do Capital**'
    linhasMenu += '\n 1 Ler'
    linhasMenu += '\n 2 Calcular'
    linhasMenu += '\n 3 Mostrar'
    linhasMenu += '\n 4 Sair'
    linhasMenu += '\n Item: '
    while True:

        itemMenu = int(input(linhasMenu))

        if itemMenu == 1:
            LerM = lerMontante()

        elif itemMenu == 2:
            CalC = getCalcularCapital(LerM)
            print('\nCalculado com sucesso!')


        elif itemMenu == 3:
            exibirCapital(CalC)

        elif itemMenu == 4:
            print('\nO programa foi finalizado')

            break

    sys.exit()

controleCapital()
