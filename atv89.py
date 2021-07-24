import sys
idade = 0
salario = 0
maiorsal = 0
menorsal = 0
menorid_menorsal = 0
menorid_maiorsal = 0
maiorid_menorsal = 0
maiorid_maiorsal = 0
contmaior = 0
contmenor = 0
item = 1


def LerCalcular():
    global idade
    global salario
    global menorid_menorsal
    global menorid_maiorsal
    global maiorid_menorsal
    global maiorid_maiorsal
    global maiorsal
    global menorsal
    global contmaior
    global contmenor

    idade = int(input('Digite a idade: '))
    salario = float(input('Digite o salário: R$'))

    if idade < 18:
        contmenor += 1
        if contmenor == 1:
            menorid_menorsal = salario
            menorid_maiorsal = salario
        else:
            if menorid_menorsal > salario:
                menorid_menorsal = salario

            if menorid_maiorsal < salario:
                menorid_maiorsal = salario
    else:
        contmaior += 1

        if contmaior == 1:
            maiorid_menorsal = salario
            maiorid_maiorsal = salario

        else:
            if maiorid_menorsal > salario:
                maiorid_menorsal = salario

            if maiorid_maiorsal < salario:
                maiorid_maiorsal = salario

def Resultados():

    print('\n** Exibição de Resultados **')
    print('\nTotal de Menores de Idade:', contmenor,
          '\nSendo o menor salário é de R$ %.2f' % menorid_menorsal,
          '\nSendo o maior salário de R$ %.2f' % menorid_maiorsal)
    print('\nTotal de Maiores de Idade:', contmaior,
          '\nSendo o menor salário é de R$ %.2f' % maiorid_menorsal,
          '\nSendo o maior salário de R$ %.2f' % maiorid_maiorsal)


while item != 3:
    item = int(input(
        '\n** Menu de Controle***\n1 Ler e Calcular\n2 Resultados\n3 Finalizar\nitem:'))

    if item == 1:
        LerCalcular()

    if item == 2:
        Resultados()

sys.exit()