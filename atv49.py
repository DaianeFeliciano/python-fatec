"""2. Escreva um programa para ler 3 valores inteiros e escrever o maior deles. Considere que o usuário
não informará valores iguais, valores nulos ou valores negativos."""

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))
if n1 > n2 and n1 > n3:
    print("O maior número inteiro é {}".format(n1))
elif n2 > n1 and n2 > n3:
    print("O maior número inteiro é {}".format(n2))
else:
    print("O maior número inteiro é {}".format(n3))

