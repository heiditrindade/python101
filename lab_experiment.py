ncases = int(input())
cases_f = []
cases_m = []
cases_r = []

for n in range(ncases):
  test_case = input().split(' ')
  if test_case[1] == 'F':
    cases_f.append(int(test_case[0]))
  elif test_case[1] == 'M':
    cases_m.append(int(test_case[0]))
  elif test_case[1] == 'R':
    cases_r.append(int(test_case[0]))

total = sum(cases_f)+sum(cases_m)+sum(cases_r)
p_rabbits = (sum(cases_r)*100)/total
p_mice = (sum(cases_m)*100)/total
p_frogs = (sum(cases_f)*100)/total

print(f'Total: {total} subjects'
      f'\nTotal of rabbits: {sum(cases_r)}'
      f'\nTotal of mice: {sum(cases_m)}'
      f'\nTotal of frogs: {sum(cases_f)}'
      f'\nPercentage of rabbits: {p_rabbits:.2f} %'
      f'\nPercentage of mice: {p_mice:.2f} %'
      f'\nPercentage of frogs: {p_frogs:.2f} %')