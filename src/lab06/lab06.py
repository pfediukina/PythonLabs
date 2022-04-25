import mymod

def func1( my_list ):
    sum = 0
    for i in my_list:
        if(type(i) == int or type(i) == float):
            sum += i
    return sum / len(my_list)

def func2(input_dict, value):
    return_list = []
    for key, val in input_dict.items():
        if val == value: return_list.append(key)
    return return_list
    
def func3(input_list):
    return_list = []
    for item in input_list:
        if(type(item) != list):
            return_list.append(int(item)) 
        else:
            for item2 in item:
                return_list.append(item2)
    return return_list
    
my_list = [1, 2, 3, 4, 6]
print(func1(my_list))    
print()  
 
a_dict = {
  1: 'a',
  2: 'b',
  3: 'c',
  4: 'd',
  5: 'e',
  6: 'f',
  7: 'g',
  8: 'h',
  9: 'a',
  10: 'b',
  11: 'a'
}
print(func2(a_dict, 'a'))
print() 

a_list = list(['1123', '11', list([1, 2, 3])])
res_list = func3(a_list)
print(res_list)
res_list.sort()
res_list.reverse()
print(res_list)
print()

str_code = "print(\'Hello, World!\')"
comp_code = compile(str_code,'<string>' , 'exec');
exec(comp_code)

mymod.HelloWorld()