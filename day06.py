TheLazzyBand = ("Kallu", "Motilal", "Nikhil", "DhinchakPooja")
count = 1
for name in TheLazzyBand:
    if len(name) <7:
        print(count, ".", name)
        count = count + 1
