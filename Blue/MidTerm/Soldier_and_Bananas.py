k, n, w = map(int, input().split())
cost = 0

for i in range(w):
    cost += k * (i+1)

if cost > n:
    print(cost - n)
else:
    print(0)