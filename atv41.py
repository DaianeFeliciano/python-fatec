#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input("Digite a primeira reta: "))
b= float(input("Digite a segunda reta: "))
c= float(input("Digite a terceira reta: "))
if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    print("É um triângulo!")
else:
    print("Não pode formar triângulo!")
