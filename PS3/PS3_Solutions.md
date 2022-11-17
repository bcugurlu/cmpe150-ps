# PS-3 Solutions

**Q1) Factorial**

```py
x = int(input())
prod = 1

for i in range(1, x + 1):
    prod *= i

print(prod)
```

**Q2) Largest number**


```py
max_num = 0

for _ in range(5):
    x = int(input())
    if x > max_num:
        max_num = x

print(max_num)
```

**Q3) Hooping numbers**

```py
initial = int(input())
final = int(input())
change = int(input())

for i in range(initial, final + 1, change):
    print(i, end=" ")
```

**Q4) Logistics**

```py
n = int(input())
minibus = 0
truck = 0
train = 0
total_w = 0
price = 0

for i in range(n):
    w = int(input())
    total_w += w
    if w > 11:
        train += w
        price += w*120
    elif w <= 3:
        minibus += w
        price += w*200
    else:
        truck += w
        price += w*175

print("%.2f" % (price/total_w))
print("%.2f" % (100*minibus/total_w))
print("%.2f" % (100*truck/total_w))
print("%.2f" % (100*train/total_w))
```

**Q5) Multiplication table**

```py
for i in range(1, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print()
```
**Q6) Rectangles**

**a)** 
```py
row = int(input())
column = int(input())

for i in range(row):
    for j in range(column):
        print("o", end="")
    print()
```
**b)**
```py
row = int(input())
column = int(input())

for _ in range(column):
    print("o", end="")
print()

for _ in range(row-2):
    print("o", end="")
    for _ in range(column-2):
        print("_", end="")
    print("o")

for _ in range(column):
    print("o", end="")
```

**Q7) Powers**

```py
num = int(input())
power = int(input())

for i in range(1, power+1):
    for j in range(1, i+1):
        print(num**j, end=" ")
    print()
```