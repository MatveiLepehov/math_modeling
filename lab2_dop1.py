a= float(input('введите число :а= '))
b= float(input('введите число :b= '))
c= float(input('введите число :c= '))
D= ((b**2)-4*a*c)
print (D)
if D > 0 and a != 0:
    x1=(-b+ (D**0.5))/ (2*a)
    x2=(-b- (D**0.5))/ (2*a)
elif D == 0:
    x= -b/(2*a)
    print (x)
else:
    print ('корней нет')
    