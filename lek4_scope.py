x0=12 #глобальная перемена
def move(t):
  x=x0*t #локальная переменная
  return x
print (move(123))
x='good'
def my_func():
  x='bad'
  print(x)
my_func()
print(x)