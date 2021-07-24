import os
import sys

mediaF = 0
mediaM = 0
contF= 0
contM =0
salF = 0
salM = 0
saldoF = 0
saldoM = 0
sexoF = ""
sexoM =""
sexo = ""
def LerSexoeSalario():

    global sexoM
    global sexoF
    global sexo
    global salM
    global salF

    sexo = input("Digite o seu sexo (F ou M): ").upper()

    if sexo == "F":
        sexoF = "Feminino"
        salF = float(input("Digite o seu salário: "))
    elif sexo == "M":
        sexoM = "Masculino"
        salM = float(input("Digite o seu salário: "))
    else: print("Sexo inválido, digite novamente! Por favor, digite F para Feminino ou M para Masculino!")

def LerCalcular():

    global mediaF
    global mediaM
    global saldoF
    global saldoM
    global contF
    global contM


    if sexo == "M":
        contM += 1
        saldoM += salM
        mediaM = saldoM / contM

    if sexo == "F":
        contF += 1
        saldoF += salF
        mediaF = saldoF / contF

def Resultados():

    print('\n*** Resultados F***\n Sexo {}\n O saldo é de: {:.2f}\n Media salarial: {:.2f}'.format(sexoF,saldoF,mediaF))
    print('\n*** Resultados M***\n Sexo {}\n O saldo é de: {:.2f}\n Media salarial: {:.2f}'.format(sexoM,saldoM,mediaM))

item = 0
while item != 3:
    item = int(input(
        '\n** Menu de Controle***\n1 Ler e Calcular\n2 Resultados\n3 Finalizar\nitem:'))

    if item == 1:
        LerSexoeSalario()
        LerCalcular()

    elif item == 2:
        Resultados()

sys.exit