names = "Freddy", "Mysticore", "Windler", "Majem", "Saguna", "Broklly"
def get_long_names(names, min_length):
    long_names = []

    for name in names:
        if len(name) > min_length:
            long_names.append(name)

    return long_names

def get_short_names(names, max_length):
    short_names = []

    for name in names:
        if len(name) <= max_length:
            short_names.append(name)

    return short_names

def show_name_details(names):
    for name in names:
        print(f"{name} -> First Name ->{name[0]}, Last Name ->{name[-1].upper()}, Length of Name ->{len(name)} Characters")

print("Total Names:", len(names))
long_names = get_long_names(names, 6)
print("\nLong Names:")
show_name_details(long_names)

short_names = get_short_names(names, 6)
print("\nShort Names:")
show_name_details(short_names)
