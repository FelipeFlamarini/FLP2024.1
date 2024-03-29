random_keys = {}
random_keys["astring"] = "somestring"
random_keys[5] = "aninteger"
random_keys[25.2] = "floats work too"
random_keys[("abc", 123)] = "so do tuples"
 
class AnObject:
    def __init__(self, avalue):
        self.avalue = avalue
 
my_object = AnObject(14)
random_keys[my_object] = "We can even store objects"
my_object.avalue = 12
 
try:
    random_keys[[1, 2, 3]] = "we can't store lists though"
except:
    print("unable to store list\n")
 
for key, value in random_keys.items():
    print(f"{key} has value {value}")

# print()
# print(random_keys[("abc", 123)])

print()
print(my_object.__dict__)

print()
print(my_object.avalue)
try:
    print(my_object["avalue"])
except:
    print("unable to access my_object as a dictionary\n")