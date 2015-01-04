members, topics = [int(x) for x in input().split(" ")]

team = []
for i in range(members):
    team.append(input())

h = {}
for i in range(members):
    for j in range(i + 1, members):
        no = int(team[i], 2) | int(team[j], 2)
        no = str(bin(no)[2:])
        h.setdefault(no.count("1"), 0)
        h[no.count("1")] += 1

m = max(h.keys())
print(m)
print(h[m])

        


