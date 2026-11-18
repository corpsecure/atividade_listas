import random

cadastrados = []

while True:
    print("Digite 0 ou 1 para encerrar a lista")
    fv = input("Digite o nome da pessoa cadastrada:\n")

    if fv == "0" or fv == "1":
        print("LISTA ENCERRADA.\n")
        break

    cadastrados.append(fv)

if len(cadastrados) == 0:
    print("Nenhuma pessoa foi sorteada, tente novamente.")
else:
    random.shuffle(cadastrados)
    print(f"O sorteado dos cadastrados é: {random.choice(cadastrados)}")