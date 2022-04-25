from math import fabs
import random

words = ('телевизор', 'подушка', 'маникюр', 'трафарет', 'перекись')

correct_word = random.choice(words)
word_list = list(correct_word)
random.shuffle(word_list);
word = ''.join(str(e) for e in word_list)

print('''
          Игра "АНАГРАММА"
   Для выхода - нажмите клавишу Enter''')
print('\nЭто анаграмма: ', word.upper())

hints = 3

true_answer = False
while(true_answer == False):
    print('Количество подсказок (введите *****а*, чтобы узнать, есть ли буква А на 6 месте): ' + str(hints))
    print('\nЭто анаграмма: ', word.upper())
    user_word = input('Найди исходное слово: ').casefold()
    l_user_word = list(user_word)
    
    is_hint = False
    hint_pos = 0
    
    for i in range(len(l_user_word)):
        if(l_user_word[i] == '*'):
            is_hint = True
        else:
            hint_pos = i
            
    if(is_hint == True & hint_pos < len(correct_word)):
        hints = hints - 1
        if(correct_word[hint_pos] != l_user_word[hint_pos]):
            print('Этой буквы на месте нет!')
        else:
            print('Да, буква есть на данной позиции ' + user_word)
    
    elif(user_word == correct_word):
        print('Молодец!')
        true_answer = True
    else:
         print('Ответ неверный. Попробуй заново!')
         
    print()

print('Спасибо за игру')