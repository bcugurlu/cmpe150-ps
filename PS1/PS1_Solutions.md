# PS-1 Solutions

```py
metamorphosis = open("samsa.txt", "x") 

paragraph = open("samsa.txt", "w") 
paragraph.write("As Gregor Samsa awoke one morning from uneasy dreams he found himself transformed in his bed into a gigantic insect. \nHe was lying on his hard, as it were armor-plated, \nback and when he lifted his head a little he could see his dome-like brown belly divided into stiffarched segments \non top of which the bed quilt could hardly keep in position and was about to slide off completely. \nHis numerous legs, which were pitifully thin compared to the rest of his bulk, waved helplessly before his eyes.")
paragraph.close()

paragraph = open("samsa.txt", "r") 
print(paragraph.read()) 
paragraph.close() 

paragraph = open("samsa.txt", "r") 
print(paragraph.readline()) 
print(paragraph.readline()) 
paragraph.close() 

paragraph = open("samsa.txt", "a") 
paragraph.write("\n------- END OF THE PARAGRAPH -------") 
paragraph.close() 

paragraph = open("samsa.txt", "r") 
print(paragraph.read()) 
paragraph.close()
```

**Q2) Area of a circle**

```py
def area(r):
    A = pi*r**2
    print(A)

pi = 3.14
radius = int(input())
area(radius)
```

**Q3) Body-mass index**

```py
def bmi(w, h):
    return w/(2.54*h/100)**2

weight = float(input())
height = float(input())
print("%.2f" % bmi(weight, height))
```

**Q4) Operations on a 2D-plane**

```py
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

```py
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
