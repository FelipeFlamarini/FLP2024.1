# Dicionário de definição de palavras
# Melhore a solução proposta para o problema do dicionário de palavras definido anteriormente. 
# Crie uma API com os seguintes métodos:

# set(word, definition): Adiciona ou modifica a definição de uma palavra.
# get(word): Retorna a definição de uma palavra. Se a palavra não existir no dicionário, 
# retorna uma mensagem indicando que a palavra não foi encontrada.
# get_word_order(word): Retorna a ordem em que uma palavra foi adicionada/modificada no dicionário. 
# A ordem deve ser um número inteiro representando a posição da palavra na sequência de adições/modificações.
# get_all_words(): Retorna uma lista com todas as palavras presentes no dicionário, na ordem em que 
# foram adicionadas/modificadas.
from collections import defaultdict, namedtuple

class dictionary:
    _wordDefinition = namedtuple("wordDefinition", ("definition", "lastUpdated"))
    _update = 0
    
    def __init__(self):
        self._words = defaultdict(lambda : self._wordDefinition(0, self._updateCounter()))
        
    def _updateCounter(self):
        self._update += 1
        return self._update
            
    def set(self, word : str, definition : str):
        self._words[word.lower()] = self._wordDefinition(definition, self._updateCounter())
    
    def get(self, word : str):
        return self._words[word].definition if self._words[word].definition != 0 else "Essa palavra não existe nesse dicionário."
    
    def get_word_order(self, word : str):
        for index, wordSearch in enumerate(self.get_all_words()):
            if wordSearch == word:
                return index
    
    def get_all_words(self):
        return [word[0] for word in sorted(self._words.items(), key=lambda e : e[1].lastUpdated) if word[1].definition != 0]

dictionary1 = dictionary()
dictionary1.set("pindaíba", "falta de dinheiro")
dictionary1.set("gororoba", "comida duvidosa")
dictionary1.set("bugiganga", "quinquilharia")
dictionary1.set("bizu", "ideia")

dictionary1.set("gororoba", "comida duvidosa")

print(dictionary1.get("pindaíba"))
print(dictionary1.get("gororoba"))
print(dictionary1.get("abc"))

print(dictionary1.get_word_order("pindaíba"))
print(dictionary1.get_word_order("bizu"))

print(dictionary1.get_all_words())