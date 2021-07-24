"""Faça um código contendo vetores com valores não explícitos, para armazenar o nome,
a situação do empregado que poderá ser: “efetivo” ou “estagiário” e a idade. A leitura deverá
ser feita através de um menu de controle, coloque também uma opção  para  exibir  somente  os
 nomes  dos  estagiários  e  outra  opção  para  exibir somente
  o  nome  dos  efetivos,  finalmente  uma  opção  para  exibir  os  funcionários menores de idade."""

import sys

nome = []
situacao = []
idade = []
i = 0

def leituraDados():
    i = 0
    name = input("Digite o nome do funcionário: ")
    nome.append(name)
    ida  = int(input("Digite a idade do funcionário: "))
    idade.append(ida)
    situacaoatual = input("Digite a situação do empregado(Efetivo ou Estagiário): ")
    situacao.append(situacaoatual)


def exibirDadosEstagiario():
    print('\n\033[1;96m**Funcionários - Estagiários**\033[m')
    for i in range(0, len(situacao)):
        aux = situacao[i]
        if aux == "Estagiário":
            print(f"Nome do Estagiário: {nome[i]}\n Idade: {idade[i]}\n Situação: {aux}")

def exibirDadosEfetivo():
    print('\n\033[1;96m**Funcionários - Esfetivos**\033[m')
    for i in range(0, len(situacao)):
        aux = situacao[i]
        if aux == "Efetivo":
            print(f"Nome do Estagiário: {nome[i]}\n Idade: {idade[i]}\n Situação: {aux}")

def menoresdeIdade ():
    print('\n\033[1;96m**Funcionários - Menores de Idade**\033[m')
    for i in range(0, len(idade)):
        aux = idade[i]
        if aux < 18:
            print(f"Nome do Estagiário: {nome[i]}\n Idade: {idade[i]}\n Situação: {aux}")


def controle():

    itemMenu = 0

    linhasMenu = '\n\033[1;96m**Menu de Controle**\033[m'
    linhasMenu += '\n 1 Leitura dos Dados'
    linhasMenu += '\n 2 Exibir Nome dos Estágiarios'
    linhasMenu += '\n 3 Exibir Nome dos Efetivos'
    linhasMenu += '\n 4 Exibir Funcionários menores de idade'
    linhasMenu += '\n 5 Sair'
    linhasMenu += '\n Item: '

    while True:

        itemMenu = int(input(linhasMenu))

        if itemMenu == 1:
            ler = leituraDados()
        elif itemMenu == 2:
            estagiario = exibirDadosEstagiario()
        elif itemMenu == 3:
            efetivo  = exibirDadosEfetivo()
        elif itemMenu == 4:
            idade = menoresdeIdade()
        elif itemMenu == 5:
            break

    sys.exit()

controle()
