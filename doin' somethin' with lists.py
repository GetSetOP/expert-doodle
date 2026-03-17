print("doin' somethin' with lists")

list0 = ["Etter", "XMaterrz", "LowwIgh", "KnockoutBoss"]

def search():
    a = input("Search with the first letter of name: ").lower()
    found = False

    for name in list0:
        if name.lower().startswith(a):
            print(name)
            found = True

    if not found:
        print("No Name Found with that starting letter.")

def see_all_names():
    print("\nAll names:")
    for name in list0:
        print(name)

def exiting():
    c = input("Are you sure you want to exit? (y/n): ").lower()
    if c == "y":
        print("Goodbye!")
        exit()

def add_name():
    new_name = input("What Name Would You Like To Add? ")
    list0.append(new_name)
    print(f"{new_name} added.")

def delete_name():
    if not list0:
        print("No names to delete.")
        return
    print("\nNames:")
    for i, name in enumerate(list0, 1):
        print(f" {i}. {name}")
    try:
        choice = int(input("Enter number beside the name to delete it: "))

        if 1 <= choice <= len(list0):
            selected_name = list0[choice-1]
            confirm = input(f"Are you sure you want to delete {selected_name}? (y/n): ").lower().strip()
            if confirm == "y":
                removed = list0.pop(choice - 1)
                print(f"Deleted {removed}")
            else:
                print("Deletion Cancelled")
        else:
            print("Invalid Number")
        print(f"Total Names Left, {len(list0)}")
    except ValueError:
        print("Please Enter a Valid Number")

while True:
    print("\nPress 1 to search")
    print("Press 2 to see all names")
    print("Press 3 to add a new name")
    print("Press 4 to delete a name")
    print("Press 5 to exit")

    Avariable = input("Choose: ")

    if Avariable == "1":
        search()
    elif Avariable == "2":
        see_all_names()
    elif Avariable == "3":
        add_name()
    elif Avariable == "4":
        delete_name()
    elif Avariable == "5":
        exiting()
    else:
        print("Invalid option.")
