#!C:\Users\Lina\AppData\Local\Programs\Python\Python310\python.exe

import cgi
import html
import funcs 
from random import randint

form = cgi.FieldStorage()
user_name = form.getvalue("name", "TestName")
group1 = form.getvalue("group1", False)
group2 = form.getvalue("group2", False)
group3 = form.getvalue("group3", False)
user_name = html.escape(user_name)

print ( 'Content-type: text/html\n' )

numbers = []
for i in range(8):
    numbers.append(randint(-7, 12))
    
print(f"<h3>{user_name}</h3>")    
    
print("Случайные числа: " + str(numbers))
print("<br><br>")

if group1:
    print("Результат функции группы 1: ")
    print(funcs.Func1(numbers))
    
print("<br>")

if group2:
    print("Результат функции группы 2: ")
    print(funcs.Func2(numbers))
    
print("<br>")    
    
if group2:
    print("Результат функции группы 3: ")
    print(funcs.Func3(numbers))