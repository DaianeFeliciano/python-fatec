import os
import sys
def lerN1():
    #os.system('clear')
    n1=float(input('\nDigite a nota 1:'))
    return n1

def lerN2():
    #os.system('clear')
    n2=float(input('\nDigite a nota 2:'))
    return n2

def calcMedia(n1,n2):
    media=(n1+n2)/2
    return media

def mostrar( media ):
    #os.system('clear')
    print(f'\nMédia:{media}')

    if media < 6:
        status = 'Aluno Reprovado!'
    else:
        status = 'Aluno Aprovado!'

    print('\nStatus:', status)

   # os.system('sleep 3')

def controle():
    nota1=lerN1()
    nota2=lerN2()
    media=calcMedia(nota1,nota2)
    mostrar( media )

controle()
