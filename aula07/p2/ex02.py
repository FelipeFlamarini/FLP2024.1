# (25% pontos) Implemente a função contida: Recebe duas strings. Retorna True ou False dependendo
# se a primeira string possui todos os caracteres da segunda string ou não. Deve ser usada a classe set.

def contida(str1 : str, str2 : str):
    if set(str1) > set(str2):
        return True
    return False