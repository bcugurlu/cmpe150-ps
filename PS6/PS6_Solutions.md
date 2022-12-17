# PS-6 Solutions

**Q1) Sum of squares**

```py
n = int(input())
s = 0

while n > 0:
    s += n ** 2
    n -= 1

print(s)
```

**Q2) Prime factorization**

```py
n = int(input())

for i in range(2, n + 1):
    while n % i == 0:
        print(i, end=" ")
        n = n / i
```

**Q3) Least common multiple**

```py
a = int(input())
b = int(input())
c = a if a > b else b # takes the greater number as "c"

while True:
    if (c % a == 0) and (c % b == 0):
        lcm = c
        break
    c += 1

print(lcm)
```

**Q4) Greatest common divisor**

```py
a = int(input())
b = int(input())
c = a if a < b else b # takes the smaller number as "c"

while c > 0:
    if (a % c == 0) and (b % c == 0):
        gcd = c
        break
    c -= 1

print(gcd)
```

**Q5) Sum of digits**

```py
n = int(input())
s = 0

while n > 0:
    s += n % 10 # last digit
    n = (n - n % 10) / 10

print(int(s))
```

**Q6) Taylor series**

```py
def facto(i):
    f = 1
    while i > 0:
        f *= i
        i -= 1
    return f

x = int(input())
n = int(input())
t = 0

while n > -1:
    t += (x ** n) / facto(n)
    n -= 1

print(t**(1/x))
```