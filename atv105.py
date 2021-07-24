import os
import sys

def lerNumero():

    N = int(input('Digite um número: '))
    return N

def numeroParouImpar(N):

    if N % 2 == 0:
        print("Número {} é par".format(N))
        return True
    else:
        print("Número {} é impar".format(N))
        return False


def numeroPrimo(N):
    contdiv = 0;
    for i in range(1, N + 1, 1):
        if N % i == 0:
            contdiv += 1;  # incrementa 1 ao contdiv

    if contdiv == 2:
        return True  # é primo
    else:
        return False  # não é primo


def somaPrimos( x, y ):
    somaprimo=0
    for i in range (x, y+1):
        if numeroPrimo (i):
            somaprimo+= i # acumular os pares somapar = somapar + i
    return somaprimo


def controle():

    itemMenu = 0

    linhasMenu = '\n\033[1;96m**Menu de Controle**\033[m'
    linhasMenu += '\n 1 Ler'
    linhasMenu += '\n 2 Par ou Impar'
    linhasMenu += '\n 3 Verificar Primo'
    linhasMenu += '\n 4 Somar Primo'
    linhasMenu += '\n 5 Sair'
    linhasMenu += '\n Item: '

    while True:

        itemMenu = int(input(linhasMenu))

        if itemMenu == 1:
            numero = lerNumero()

        elif itemMenu == 2:
            parouimpar = numeroParouImpar(numero)

        elif itemMenu == 3:
            primo = numeroPrimo(numero)
            status = numeroPrimo(numero)
            if status:
                print(f'O número {numero} é um número primo.')
            else:
                print(f'O número {numero} não é um número primo.')

        elif itemMenu == 4:
            x = somaPrimos(1,numero)
            print('A soma dos números primos de 1 até {} é {}'.format(numero, x))

        elif itemMenu == 5:

            print("Programa Finalizado")

            break

    sys.exit()

controle()
