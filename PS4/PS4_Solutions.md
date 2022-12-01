# PS-4 Solutions

**Q1) Guess the number!**

```py
import random

score = 0

for _ in range(10):

    g_num = int(input())
    num = random.randint(1, 10)

    if g_num is num:
        score += 10
        print("Well done! Please go to the next step.")

    elif (2 >= g_num - num >= -2) and (g_num != num):
        score += 3
        print("Close enough, go on with the next step.")

    else:
        print("Incorrect, go on with the next step.")

print(score)
```
**Q2) Remove A**

```py
lst = [int(x) for x in input().split()]
a = int(input())
new_lst = []

for x in lst:
    if x != a:
        new_lst.append(x)
print(new_lst)
```

**Q3) Duplicate elements**

**a)**
```py
lst = [int(x) for x in input().split()]
new_lst = []

for x in lst:
    if x not in new_lst:
        new_lst.append(x)

print(new_lst)
```

**b)**

```py
lst = [int(x) for x in input().split()]
new_lst = []
count_lst = []

for x in lst:
    if x not in new_lst:
        new_lst.append(x)
        count_lst.append(1)
    else:
        count_lst[new_lst.index(x)] += 1

for i in range(len(count_lst)):
    if count_lst[i] >= 3:
        print(new_lst[i], count_lst[i])
```

**Q4) Transpose of a Matrix**

```py
rows = int(input())
m = []
t_m = []

for r in range(rows):
    row_elements = []
    for x in input().split():
        row_elements.append(int(x))
    m.append(row_elements)

for i in range(len(m[0])):
    new_row = []
    for j in range(rows):
        new_row.append(m[j][i])
    t_m.append(new_row)
    
# You can also write the for loops above as follows:

# for r in range(rows):
#     row_elements = [int(x) for x in input().split()]
#     m.append(row_elements)

# for i in range(len(m[0])):
#     new_row = [m[j][i] for j in range(rows)]
#     t_m.append(new_row)

for r in range(len(t_m)):
    for c in range(len(t_m[0])):
        print(t_m[r][c], end=" ")
    print()
```

**Q5) Pascal's Triangle**

```py
def facto(x):
    prod = 1
    for i in range(2, x+1):
        prod *= i
    return prod

n = int(input())

for i in range(n):
    for _ in range(n-i-1):
        print(end=" ")
# C(a,b) = a! / b!(a-b)!
    for j in range(i+1):
        print(int(facto(i)/(facto(j)*facto(i-j))), end=" ")
    print()
```