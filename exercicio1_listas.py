#atividade 1 - listas 

impar=0
par=0

lista=[]
for i in range (1,11):
    i=int(input(f"Digite o {i}º número:"))
    lista.append(i)
    if i%2==0:
        par+=1
    else:
        impar+=1

print(f"Há {impar} números ímpares e {par} números pares na lista")