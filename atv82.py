import sys

tecla = 0
menu = 0
contpes = 0
salacumulado = 0
idaacumulada = 0
while tecla != 3:
    tecla = int(input("\nMenu\n1 Leitura de Dados\n2 Exibir\n3 Sair\nItem:"))

    if tecla == 1:

        nome = input("Digite o nome: ")
        salario = float(input("Digite o salário: R$ "))
        salacumulado = salacumulado + salario
        idade = int(input("Digite a idade: "))
        idaacumulada = idaacumulada + idade
        contpes = contpes + 1
        mediasal = salacumulado/contpes
    elif tecla == 2:
        print("A quantidade lida é de:  {} pessoas".format(contpes))
        print("Média salarial: {:.2f}".format(mediasal))
        mediaida = idaacumulada / contpes
        print("Média de idades: {:.2f}".format(mediaida))
    elif tecla == 3:
        break
    else:
        print("Digite novamente, por favor")
print("Fechando a aplicação...")
sys.exit()
