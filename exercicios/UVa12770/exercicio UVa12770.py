from sys import stdin, stdout

word = stdin.readline().strip()
while word != "#":
    str_out = ""
        
    if len(word) >= 3:
        char_count = set(word)
        uneven_chars = set()
        for char in char_count:
            if word.count(char) % 2 != 0:
                uneven_chars.add(char)
                
        while len(uneven_chars) > 1:
            character_min = min(uneven_chars)
            str_out += character_min
            uneven_chars.remove(character_min)

    stdout.write(f"{str_out}\n")
    word = stdin.readline().strip()