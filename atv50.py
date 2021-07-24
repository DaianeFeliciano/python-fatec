a = int(input("Primeiro lado do triângulo: "))
b = int(input("Segundo lado do triângulo: "))
c = int(input("Terceiro lado do triângulo: "))
if a >= (b+ c) or b >=(a+c) or c >= (b+a):
    print("Não é um triângulo!")
elif a == b and a == c and b ==c:
    print("É um triângulo EQUILÁTERO!")
elif a != b and a != c and b !=c:
    print("É um triângulo ESCALENO!")
else:
    print("É um triângulo ISÓSCELES!")







#if a or b or c >= (b+c) and a or b or c >= (a+b) and a or b or c >= (a+c):