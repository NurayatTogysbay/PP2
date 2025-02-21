#Tuples
mytuple = ("apple", "banana", "cherry")
#Acces Tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#Update Tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#Unpack Tuples
fruits = ("apple", "banana", "cherry")
#Loop Tuples
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#Join Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
