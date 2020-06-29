import pymorphy2
import sqlite3
from random import randint
import reaction, dbfunc, admin

morph = pymorphy2.MorphAnalyzer()

def Check_collision_answer(a):
    for answer in answers:
        if answer == a:
            return False
    return True

while(True):
    answers = []
    line = input()
    if(line == "1234"):
        admin.Admin_mode_func()
    else:
        check_one = True
        words = line.replace('.', '').replace(',', '').replace('?', '').replace('!', '').split()
        last_answer_str = ''
        for word in words:
            forms = morph.parse(word)
            last_answer_str = ''
            for form in forms:
                answer_str = dbfunc.sqlite3_simple_call_db(str(form.normal_form))
                if (answer_str): #если ответ есть
                    if(Check_collision_answer(answer_str)):
                        answers.append(answer_str)
                    check_one = False
        if(answer_str == None and check_one):
            print(reaction.random_phrase_func() + " " + reaction.emotion_func(4))
        else:
            for answer in answers:
                print(answer + " " + reaction.emotion_func(int(dbfunc.sqlite3_emotion_call_db(answer))))
