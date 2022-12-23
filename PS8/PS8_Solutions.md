# PS-8 Solutions

**Q1) Border crossing**

```py
with open("border_crossing_entry.csv") as f:
    d = [l.rstrip().split(",") for l in f]

border = []
year = []
method = []
entry = {}

for i in range(len(d)):
    border.append(d[i][3]) if d[i][3] not in border else None
    year.append(d[i][4]) if d[i][4] not in year else None
    method.append(d[i][5]) if d[i][5] not in method else None

for y in year:
    entry[y] = {}
    for b in border:
        entry[y][b] = {}
        for m in method:
            entry[y][b][m] = []
            for i in range(len(d)):
                entry[y][b][m].append(int(d[i][6])) if d[i][3] == b and d[i][4] == y and d[i][5] == m else None

y_req = input()
b_req = input()
m_req = input()
s = 0

for x in entry[y_req][b_req][m_req]:
    s += x

print(s)
```

**Q2) Grade analysis**

```py
def median(lst):
    lst = [int(x) for x in lst]
    lst.sort()
    mid = len(lst) // 2
    if len(lst) % 2 == 0:
        return (lst[mid] + lst[mid - 1]) / 2
    else:
        return lst[mid]

def avg(lst):
    lst = [int(x) for x in lst]
    tot = 0
    for a in lst:
        tot += a
    return tot / len(lst)

with open("grades.txt") as f:
    d = [l.rstrip().split(",") for l in f]

group = [d[i][0] for i in range(len(d))]
data = {}

for i in range(len(group)):
    subj = []
    grades = []
    for j in range(1, len(d[i])):
        if not d[i][j].isnumeric():
            subj.append(d[i][j])
        else:
            grades.append(d[i][j])
    stud = len(grades)
    data[group[i]] = {}
    for s in subj:
        data[group[i]][s] = grades[:stud//len(subj)]
        del grades[:stud//len(subj)]

g_req, s_req, op = input().split()

if op == "average":
    print(avg(data[g_req][s_req]))
elif op == "median":
    print(median(data[g_req][s_req]))
```

**Q3) Pant style pattern**

```py
n = int(input())
i = (n // 2)
j = 0
while i != 0:
    print("*" * i, end="")
    print(" " * j, end="")
    print("*" * i, end="\n")
    i -= 1
    j += 2
```