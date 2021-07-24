from math import pow, sqrt

print("Cálculo Equação de 2º grau")
a = float(input('Digite o valor de a: '))

# vamos verificar se o A é zero, se for trará mensagem de erro, senao pediremos B e C
if a == 0:
    print("O valor de a tem que ser diferente de 0 para seguir com a equação de segundo grau!")
else:
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))

    # calculamos o delta independente do valor de A, pois isso nao dará erros
    delta = pow(b, 2) - (4 * a * c)

    # nao é mais else if, se tornou um novo if
    if delta > 0:
        raiz = sqrt(delta)
        a2 = 2 * a
        x1 = (- b + raiz) / a2
        x2 = (- b - raiz) / a2

        print("O delta da equacão de 2º grau é  {:.2f}\n A raiz de delta é {:.2f} "
              "\ne as duas raízes encontradas na equação de 2º grau é x1 = {:.2f} "
              "e x2 = {:.2f}".format(delta, raiz, x1, x2))

    elif delta == 0:
        raiz = sqrt(delta)
        a2 = 2 * a
        x1 = (- b + raiz) / a2
        x2 = (- b - raiz) / a2

        print("O delta da equacão de 2º grau é {}\n A raiz de delta é {} "
              "\ne as duas raízes encontradas na equação 2º grau são iguais, pois delta é igual a zero sendo =  x1 {} e "
              "x2 {}".format(
            delta, raiz, x1, x2))
    else:
        print("O delta da equacão de 2º grau é negativo, sendo {} e as raízes não possuem valores reais".format(delta))





