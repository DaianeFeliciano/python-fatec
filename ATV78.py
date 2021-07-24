n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = int(input("Digite o terceiro número inteiro: "))
n4 = int(input("Digite o quarto número inteiro: "))

if   (n1 > n2  and n2 > n3 and n3 > n4):
    print("A ordem crescente dos valores é {}, {}, {}  e {}".format(n4,n3,n2,n1))
elif (n2 > n1 and n1 > n3 and  n3 > n4 ):
    print("A ordem crescente dos valores é {}, {}, {} e {}".format(n4,n3,n1,n2))
elif (n3 > n1 and n1 > n2 and n2 > n4):
    print("A ordem crescente dos valores é {}, {}, {} e {}".format(n4,n2,n1,n3))
elif (n4 > n1 and n1> n2 and n2 > n3):
    print("A ordem crescente dos valores é {}, {}, {} e {}".format(n3,n2,n1,n4))
elif (n1 > n2 and n2 > n4 and n4 > n3):
    print("A ordem crescente dos valores é {}, {}, {} e {}".format(n3,n4,n2,n1))
elif (n1 > n3 and n3 > n4 and n4 > n2):
    print("A ordem crescente dos valores é {}, {}, {} e {}".format(n2,n4,n3,n1))
elif (n1> n4 and n4 > n3 and n3 > n2):
    print("A ordem crescente dos valores é {}, {}, {} e {}".format(n2,n3,n4,n1))
elif (n2 > n1 and n1 > n3 and n3 > n4):
    print("A ordem crescente dos valores é {}, {}, {} e {}".format(n4, n3, n1, n2))
elif (n2 > n3 and n3 > n1 and n1 > n4):
    print("A ordem crescente dos valores é {}, {}, {} e {}".format(n4, n1, n3, n2))
elif (n2 > n4 and n4 > n1 and n1 > n3):
    print("A ordem crescente dos valores é {}, {}, {} e {}".format(n3, n1, n4, n2))
    print("A ordem crescente dos valores é {}, {}, {} e {}".format(n2,n3,n4,n1))
elif (n3 > n1 and n1 > n2 and n2 > n4):
    print("A ordem crescente dos valores é {}, {}, {} e {}".format(n4, n2, n1, n3))
elif (n3 > n2 and n2 > n1 and n1 > n4):
    print("A ordem crescente dos valores é {}, {}, {} e {}".format(n4, n1, n2, n3))
elif (n3 > n4 and n4 > n2 and n2 > n1):
    print("A ordem crescente dos valores é {}, {}, {} e {}".format(n1, n2, n4, n3))
elif (n4 > n1 and n1 > n2 and n2 > n3):
    print("A ordem crescente dos valores é {}, {}, {} e {}".format(n3, n2, n1, n4))
elif (n4 > n2 and n2 > n1 and n1 > n3):
    print("A ordem crescente dos valores é {}, {}, {} e {}".format(n3, n1, n2, n4))
elif (n4 > n3 and n3 > n1 and n1 > n2):
    print("A ordem crescente dos valores é {}, {}, {} e {}".format(n2, n1, n3, n4))









