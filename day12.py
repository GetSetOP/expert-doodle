name = input("Hi! May I Know Your Name: ")

if name.strip() =="":
    print("Umm... Being Smart? You Pressed Enter, But Why?")
else:
    print("Welcome", name)
    print("First Letter:", name[0])
    print("Last Letter:", name[-1].upper())
    print("Length:", len(name))

    if len(name) >6:
        print("Cool Guys Have LONG Name!")

    elif len(name) <=6:
        print("short Names Are Not as Cool as LONG Ones!")
