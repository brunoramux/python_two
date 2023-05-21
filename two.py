qtdAlunos = 0
idades = []
menorIdade = 0
maiorIdade = 0

while True:
    idade = int(input("Digite a idade do aluno {}: ".format(qtdAlunos+1)))
    if idade < 0:
        break
    else:
        idades.append(idade)
        qtdAlunos += 1

if qtdAlunos != 0:
    menorIdade = min(idades)
    maiorIdade = max(idades)
    print("A media entre a menor e a maior idade e: {}".format((menorIdade + maiorIdade) / 2))