users = ["abhi", "proteas", "kiwis"]
data = ["abhi", "proteas", "kiwis", 32, True]
emptylist = [ ]
print("abhi" in users)
print("abhi" in emptylist)
print(users[0])
#Counts from end in negative
print(users[-2])
#If to show the Position of Data
print(users.index("abhi"))
#To Print Numbers from a Fixed to a Fixed
print(users[0:3])
#If we Leave the Other :example blank it would print till last
print(users[0:])
#it could also accept negatives
print(users[-3:-1])
#Return the amount of data in a list
print(len(data))
#If we Have to Add Something to the List
users.append("Robin")
print(users)
#Another Method
users += ["Jason"]
print(users)
#Another Method
users.extend(["Robert", "Jimmy"])
print(users)
#Inserting Your Data to Your Favouraite Position
users.insert(0, "Bob")
print(users)
#if inserting 2 or more
users[2:2] = ["Eddie","Alex"]
print(users)
#Inserting and Replacing
users[1:3] = ["Koala","Texin"]
print(users)
#If Have to Remove Specific Data
users.remove("Bob")
print(users)
#Removing the Last Data
print(users.pop())
print(users)
#Removing by Positions
del users[0]
print(users)
#Clears Data But The List Still Exists
data.clear()
print(data)
#To Get It Sorted in Alphabetical Order
users.sort()
print(users)
#Same but for Lowercase Also Can Use Capital
users.sort(key=str.lower)
print(users)
#Counts From End or Reverses The Integers
nums = [2, 34, 56, 67]
nums.reverse()
print(nums)
#Sorting Numbers in Descending Order
nums.sort(reverse=True)
print(nums)
#Making Copies of Lists Various Methods
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[0:]
#(All Do The Same Work)
print(numscopy)
print(mynums)
print(mycopy)
mycopy.sort()
#Classifying a Data Type
print(type(nums))
#If To Make a List Contain More Than One Data Type
mylist = list([1, "Neil", True])
print(mylist)

#Tuples
