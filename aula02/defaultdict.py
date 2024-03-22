# Define um valor default para cada chave individualmente na linha 5
def letter_frequency(sentence):
    frequencies = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1
        # frequencies[letter] += 1
        # não é obrigatório usar a variável frequency, mas é uma boa prática, porque ela já foi criada
    return frequencies

print(letter_frequency("banana"))
print(letter_frequency("banana").keys())

letraTeste = "x"
try:
    print(letter_frequency("banana")[letraTeste])
except:
    print(f"A chave {letraTeste} não existe no dicionário")
    
print()

# Define um valor default para todas as chaves, ao mesmo tempo, na linha 15
from collections import defaultdict
def letter_frequency2(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies

print(letter_frequency2("banana"))
print(letter_frequency2("banana").keys())

# Apesar de não existir a chave "x" no dicionário, o valor default (por conta da classe int) é 0, portanto, não gera erro
try:
    print(letter_frequency2("banana")[letraTeste])
except:
    print(f"A chave {letraTeste} não existe no dicionário")