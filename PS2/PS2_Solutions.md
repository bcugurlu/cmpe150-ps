# PS-2 Solutions

**Q1) Simple calculator**

```py
a = int(input())
b = int(input())
op = input()

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    print(a/b)
```

**Q2) Letter grade calculator**

```py
def letter_grade_generator(m1, m2, proj, hw, cw, q, f):
    score = 0.15 * m1 + 0.2 * m2 + 0.08 * proj + 0.06 * hw + 0.06 * cw + 0.1 * q + 0.35 * f
    if attendance / 28 >= 0.8:
        score += 2
    print(score)
    if score >= 85:
        return "A"
    elif 65 <= score < 85:
        return "B"
    elif 40 <= score < 65:
        return "C"
    elif 20 <= score < 40:
        return "D"
    else:
        return "F"


mt1 = int(input())
mt2 = int(input())
project = int(input())
homework = int(input())
classwork = int(input())
quiz = int(input())
final = int(input())
attendance = int(input())
print(letter_grade_generator(mt1, mt2, project, homework, classwork, quiz, final))
```

**Q3) Simple ATM**

```py
balance = 45178
withdrawal_limit = 5000
true_pin = 5713
pin = int(input("Welcome! Please enter your PIN: "))

if pin != true_pin:
    "Incorrect PIN, goodbye!"
else:
    print("Please select an operation: \n1. View account balance "
                   "\n2. Cash withdrawal \n3. Cash deposit")
    op = int(input())
    if op == 1:
        print(balance)
    elif op == 2:
        wd_request = int(input("Withdrawal request: "))
        if wd_request > 5000:
            print("Your withdrawal request is higher than the withdrawal limit. Goodbye!")
        else:
            print(balance-wd_request, "TRY")
    elif op == 3:
        dep_request = int(input("Deposit request: "))
        if dep_request <= balance:
            print(balance + dep_request, "TRY")
        else:
            print("Your deposit request is higher than your balance. Goodbye!")
    else:
        print("Invalid operation request, goodbye!")
```

**Q4) Sum of odd numbers**

```py
sum = 0

for i in range(5):
    x = int(input())
    if x % 2 == 1:
        sum += x

print(sum)
```

**Q5) Prime or not**

```py
num = int(input())
prime = True

for i in range(2, num):
    if num%i == 0:
        prime = False

if prime:
    print("Prime")
else:
    print("Not prime")
```

**Q6) Multiplies of 3 or 5**

```py
sum = 0
limit = int(input())

for i in range(limit):
    if (i % 5 == 0 or i % 3 == 0) and (i % 15 != 0):
        sum += i

print(sum)
```