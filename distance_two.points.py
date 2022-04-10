import math
a, b = map(float, input().split())
c, d = map(float, input().split())
dist_two = math.sqrt(((a-c)**2)+((b-d)**2))

print(f'{(dist_two):.4f}')