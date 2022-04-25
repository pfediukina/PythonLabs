import collections
import random

a_tuple = 7.12, list([3, 'Lina']), 'Hello', True

for i in a_tuple:
    if isinstance(i, collections.abc.Container):
        print("Объект пренадлежит к ABC-классу Container")
    if isinstance(i, collections.abc.Iterator):
        print("Объект пренадлежит к ABC-классу Iterator")    
    if isinstance(i, collections.abc.Iterable):
        print("Объект пренадлежит к ABC-классу Iterable")
    if isinstance(i, collections.abc.Sequence):
        print("Объект пренадлежит к ABC-классу Sequence")
    if isinstance(i, collections.abc.MutableSequence):
        print("Объект пренадлежит к ABC-классу MutableSequence")

print('\nЭлемент кортежа в список:')
        
a_list = list(a_tuple[2])
for i in a_list:
    print(i)

print('\nСписок в кортеж')

b_tuple = tuple(a_list)
for i in b_tuple:
    print(i)
                  
a_range = [random.randrange(11), random.randrange(11)]
print(a_range)


a_byte = bytearray ( 'kick' , 'utf-8' )
print(a_byte.decode())
a_byte = a_byte.capitalize()
print(a_byte.decode())
