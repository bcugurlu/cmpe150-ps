# PS-7 Solutions

**Q1) Inverted dictionary**

```py
def invert_dict(d):
    i_d = {}
    for k, v in d.items():
        i_d[v] = k
    return i_d

```

**Q2) Data collection**

```py
d = {}

while True:
    a = input()
    if a == "exit":
        break
    d[a.split()[0]] = {"genre": a.split()[1], "release date": a.split()[2], "producer": a.split()[3]}

print(d)
```

**Q3) Order filler**

```py
s = {"socks": 14, "pants": 6, "shoes": 7}

while True:
    req = input()
    if req == "exit":
        break
    if s[req.split()[0]] >= int(req.split()[1]):
        print("successful")
        s[req.split()[0]] -= int(req.split()[1])
    else:
        print("unsuccessful")

for k, v in s.items():
    print(k, v)
```