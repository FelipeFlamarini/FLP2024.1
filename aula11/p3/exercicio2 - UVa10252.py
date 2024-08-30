from sys import stdin, stdout

lines_output = []

for line_i in stdin:
    line_j = stdin.readline()
        
    line_i = line_i.removesuffix("\n")
    line_j = line_j.removesuffix("\n")
    
    set_line_i = set(line_i)
    set_line_j = set(line_j)
    
    line_output = ""
    
    for character in set_line_i:
        if character in set_line_j:
            # a lógica de contagem não é necessária para os exemplos de input e output do exercício
            # mas existiriam problemas se a primeira palavra do par tiver x quantidade de caracteres y
            # e a segunda palavra do par tiver menos de x quantidade de caracteres y
            # não há nenhum par assim no input de exemplo
            # um par assim seria: "street", "the"
            # "street" vem primeiro e tem 2 "e" enquanto "the" tem 1 "e"
            count_line_i = line_i.count(character)
            count_line_j = line_j.count(character)
            count = count_line_i if count_line_i < count_line_j else count_line_j
            line_output += character*count
    
    lines_output.append("".join(sorted(line_output)))
    
for i in range(len(lines_output)):
    stdout.write(f"{lines_output[i]}{"" if i == (len(lines_output) - 1) else "\n"}")
