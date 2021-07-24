import sys

a = 0
b = 0
c = 0
tecla = 0

tecla = int(input("\nMenu\n1 Ler e Exibir\n2 Sair\nItem:"))
if tecla == 1:
    a = float(input("\nDigite o primeiro lado:"))
    b = float(input("\nDigite o segundo lado:"))
    c = float(input("\nDigite o terceiro lado:"))
    if a < b + c and b < a + c and c < a + b:
        triangulo = True
    else:
        triangulo = False
    if triangulo == True:
        print("Tratasse de um triângulo")
    else:
        print("Uma figura qualquer de três lados")
elif tecla == 2:
    sys.exit()
