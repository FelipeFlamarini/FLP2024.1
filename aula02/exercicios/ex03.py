# Sistema de eleições
# Crie um programa para gerenciar uma eleição. Primeiramente, será necessário cadastrar os 
# candidatos e associá-los às suas respectivas chapas. Em seguida, o programa deverá ler a 
# lista de votos, onde cada voto é representado pelo número da chapa do candidato votado.

# Primeiramente o programa lê a quantidade de candidatos, seguida pelo número da chapa e o nome 
# (única palavra, sem espaços) de cada candidato. 
# Depois o programa lê a quantidade de votos, seguida pelos números das chapas votadas. 
# Caso haja algum número sem chapa cadastrada, considerar como voto nulo. 
# Por fim, o programa deve exibir os dois candidatos mais votados, e a mensagem "SEM SEGUNDO TURNO" 
# ou "COM SEGUNDO TURNO", 
# caso o primeiro candidato tenha conseguido mais de 50% dos votos ou não. 
# Caso haja empate, o critério de desempate é a ordem alfabética. A entrada e saída de dados 
# deve obedecer ao seguinte padrão de exemplo:
# Entrada   Saída
# 3         Sicrano
# 14	    Beltrano
# Fulano	COM SEGUNDO TURNO
# 42	
# Beltrano	
# 20	
# Sicrano	
# 5	
# 20	
# 14	
# 0	
# 42	
# 20

from collections import defaultdict

class Election:
    def __init__(self):
        self._candidates = defaultdict(lambda : {"candidate": "", "votes": 0})
        self._candidates[0]["candidate"] = "Nulo"
        
    def _getAllVotes(self):
        votes = [parties for parties in sorted(list(self._candidates.items()), key=lambda x : (-x[1]["votes"], x[1]["candidate"], x[1]["candidate"] == "Nulo"))]
        # resolve primeiro ou segundo turno
        # se há segundo turno (número de votos do maior colocado > 50%), o primeiro elemento da list é true
        # se não, false
        if votes[0][1]["votes"] > len(votes) / 2:
            votes.insert(0, True)
        else:
            votes.insert(0, False)
        return votes    
    
    def _incrementVote(self, party : int):
        self._candidates[party]["votes"] += 1
    
    def _getCandidate(self, party : int):
        return self._candidates[party]["candidate"]
    
    def _setCandidate(self, party : int, candidate : str):
        if " " in candidate:
            raise Exception("Utilize apenas nome de palavra única, sem espaços")
        self._candidates[party]["candidate"] = candidate
        
    def startRegistering(self):
        candidatesNumber = int(input()) # "Digite o número de candidatos: "
        for _ in range(candidatesNumber):
            party = int(input()) # "Digite o número do partido: "
            candidate = str(input()) # "Digite o nome do candidato: "
            if self._getCandidate(party) == "":
                self._setCandidate(party, candidate)
            else:
                raise Exception("O partido já possui candidato")
        print()
            
    def startVoting(self):
        votesNumber = int(input()) # "Digite o número de votos: "
        for _ in range(votesNumber):
            party = int(input()) # "Digite o número do partido a ser votado: "
            if self._getCandidate(party) != "":
                self._incrementVote(party) 
            else:
                self._incrementVote(0)
                          
    def end(self):
        result = self._getAllVotes()
        print(result[1][1]["candidate"])
        print(result[2][1]["candidate"])
        if result[0]:
            print("COM SEGUNDO TURNO")
        else:
            print("SEM SEGUNDO TURNO")
        print(result)
            
election1 = Election()
election1.startRegistering()
election1.startVoting()
election1.end()