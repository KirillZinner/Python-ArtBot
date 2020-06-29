import dbfunc,reaction

def Admin_mode_func():
    while (True):
        print("Режим изменения данных - для добавить введите 'a' для удаления 'd' для выхода из режима любую другую букву")
        check_k = input()
        if (check_k == "a" or check_k == "а" or check_k == "A" or check_k == "А"):  # add
            print("Введите ключевое слово")
            key_word = input().lower()
            print("Введите ключевое слово 2, если его нет, то пробел")
            key_word2 = input().lower()
            print("Введите ответ на это слово")
            answer = input()
            print("Введите эмоцию")
            emot = input()
            print(key_word)
            print(key_word2)
            print(answer)
            print(reaction.emotion_func(int(emot))+"[" + emot +"]")
            dbfunc.sqlite3_simple_insert_db(key_word,key_word2, answer,emot)
        elif (check_k == "d" or check_k == "D"):
            print("Введите ключевое слово")
            key_word = input().lower()
            dbfunc.sqlite3_simple_delete_by_keyword_db(key_word)
        else:
            print("Выход из режима редактирования")
            break
