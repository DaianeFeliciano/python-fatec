from math import pow
pi = 3.14
perimetro = float(input("Digite o perimetro: "))
diametro = (perimetro/pi)
raio = (diametro/2)
area = pow(raio,2)*pi
print("A área é de {:.2f}".format(area))

