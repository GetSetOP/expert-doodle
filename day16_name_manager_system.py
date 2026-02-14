                                                  # Base Structure
names = []

def add_name():
    name = input("Enter Name: ").strip()
    if name:
        names.append(name)
        print("Added.")
    else:
        print("Invalid Input.")

def show_names():
    if not names:
        print("No Names Yet.")
    else:
        for i, name in enumerate(names, 1):
            print(f" {i}. {name}")

def search_names():
    letter = input("Enter Starting Letter: ").strip().lower()
    matches = [name for name in names if name.lower().startswith(letter)]

    if matches:
        print("Matches:")
        for name in matches:
            print(name)
        print("Total:", len(matches))
    else:
        print("No Matches Found.")

def delete_name():
    if not names:
        print("No Names To Delete.")
        return
    print("\nNames:")
    for i, name in enumerate(names, 1):
        print(f" {i}. {name}")
    try:
        choice = int(input("Enter Number To Delete: "))
        
        if 1 <= choice <= len(names):
                selected_name = names[choice -1]
                confirm = input(f"Are You Sure You Want To Delete {selected_name}? (y/n):  ").strip().lower()
                if confirm == "y":
                    removed = names.pop(choice - 1)
                    print(f"Deleted: {removed}")
                else:
                    print("Deletion Cancelled.")
        else:
            print("Invalid Number.")
        print(f"Total Names Left: {len(names)}")
    except ValueError:
        print("Please Enter a Valid Number.")
    
                                                  # Menu Loop
while True:
    print("\n                           --- Name Manager ---                         ")
    print("1. Add Name")
    print("2. Show Names")
    print("3. Search")
    print("4. Delete Name")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_name()
    elif choice =="2":
        show_names()
    elif choice == "3":
        search_names()
    elif choice == "4":
        delete_name()
    elif choice == "5":
        break
    else:
        print("Invalid Choice.")
