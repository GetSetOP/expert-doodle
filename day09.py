names = ("Kallu", "MausiOfKallu", "NosterBhai", "Gauster", "PrismBanker")
for name in names:
    print(names)

def show_long_names(names):
    for name in names:
        if len(name) > 6:
            print(name)
print(show_long_names)    
