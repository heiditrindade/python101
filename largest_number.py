values = input()
vlist = values.split(' ')
largest_ab = (int(vlist[0])+int(vlist[1])+abs(int(vlist[0])-int(vlist[1])))/2
largest_total = (int(largest_ab)+int(vlist[2])+abs(int(largest_ab)-int(vlist[2])))/2
print(f'{int(largest_total)} is the largest number')