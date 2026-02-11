TheLazzyBand = ("Kallu", "MausiOfKallu", "NosterBhai", "Gauster", "PrismBanker")
count = 1
for name in TheLazzyBand:
    if len (name) < 7:
        firstletter = name[0]
        print(count, ".", name, firstletter)
        count = count + 1
