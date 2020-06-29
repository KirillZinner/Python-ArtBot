import sqlite3

key_using = []
key_list = []

def sqlite3_simple_create_db():
    print("Таблица создана")
    con = sqlite3.connect('./ArtBot_base.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS answer_table(keyword TEXT,keyword2 TEXT, answer TEXT, emotion INTEGER)')
    con.commit()
    cur.close()
    con.close()

def sqlite3_simple_insert_db(w,w2,a,e):
    con = sqlite3.connect('./ArtBot_base.db')
    cur = con.cursor()
    cur.execute("INSERT INTO answer_table VALUES ('" + w + "','" + w2 + "','" + a + "','" + e + "')" )
    con.commit()
    cur.close()
    con.close()

def sqlite3_simple_delete_by_keyword_db(k):
    con = sqlite3.connect('./ArtBot_base.db')
    cur = con.cursor()
    print("Удаление варианта"+"'"+k+"'...")
    cur.execute("DELETE FROM answer_table WHERE keyword ="+"'"+k+"'")
    con.commit()
    cur.close()
    con.close()

def sqlite3_emotion_call_db(a):
    con = sqlite3.connect('./ArtBot_base.db')
    cur = con.cursor()
    cur.execute("SELECT emotion FROM answer_table WHERE answer = '" + a + "'")
    rows = cur.fetchone()
    #print(rows)
    if (rows):
        out = str(rows)
    else:
        out = "1";
    con.commit()
    cur.close()
    con.close()
    return out.replace(',', '').replace('(', '').replace(')', '').replace('\'', '')

def sqlite3_simple_call_db(wrd):
    con = sqlite3.connect('./ArtBot_base.db')
    cur = con.cursor()
    cur.execute("SELECT Answer FROM answer_table WHERE keyword = " + "'" + wrd + "'OR keyword2 = " + "'" + wrd + "'") #слово вообще встречается
    rows = cur.fetchone()
    print(rows)
    double_rows = None
    if rows: #если есть, записываем
        if (Check_collision_word(wrd)):
            key_list.append(wrd)
    for key in key_list:
        cur.execute("SELECT answer FROM answer_table WHERE keyword = " + "'" + key + "'AND keyword2 = " + "'"+ wrd + "'")
        double_rows = cur.fetchone()
        if double_rows:
            key_using.append(key)
            break
        if double_rows == None:
            cur.execute("SELECT answer FROM answer_table WHERE keyword = " + "'" + wrd + "'AND keyword2 = " + "'" + key + "'")
            double_rows = cur.fetchone()
            if double_rows:
                key_using.append(key)
            break
    if double_rows:
        rows = double_rows
    elif(Check_collision_using(wrd)):
        cur.execute("SELECT answer FROM answer_table WHERE keyword = " + "'" + wrd + "'AND keyword2 = " + "' '")    # если одиночное слово, перезаписываем
        rows = cur.fetchone()
    con.commit()
    cur.close()
    con.close()
    if rows:
        outp = str(rows)
        return outp.replace(',', '').replace('(', '').replace(')', '').replace('\'', '')
    else:
        return None

def Check_collision_word(key_w):
    for k in key_list:
        if k == key_w:
            return False
    return True

def Check_collision_using(k):
    for k_u in key_using:
        if k_u == k:
            return False
    return True