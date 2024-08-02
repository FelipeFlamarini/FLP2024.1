# print("iniciando script")
# pegando caracteres precificados
n_caracteres_precificados = int(input())
if n_caracteres_precificados <= 0 or n_caracteres_precificados > 100:
    raise Exception("Esse número deve valer de 1 a 100")
caracteres_precificados = {}

for i in range(n_caracteres_precificados):
    caracter_valor = str(input()) # input deve estar no formato "letra valor". Exemplos: "a 3", "A 99"
    caracter, valor = caracter_valor.split(" ")
    caracteres_precificados.update({caracter: int(valor)})

# recebendo arquivos de texto
n_arquivos_texto = int(input())
if n_arquivos_texto <= 0 or n_arquivos_texto > 5:
    raise Exception("Esse número deve valer de 1 a 5")

valores_artigos = []
for n_arquivo in range(n_arquivos_texto):
    caminho_arquivo_texto = str(input())
    
    valores_artigos.append(0)
    with open(caminho_arquivo_texto, "r") as arquivo_texto:
        texto_linhas = arquivo_texto.readlines()
        if len(texto_linhas) > 150000:
            raise Exception("Os artigos devem ter no máximo 150000 linhas")
        
        for linha in texto_linhas:
            if len(linha) > 10000:
                raise Exception("As linhas dos artigos devem ter no máximo 10000 caracteres")
            
            for caracter in linha:
                if caracter in caracteres_precificados.keys():
                    valores_artigos[n_arquivo] += caracteres_precificados[caracter]

for i in range(len(valores_artigos)):
    print(f"R${str(valores_artigos[i]/100).replace(".", ",")}")