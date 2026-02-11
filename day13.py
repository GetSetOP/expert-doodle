names = []
names_lower = set()

while True:
    name = input("Enter a Name(or type 'stop') ").strip()

    if name.lower().strip() == "stop":
        break
    
    if  name.strip() == "":
        print("Empty Name Ignored Succesfully.")
        continue

    if name.lower() in names_lower:
        print("Duplicate Name Ignored Succesfully!")
        continue
    
    names.append(name)
    names_lower.add(name.lower())

print("\nFinal List:")
print(names)
for name in names:
    print(f" {name} -> {len(name)}")
