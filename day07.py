TheLazzyBand = ("Jaqline", "Ferera", "Tyson", "Sharma")
count = 1
for name in TheLazzyBand:
    if len(name) < 7:
        firstletter = name[0]
        print(f"{count}. {name} {firstletter}")
        count = count + 1
