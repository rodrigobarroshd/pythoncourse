"""""
Listas em Python 
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range


"""""

#         0    1         2    3    4
lista = ['A', 'Banana', 'C', 'D', 'E']
#    -    5    4         3    2    1

print(lista[1])
print(lista[-1])
print(lista[-3])

print(lista[0:3])
print(lista[::2])

print('#####################################################################')

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2
print(l1)
print(l2)
print(l3)

print('#####################################################################')


l4 = [1,2,3,4,5,6,7,8,9]
l4.insert(0, 'banana')
print(l4)
del(l4[0])
print(l4)