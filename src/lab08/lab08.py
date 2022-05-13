#!C:\Users\Lina\AppData\Local\Programs\Python\Python310\python.exe

import cgi
import os
import helper

print ( 'Content-type: text/html\n' )
form = cgi.FieldStorage()
user_name   = form.getvalue("name", "TestName")
user_univ   = form.getvalue("university", "TestUniv")
user_email  = form.getvalue("email", "TestEmail")

current_dir = os. getcwd()
current_dir = current_dir + "\CGI"

if not os.path.exists(current_dir):
    os.makedirs(current_dir)
    
f_name = open('./CGI/name.txt', 'w')
f_values = open('./CGI/values.txt', 'w')
f_name.write(user_name)
f_values.writelines({user_univ, "\n", user_email})

f_name.close()
f_values.close()

fn_lenth = os.stat("./CGI/name.txt").st_size
fv_lenth = os.stat("./CGI/values.txt").st_size
print(f"Длинна файла name.txt - {fn_lenth}<br>Длинна файла values.txt - {fv_lenth}")

print("<br><h3>values.txt</h3>")
f_values = open('./CGI/values.txt', 'r')
print(f_values.readline())
f_values.close()

f_binary = open ('./CGI/binary_data.dat', 'bw')
l_numbers = range(2, 14)
f_binary.write(bytearray(l_numbers))
f_binary.close()

f_binary = open("./CGI/binary_data.dat", "rb") 
data = f_binary.read() 
print(f"<br>Значение байта 6 (последовательность 2-14): {data[6]}")
f_binary.seek(10)
print(f"<br>Значение 3 байтов после смещения: {data[2]} {data[3]} {data[4]}")
f_binary.close()

try:
    c=12
    assert helper.isPrime(c)
    print ( 'Число простое ' + c)
except ZeroDivisionError:
    print ( 'Ошибка: деление на 0' )
except AssertionError:
    print ( 'Число не простое ' + c)