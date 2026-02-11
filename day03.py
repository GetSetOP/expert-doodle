#Tuples
mytuple = ("Jokes", 34, True)
yourtuple = tuple(("boss","Gang", 89, False))
print(mytuple)
print(yourtuple)
print(type(mytuple))
print(type(yourtuple))

newlist = list(mytuple)
newlist.append("BJP")
print(newlist)
newtuple = tuple(newlist)
print(newtuple)
#The Astrick in Front of Two Makes it Print Till Second Last Data
(one, *two, hey) = yourtuple
print(one)
print(two)
print(hey)
#Counting How Many Data (2) Are in Tuple
print(yourtuple.count(2))

#Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}
band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

#Access items
print(band["vocals"])
print(band.get("guitar"))

#List all keys
print(band.keys())

#List all values
print(band.values())

#List of Key/Values pairs as Tuples
print(band.items())

#Verifying Data Availibility
print("guitar" in band)
print("Ramu" in band)

#Changing and Pairing Values
band["vocals"] = "Coverdale"
band.update({"bass" : "FFd"})
print(band)

#Remove Items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())
print(band)

#Delete and Clear

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

#Copy Dictionaries
