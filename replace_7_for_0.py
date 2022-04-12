entrada = input().replace('7', '0').split()
a, s, b = int(entrada[0]), entrada[1], int(entrada[2])

resultado = 0

if s == '+':
  resultado = a + b
else:
  resultado = a * b

resultado = int(str(resultado).replace('7', '0'))

print(resultado)