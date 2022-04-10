hours = int(input())
average_speed = int(input())
liters_per_km = int(input())
dist = average_speed * hours

liters = dist/liters_per_km
print(f'{liters:.3f}')