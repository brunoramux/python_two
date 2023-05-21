class Atleta:
    def __init__(self, id, nome, tempo):
        self.id = id
        self.nome = nome
        self.tempo = tempo

atletas = []
indexMelhor = -1
indexPior = -1
melhor_tempo = 0.0
piorTempo = 0.0
somaTempo = 0.0
qtdAtletas = 0


for i in range (0, 7):
    id = i
    nome = input("Digite o nome do atleta {}: ".format(i+1))
    tempo = float(input("Digite o tempo (em segundos) do atleta {}: ".format(i+1)))
    atletas.append (Atleta(id, nome, tempo))
    
print (atletas[1].tempo)

for obj in atletas:
    if indexMelhor == -1:
        indexMelhor = obj.id
        melhor_tempo = obj.tempo
    elif obj.tempo < melhor_tempo:
        indexMelhor = obj.id
        melhor_tempo = obj.tempo
    if indexPior == -1:
        indexPior = obj.id
        piorTempo = obj.tempo
    elif obj.tempo > piorTempo:
        indexPior = obj.id
        piorTempo = obj.tempo
    somaTempo += obj.tempo
    if obj.tempo >= 12 and obj.tempo <= 15:
        qtdAtletas += 1
    
        
print("Atleta com melhor tempo: {}".format(atletas[indexMelhor].nome))
print("Atleta com pior tempo: {}".format(atletas[indexPior].nome))
print("Media dos tempos entre os atletas: {}".format(somaTempo / 7))
print("Quantidade de atletas com tempo entre 12s e 15s: {}".format(qtdAtletas))
  

