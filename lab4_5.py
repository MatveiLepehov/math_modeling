import numpy as np
index = int(input('введите номер фигуры (круг - 0, прямоугольник - 1, треугольник - 2. ): '))
def mult_func(index=0):
    if index==0:
        r= float(input('радиус = '))
        s=np.pi*r**2
        print('Площадь круга =', s)
    elif index==1:
        a= float(input('длина = '))
        b= float(input('ширина = '))
        s=a*b
        print('Площадь прямоугольника =', s)
    elif index==2:
        a= float(input('сторона треугольника = '))
        h= float(input('высота ='))
        s=0.5*(a*h)
        print('Площадь треугольника =', s)
    else:
        print('ты ошибся')
        
mult_func(index)