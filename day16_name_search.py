names = ("David", "Micheal", "Sweetie", "Katty", "Grouse", "Robin", "Jason", "Lionel")
letter = input("Enter Starting Letter: ").strip().lower()

print("\nMatching Names: ")
count = 0
for name in names:
    if name.lower().startswith(letter):
        count +=1
        print(name)
        print("Total Matches:", count, "out of", len(names)," ")
if count == 0:
    print("No Names Found")

