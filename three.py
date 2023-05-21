nome = []
opcao = 0
import random

while True:
    opcao = int(input("Digite 1 para inserir uma nova pessoa, 0 para sair ou 3 para sortear: "))
    if opcao == 0:
        break
    elif opcao == 1:
        nome.append(input("Digite o nome da pessoa: "))
    elif opcao == 3:
        numSorteado = random.randrange(0, len(nome))
        print(numSorteado)
        print("A pessoa sorteada foi: {}".format(nome[numSorteado]))
        break
    else:
        print("Opcao invalida")
        


