#List Of Names
names = ("Kallu", "MausiOfKallu", "NosterBhai", "Gauster", "PrismBanker")
#Defines The Long Names
def get_long_names(names, min_length):
    long_names = []
#Sorts The Names
    for name in names:
        if len(name) > min_length:
            long_names.append(name)
#Returns the Names
    return long_names
#Stores The Result
result = get_long_names(names, 6)
#Prints Nicely
for name in result:
    print(name)

result2 = get_long_names(names, 10)
print(result2)
