salario_hora = float(input('Quanto você ganha por hora? '))
horas = int(input('Número de horas trabalhadas no mês: '))

bruto = salario_hora*horas
ir = bruto*0.11
inss = bruto*0.08
sindicato = bruto*0.05
liquido = bruto - ir - inss - sindicato

print(f'+ Salário Bruto: R${bruto}\n'
      f'- IR (11%): R${ir}\n'
      f'- INSS (8%): R${inss}\n'
      f'- Sindicato (5%): R${sindicato}\n'
      f'= Salário Líquido: R${liquido}')