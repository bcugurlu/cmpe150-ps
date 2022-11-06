"""Write a function that calculates the area of a circle and prints the output (π = 3.14)."""

def area(r):
    A = pi*r**2
    print(A)

pi = 3.14
radius = int(input())
area(radius)