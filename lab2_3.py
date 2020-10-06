ear=int(input('год: '))
if (ear%4==0) and (ear%100!=0) or (ear%400==0) and (ear%100==0):
    print ('будет')
else:
    print ('не будет')