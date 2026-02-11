names = ("Kallu", "MausiOfKallu", "NosterBhai", "Gauster", "PrismBanker")
count = 1
for name in names: 
    if len(name) >6:
        print(f"{count}. {name} {name[0]} {name[-1]} ")
        count +=1
