# ejercicio 10
c = str(input("cadena : "))
cont = 0
for a in c:
    if a == 'a':
        cont += 1
    elif a == 'e':
        cont += 1
    elif a == 'i':
        cont += 1
    elif a == 'o':
        cont += 1
    elif a == 'u':
        cont += 1

print(cont)

#ejercicio 04
min = int(input('minimo: '))
max = int(input('maximo: '))
sum=0
print('numeros : ', end = '')
for i in range(min,max+1):
    if i%7==0:
        print(i,end=' ')
        sum += i
    elif i%5 == 0:
        print(i, end=' ')
        sum+= i

print(' ')
print('suma :',sum)