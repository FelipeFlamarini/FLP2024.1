# (25% pontos) Implemente a função combinar_listas: Recebe duas listas. Combina os elementos das
# duas listas em uma lista de tuplas, onde cada tupla conterá os próximos itens de cada lista. Retorna a lista
# de tuplas. Caso as listas sejam de tamanhos diferentes, levantar uma exceção. Deve ser usada a função zip.

def combinar_listas(lista1 : list, lista2 : list):
    if len(lista1) != len(lista2):
        raise Exception("As listas devem possuir o mesmo comprimento")
    
    return list(zip(lista1, lista2))