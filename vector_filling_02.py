t = int(input())

i = 0

while i < 1001:
  for n in range(0,t):
    print(f'N[{i}] = {n}')
    i += 1
    if i >= 1000:
      break