lst_clientes = [
    {'razaoSocial':'LA Transportes', 'totalCompras': 1},
    {'razaoSocial':'NY Tranportes', 'totalCompras': 2},
    {'razaoSocial':'SP Transportes', 'totalCompras': 3},
    {'razaoSocial':'MG Transportes', 'totalCompras': 4},
    {'razaoSocial':'DF Trasnportes', 'totalCompras': 5}
]

def getKey(lista):
      return lista['razaoSocial']
  
lst_clientes.sort(key=lambda cliente: cliente['totalCompras'], reverse=True)

for list in lst_clientes:
    print(list)