from random import randint

def random_phrase_func():
    rnd = randint(0, 9)
    if(rnd == 9):
        return "Не совсем понял..."
    elif(rnd == 8):
        return "Что?"
    elif (rnd == 7):
        return "Что ты имеешь ввиду?"
    elif (rnd == 6):
        return "Ммм?"
    elif (rnd == 5):
        return "Не понял тебя..."
    elif (rnd == 4):
        return "Что ты хочешь сказать?"
    elif (rnd == 3):
        return "В каком смысле?"
    elif (rnd == 2):
        return "Как как?"
    elif (rnd == 1):
        return "Не понял..."
    else:
        return "Не понимаю..."

def emotion_func(num):
    if(num == 8):
        return "*Радость*"
    elif (num == 7):
        return "*Печаль*"
    elif (num == 6):
        return "*Плачь*"
    elif (num == 5):
        return "*Гнев*"
    elif (num == 4):
        return "*Удивление*"
    elif (num == 3):
        return "*Страх*"
    elif (num == 2):
        return "*Презрение*"
    elif (num == 1):
        return "*Безразличие*"
    else:
        return "*Безразличие*"