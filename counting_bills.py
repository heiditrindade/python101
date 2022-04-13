value = int(input())
n_100 = value//100
n_50 = (value-(n_100*100))//50
n_20 = (value-(n_100*100)-(n_50*50))//20
n_10 = (value-(n_100*100)-(n_50*50)-(n_20*20))//10
n_5 = (value-(n_100*100)-(n_50*50)-(n_20*20)-(n_10*10))//5
n_2 = (value-(n_100*100)-(n_50*50)-(n_20*20)-(n_10*10)-(n_5*5))//2
n_1 = (value-(n_100*100)-(n_50*50)-(n_20*20)-(n_10*10)-(n_5*5)-(n_2*2))//1

print(f'{value}\n'
      f'{n_100} nota(s) de R$ 100,00\n'
      f'{n_50} nota(s) de R$ 50,00\n'
      f'{n_20} nota(s) de R$ 20,00\n'
      f'{n_10} nota(s) de R$ 10,00\n'
      f'{n_5} nota(s) de R$ 5,00\n'
      f'{n_2} nota(s) de R$ 2,00\n'
      f'{n_1} nota(s) de R$ 1,00')