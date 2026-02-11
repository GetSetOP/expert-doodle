#Lists
names = ["DonnyDon", "BoggyBog"]
names.append("JackieJack")
print(names)

#Tuple
names2 = ("LoggieLog", "MoggieMog")
names2 = names2 + ("GoggyGog",)#The Comma (,) Is Very Important
print(names2)

#Dictionaries
names ={"ChannieChan" : 67}
names["NommieNom"] = 2
print(names)

#Project 1 Understanding Immutabillity and Iteration
TheLazzyBand = ("Namrit", "Parvati", "Prakritik", "Chinnulaal", "RajKarthik")
count = 1
for name in TheLazzyBand:
    if len(name) > 7:
        print(count, ".", name)
        count = count + 1
