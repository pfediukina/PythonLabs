a_set = set([1, 2, 3, 4 ,5, 6, 7])
a_set.update([8])
a_set.remove(2)

it_ob = [1, 2, 3]

from collections.abc import Hashable, Iterable, Collection, Sequence, Set, MutableSet

print(isinstance (it_ob, Iterable))

for item in it_ob:
    print(f'Объект: {item} Хешируемый: {isinstance (it_ob, Iterable)}')
    
b_set = set(it_ob)
print(f'\nb_set: {b_set}\na_set: {a_set}')
c_set = a_set.symmetric_difference(b_set)
print(f'symmetric_difference: {a_set.symmetric_difference(b_set)}')

# 5 – генератора
a_dict = {x:x**(1/2) for x in [2, 5, 25] }
print(f'\n\ndict: {a_dict}')
print(f'\nkeys()^\n {a_dict.keys()}' )
print(f'\npop()^\n  {a_dict.pop(2)}' )
print(f'\nvalues()^\n {a_dict.keys()}')
print()