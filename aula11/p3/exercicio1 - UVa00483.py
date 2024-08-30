from sys import stdin, stdout

lines_output = []

for line in stdin:
    count = 0
    word_output = []
    for word in line.split(): # split tira "\n"
        word_output.append(word[::-1])
    lines_output.append(" ".join(word_output))
    
for i in range(len(lines_output)):
    stdout.write(f"{lines_output[i]}{"" if i == (len(lines_output) - 1) else "\n"}")
