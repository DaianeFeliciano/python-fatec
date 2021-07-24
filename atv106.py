"""Faça um código para para exibir os vetores com valores
 explícitos: nome = “Sara Lemes”,”Ricardo Jafé” , salario = 12000, 10243.20 e idade=30, 45.
 O salário deverá ser exibido com 15% de aumento para os maiores de 18 anos. Faça um menu de controle. """

import sys

nome = ["Sara Lemes", "Ricardo Jafé"]
salario = [12000, 10243.20]
idade = [30, 45]


def mostrarDados():

    for i in range(0, len(idade)):
        aux = idade[i]
        if aux > 18:
            aumento = salario[i]*(15/100) + salario[i]
            print("Nome: {}\n Salário: {:.2f}\n Idade: {}\n "
                  "\033[1;96m Valor do Salário com Aumento: {:.2f}\033[m".format(nome[i],salario[i],idade[i],aumento))

def controle():

    itemMenu = 0

    linhasMenu = '\n\033[1;96m**Menu de Controle**\033[m'
    linhasMenu += '\n 1 Exibir Dados'
    linhasMenu += '\n 2 Sair'
    linhasMenu += '\n Item: '

    while True:

        itemMenu = int(input(linhasMenu))

        if itemMenu == 1:
            mostrar = mostrarDados()

        elif itemMenu == 2:

            break

    sys.exit()

controle()


