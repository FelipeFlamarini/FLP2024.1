from collections import Counter

def letter_frequency(sentence):
    return Counter(sentence)

print(letter_frequency("banana"))
print()

responses = [
    "vanilla",
    "chocolate",
    "vanilla",
    "vanilla",
    "caramel",
    "chocolate",
    "strawberry",
    "vanilla",
]
 
print("The children voted for", Counter(responses).most_common(1)[0][0], "ice cream")
