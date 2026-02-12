names = []
name_data = {}

while True:
    name = input("Enter Name, (or 'stop' to Stop) ")

    if name.lower().strip() == "stop":
        break
    
    if name.strip() == "":
        print("Empty Space Ignored.")
        continue
    
    names.append(name)
    name_data[name] = len(name)

print("\nName Length(s):")
for name, length in name_data.items():
    print(f"{name} -> {length}")

print("Longest Name:", max(name_data, key=len))

print("Total Names:", names)
