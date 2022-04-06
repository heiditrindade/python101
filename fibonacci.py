n = int(input())

l = [0,1]

while len(l) < n:
  prox = l[-1]+l[-2]
  l.append(prox)

print(*l)