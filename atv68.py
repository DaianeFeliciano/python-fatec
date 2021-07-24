from math import sqrt
import sys
tecla = 0
a = 0
b = 0
c = 0
delta =0
tecla = int(input("\nMenu\n1 Leitura\n2 Calcular\n3 Exibir\n4 Sair\nItem:"))

if  tecla == 1:
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

elif tecla == 2:
        delta = (b ** 2 - 4 * a * c)
elif tecla == 3:
    print("O valor de a tem que ser diferente de zero")

elif delta > 0 or delta == 0:
     raiz = sqrt(delta)
     a2 = 2 * a
     x1 = (-b + raiz) / a2
     x2 = (-b - raiz) / a2
     print("O Delta da equação de segundo grau é {:.2f}\n"
    "A raiz de delta é {:.2f}\n e x1 = {:.2f} e x2 = {:.2f}".format(delta, raiz, x1, x2))
else:
    print("Sem solução no conjunto dos números reais")
if tecla == 4:
    print("Programa finalizado")
    sys.exit()
