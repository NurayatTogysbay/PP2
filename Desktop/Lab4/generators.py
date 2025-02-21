#task1
def gen(N):
    for i in range(1, N+1):
        yield(i*i)
N = int(input())
for i in gen(N):
    print(i)

#task2
def gen(n):
    for i in range(0, n+1, 2):
        yield i

n = int(input())
for i in gen(n):
    print(i, end=",")

#task3
def gen(n):
    for i in range(0, n+1):
        if i%12 == 0:
            yield i
n = int(input())
for i in gen(n):
    print(i, end=" ")

#task4
def squares(a, b):
    for i in range(a, b+1):
        yield i*i
a = int(input())
b = int(input())
for i in squares(a, b):
    print(i)

#task5
def gen(n):
    for i in range(n, -1, -1):
        yield i
n = int(input())
for i in gen(n):
    print(i)
