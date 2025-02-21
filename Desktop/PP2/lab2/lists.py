#Lists
thislist = ["apple", "banana", "cherry"]
print(thislist)
#Acces List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#Change List Items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#Add List Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#Remove List Items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#Loop List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#Sort List
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#Copy List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#Join Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
