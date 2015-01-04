jars, opts = [int(x) for x in input().split()]
total = 0
for i in range(opts):
    st, ed, k = [int(x) for x in input().split()]
    total += (ed - st + 1) * k

print(int(total/jars))
