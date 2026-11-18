import math

L=[]

while True:
    print("Digite 'FIM' para encerrar a lista")
    numerais = input("Digite numerais para a lista:\n")
    if numerais.strip().upper() == "FIM":
        print("Lista encerrada.\n")
        break
    vinicius = int(numerais)

L.append(vinicius)
maior_numero=max(L)
menor_numero=min(L)

print(f"A média geométrica dos maior número e do menor número listados é: {math.sqrt(maior_numero*menor_numero)} ")

