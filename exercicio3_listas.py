lista=[]
while True:
    print("Digite 'FIM' para encerrar a lista")
    felipe=input("Digite elementos da lista:\n")
    if felipe.upper()=="FIM":
        print("LISTA 1 ENCERRADA.\n")
        break

    lista.append(felipe)

lista1=[]
while True:
    print("Digite 'FIM' para encerrar a lista")
    lara=input("Digite elementos da lista 2:\n")
    if lara.upper()=="FIM":
        print("LISTA 2 ENCERRADA.\n")
        break

    lista1.append(lara)

q=len(lista)
q1=len(lista1)

if q>q1:
    print("A lista 1 é maior que a lista 2")
elif q1>q:
    print("A lista 2 é maior que a lista 1")
else:
    print("As listas têm o mesmo tamanho")