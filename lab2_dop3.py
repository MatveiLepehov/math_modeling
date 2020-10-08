a = int(input(':Число='))
G = 0

while a>0:
    G = G*10 + a%10
    a = a//10
print(G)