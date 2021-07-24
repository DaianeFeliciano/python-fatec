#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print('-+'*10)
print("Par ou ímpar? ")
print('-+'*10)
n1 = int(input("Digite um número para saber se é par ou ímpar: "))
if n1%2==0:
    print("O número é par, sendo {}".format(n1))
else: print("Número é ímpar,sendo {}".format(n1))