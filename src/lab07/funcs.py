def Func1(list):
    mul = 1
    for num in list:
        if num % 2 == 1:
            mul = mul * num
    return mul

def Func2(list):
    min = 0
    for num in list:
        if num  < min:
            min = num
    return min

def Func3(list):
    res_list = []
    for num in list:
        res_list.append(abs(num))
    res_list.sort()
    return res_list