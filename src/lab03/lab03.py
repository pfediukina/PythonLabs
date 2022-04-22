import collections

a_list = [13, 5.78, 'James', ['a', 'b', 'c'], False]

for i in a_list:
    print(f'Тип: {type(i)} Значение: {i}')

    if isinstance(i, collections.abc.Container):
        print("Объект пренадлежит к ABC-классу Container")
    elif isinstance(i, collections.abc.Hashable):
        print("Объект пренадлежит к ABC-классу Hashable")
    elif isinstance(i, collections.abc.Iterable):
        print("Объект пренадлежит к ABC-классу Iterable")
    elif isinstance(i, collections.abc.Iterator):
        print("Объект пренадлежит к ABC-классу Iterator")
    elif isinstance(i, collections.abc.Reversible):
        print("Объект пренадлежит к ABC-классу Reversible")
    elif isinstance(i, collections.abc.Generator):
        print("Объект пренадлежит к ABC-классу Generator")
    elif isinstance(i, collections.abc.Sized):
        print("Объект пренадлежит к ABC-классу Sized")
    elif isinstance(i, collections.abc.Callable):
        print("Объект пренадлежит к ABC-классу Callable")
    elif isinstance(i, collections.abc.Collection):
        print("Объект пренадлежит к ABC-классу Collection")
    elif isinstance(i, collections.abc.Sequence):
        print("Объект пренадлежит к ABC-классу Sequence")
    elif isinstance(i, collections.abc.MutableSequence):
        print("Объект пренадлежит к ABC-классу MutableSequence")
    elif isinstance(i, collections.abc.Set):
        print("Объект пренадлежит к ABC-классу Set")
    elif isinstance(i, collections.abc.MutableSet):
        print("Объект пренадлежит к ABC-классу MutableSet")
    elif isinstance(i, collections.abc.Mapping):
        print("Объект пренадлежит к ABC-классу Mapping")
    elif isinstance(i, collections.abc.MutableMapping):
        print("Объект пренадлежит к ABC-классу MutableMapping")
    elif isinstance(i, collections.abc.MappingView):
        print("Объект пренадлежит к ABC-классу MappingView")
    elif isinstance(i, collections.abc.ItemsView):
        print("Объект пренадлежит к ABC-классу ItemsView")
    elif isinstance(i, collections.abc.Awaitable):
        print("Объект пренадлежит к ABC-классу Awaitable")
    elif isinstance(i, collections.abc.Awaitable):
        print("Объект пренадлежит к ABC-классу Awaitable")
    elif isinstance(i, collections.abc.Coroutine):
        print("Объект пренадлежит к ABC-классу Coroutine")
    elif isinstance(i, collections.abc.AsyncIterable):
        print("Объект пренадлежит к ABC-классу AsyncIterable")
    elif isinstance(i, collections.abc.AsyncIterator):
        print("Объект пренадлежит к ABC-классу AsyncIterator")
    elif isinstance(i, collections.abc.AsyncGenerator):
        print("Объект пренадлежит к ABC-классу AsyncGenerator")
print()

a_list.insert(1, 43)
a_list.reverse()
a_list = a_list[2:5]

print()
for i in range(len(a_list)):
    print(f'Type: {type(a_list[i])} Value: {a_list[i]}')

print()
st = 'Hello#my#name#is#Lina'
b_list = st.split('#')
for i in range(len(b_list)):
    print(f'Элемент {i} - {b_list[i]}        len() - {len(b_list[i])}, max() - {max(b_list[i])}')
