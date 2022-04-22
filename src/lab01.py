help("%")

s= input ( 'Введите десятичное число ' )
number1 = int(s)
s = input ('Введите шестнадцатиричное число ')
number2 = int(s, 16)

result = number1 // number2

if type(result) == float:
    result = int(result)

operation_string = str(number1) + ' // ' + str(number2) + ' = ' + str(result)
print(operation_string)
result8 = oct(result).replace('0o', '')
print('Восьмеричный результат: ' + result8)

s = input('Введите первое число, заданное в двоичной системе и имеющее длину 8 битов: ')
number1 = int(s, 2)
s = input('Введите второе число, заданное в двоичной системе и имеющее длину 8 битов: ')
number2 = int(s, 2)

result = number1 >> number2
print('Результат сдвига вправо: ' + format(result, 'b') + ' Десятичное: ' + str(result))