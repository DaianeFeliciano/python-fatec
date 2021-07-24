"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

salario = float(input("Digite o salário: "))
if salario > 1250:
    aumento = (salario*0.10)+salario #(salario*15/100)
    print("Você obteve um aumento de 10%, ficou no total de {}".format(aumento))
else:
    aumento = (salario*0.15)+salario
    print("Você obteve um aumento de 15%, ficou no total de {}".format(aumento))