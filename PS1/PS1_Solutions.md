# PS-1 Solutions

**Q2) Area of a circle**

```
def area(r):
    A = pi*r**2
    print(A)

pi = 3.14
radius = int(input())
area(radius)
```

**Q3) Body-mass index**

```
def bmi(w, h):
    return w/(2.54*h/100)**2

weight = float(input())
height = float(input())
print("%.2f" % bmi(weight, height))
```

**Q4) Operations on a 2D-plane**

```
def slope(x1,x2,y1,y2):
    return (y2-y1)/(x2-x1)

def distance(x1,x2,y1,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

xa, ya = input().split(",")
xb, yb = input().split(",")
xa, ya, xb, yb = int(xa), int(ya), int(xb), int(yb)
print(slope(xa,xb,ya,yb))
print(distance(xa,xb,ya,yb))
```

**Q5) Ideal gas equation**

```
def cel_to_fah(c):
    return 1.8*c + 32

def cel_to_kel(c):
    return c + 273.15

def pressure_of_perfect_gas(n, T, V):
    return n*R*T/V

R = 0.08205
volume = int(input())
celcius = int(input())
amount = int(input())
print(cel_to_fah(celcius), "°F")
print(pressure_of_perfect_gas(amount, cel_to_kel(celcius), volume))
```
