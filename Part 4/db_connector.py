import pymysql


def select():
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='12F1HSutPL', passwd='LB8D9pgJuP',db='12F1HSutPL')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM 12F1HSutPL.users;")
    for row in cursor:
        print(row)
    cursor.close()
    conn.close()

def insert():
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='12F1HSutPL', passwd='LB8D9pgJuP', db='12F1HSutPL')
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("INSERT into 12F1HSutPL.users (ID, name, date) VALUES (%s,%s,%s)",(users, user_name, now.strftime('%Y-%m-%d %H:%M:%S')))
    cursor.close()
    conn.close()

def delete():
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='12F1HSutPL', passwd='LB8D9pgJuP', db='12F1HSutPL')
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM 12F1HSutPL.users WHERE ID = 1")
    cursor.close()
    conn.close()

def update():
    res = requests.put('http://127.0.0.1:5000/users/1')
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='12F1HSutPL', passwd='LB8D9pgJuP', db='12F1HSutPL')
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("UPDATE SCHEMA_NAME.users SET name = 'george' WHERE ID = '1'")
    cursor.close()
    conn.close()

    