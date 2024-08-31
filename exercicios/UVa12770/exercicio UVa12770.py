from sys import stdin, stdout

word = stdin.readline().strip()
while word != "#":
    str_out = ""
        
    char_count = {}
    
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        
    uneven_chars = [char for char, count in char_count.items() if count % 2 != 0]
            
    while len(uneven_chars) > 1:
        character_min = min(uneven_chars)
        str_out += character_min
        uneven_chars.remove(character_min)

    stdout.write(f"{str_out}\n")
    word = stdin.readline().strip()