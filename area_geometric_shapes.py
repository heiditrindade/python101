valores = input()
vlist = (valores.split(' '))
triangulo = (float(vlist[0])*float(vlist[2]))/2
circulo = 3.14159*float(vlist[2])**2
trapezio = (float(vlist[0])+float(vlist[1]))/2 * float(vlist[2])
quadrado = float(vlist[1])*float(vlist[1])
retangulo = float(vlist[0])*float(vlist[1])

print(f'TRIANGULO: {triangulo:.3f}\n'
      f'CIRCULO: {circulo:.3f}\n'
      f'TRAPEZIO: {trapezio:.3f}\n'
      f'QUADRADO: {quadrado:.3f}\n'
      f'RETANGULO: {retangulo:.3f}')