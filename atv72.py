import sys
tecla = int( input ("\nMenu\n1 Executar \n2 Sair\nItem:"))
if tecla == 1:
    N1 = int(input("\nDigite n1:"))
    N2 = int(input("\nDigite n2:"))
    N3 = int(input("\nDigite n3:"))
    N4 = int(input("\nDigite n4:"))
    N5 = int(input("\nDigite n5:"))

    lista = [N1, N2, N3, N4, N5]
    lista_ordenada = sorted(lista)
    maior = lista_ordenada[4]
    menor = lista_ordenada[0]
    print("\nO maior número é {} e o menor é {}".format(maior,menor))
elif tecla == 2:
    sys.exit ()