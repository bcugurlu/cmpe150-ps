# PS-5 Solutions

**Q1) Baseball**

```py
file = open("baseball.txt", "r")
lines = [line.rstrip() for line in file]
data = [l.split("; ") for l in lines]
for i in range(len(data)):
    for j in range(2, 9):
        data[i][j] = int(data[i][j])

    singles = data[i][5] - data[i][6] - data[i][7] - data[i][8]
    total_bases = singles + 2 * data[i][6] + 3 * data[i][7]

    if data[i][3] != 0:
        bat_avg = data[i][5] / data[i][3]
        slug_avg = total_bases / data[i][3]
    else:
        bat_avg = 0
        slug_avg = 0

    data[i].extend([singles, total_bases, bat_avg, slug_avg])

player_lst = [data[i][0] for i in range(len(data))]
hit_lst = [data[i][5] for i in range(len(data))]
bat_avg_lst = [data[i][11] for i in range(len(data))]
slug_avg_lst = [data[i][12] for i in range(len(data))]

def max_giver(op, n):
    if op == "MAX HITS":
        max_lst = hit_lst
    elif op == "MAX BATTING":
        max_lst = bat_avg_lst
    elif op == "MAX SLUGGING":
        max_lst = slug_avg_lst

    while n != 0:
        x = max_lst.index(max(max_lst))
        print(player_lst[x])
        del player_lst[x]
        del max_lst[x]
        n -= 1

max_giver(input(), int(input()))
```

**Q2) Movies**

```py
with open("mov_data.csv", "r") as f:
    lines = [l.rstrip() for l in f]
    mov_lst = [l.split(",") for l in lines]

mov_dict = {}

for i in range(len(mov_lst)):
    movie = mov_lst[i][1].split(" (")[0]
    year = mov_lst[i][1].split(" (")[1]
    single_mov_dict = {"movie": movie, "genre": mov_lst[i][2], "year": year.replace(")", "")}
    mov_dict[i+1] = single_mov_dict

request = input()

for j in range(1, len(mov_dict)+1):
    if mov_dict[j]["movie"] == request:
        print(mov_dict[j]["genre"])
        print(mov_dict[j]["year"])
```