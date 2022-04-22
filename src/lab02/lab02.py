s1 = input('Введите имя, фамилию и отчество: ')
print('Строка со срезом: ' + s1[3:8])
s2 = input('Введите группу: ')
s3 = s1 + s2
print(s3)

print('count(ин): '+ str( s3.count('ин') ))
print('islower(): '+ str( s3.islower() ))
print('rindex(и): '+ str( s3.rindex('и') ))
print('swapcase(): '+ s3.swapcase() )

questions = ['Назовите метод для поиска строки: ', 'Логический тип: '] 
questions += ['Каким представлением записать число в двоичном формате? ', 'Что возникает, если срез равен 0? '] 
questions += ['Как запустить бесконечный цикл? ']
answers = ['find()', 'bool', 'b', 'Ошибка', 'while true']
mark = 0

for i in range(5):
    answer = input(questions[i])
    if(answer == answers[i]):
        mark += 1

print( s1 + ': ' + str(mark) + "/5.")

string = input('Введите строку: ')
num = input('Введите число: ')
fnum = input('Введите дробное число (5.23): ')
print(f"Строка: {string}, число: {num}, дробь: {fnum}")