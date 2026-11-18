#atividade 2 - listas

lista=[]
lista1=[]

lara=int(input("Quantos elementos você deseja inserir na lista?"))
lara1=int(input("Quantos elementos você deseja inserir na lista 2?"))

for i in range (1, lara+1):
    i=input(f"Insira o {i}° elemento da lista:")
    lista.append(i)

for i in range (1, lara1+1):
    i=input(f"Insira o {i}° elemento da lista 2:")
    lista1.append(i)

lista.extend(lista1)
print(f"A junção das duas listas é: {lista}")
