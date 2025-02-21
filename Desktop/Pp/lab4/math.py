#task1
import math
def degtorad(deg):
    return deg*(math.pi/180)
deg = float(input())
print(degtorad(deg))

#task2
h = int(input("Height: "))
b1 = int(input("Base, first value: "))
b2 = int(input("Base, second value: "))
print("Expected Output: ", (b1+b2)*h/2)

#task3
import math

def degtorad(deg):
    return deg*(math.pi/180)

n = int(input("Input number of sides: "))
a = int(input("Input the length of a side: "))
apothem = a/(2*math.tan(degtorad(180/n)))
print("The area of the polygon is: ", n*a*apothem/2)

#task4
b = int(input("Lenght of base: "))
h = int(input("Height of the parallelogram: "))
print("Expected Output: ", b*h)
