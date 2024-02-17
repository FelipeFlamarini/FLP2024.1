from collections import defaultdict
 
num_items = 0
 
def tuple_counter():
    global num_items
    num_items += 1
    return [num_items, ""]
 
d = defaultdict(tuple_counter)
 
d["pindaíba"][1] = "falta de dinheiro"
d["gororoba"][1] = "comida duvidosa"
d["bugiganga"][1] = "quinquilharia"
d["bizu"][1] = "ideia"
 
print(f'gororoba significa {d["gororoba"][1]}, e foi a {d["gororoba"][0]}ª palavra a ser adicionada neste dicionário.')