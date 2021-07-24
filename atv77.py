n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = int(input("Digite o terceiro número inteiro: "))
n4 = int(input("Digite o quarto número inteiro: "))

if n1 % 2 == 0 and n1 % 3 == 0:

    print("O {} é divisível por 2 e 3".format(n1))
elif n2 % 2 == 0 and n2 % 3 == 0:
    print("O {} é divisível por 2 e 3".format(n2))
elif n3 % 2 == 0 and n3 % 3 == 0:
    print("O {} é divisível por 2 e 3".format(n3))
elif n4 % 2 == 0 and n4 % 3 == 0:
    print("O {} é divisível por 2 e 3".format(n4))
else:
    print("Os numeros não divisíveis por 2 e 3 ao mesmo tempo")
