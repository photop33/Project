from flask import Flask, request
import requests, json,pymysql,datetime,time
app = Flask(__name__)

# local users storage
users = {}


# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        res = requests.get('http://127.0.0.1:5000/users/1')
        conn = pymysql.connect(host='remotemysql.com', port=3306, user='12F1HSutPL', passwd='LB8D9pgJuP',db='12F1HSutPL')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM 12F1HSutPL.users;")
        return {'status':"ok","user_name":user_name}, 200 # status code
    else:
        return {'status':"error","reason":"no such id"}, 500 # status code

    if request.method == 'POST':
        res = requests.post('http://127.0.0.1:5000/users/1', json={"user_name": "itay"})
        conn = pymysql.connect(host='remotemysql.com', port=3306, user='12F1HSutPL', passwd='LB8D9pgJuP',db='12F1HSutPL')
        conn.autocommit(True)
        cursor = conn.cursor()
        now = datetime.datetime.utcnow()
        cursor.execute("INSERT into 12F1HSutPL.users (ID, name, date) VALUES (%s,%s,%s)" , (users, user_name, now.strftime('%Y-%m-%d %H:%M:%S')))
        cursor.close()
        conn.close()
        request_data = request.json
        user_name = request_data.get('user_name')
        users[user_id] = user_name
        return {'status': 'ok',"user_added":user_name}, 200  # status code
    else:
        return {'status':"error","reason":"id already exists"}, 500 # status code

    if request.method == 'PUT':
        res = requests.put('http://127.0.0.1:5000/users/1')
        conn = pymysql.connect(host='remotemysql.com', port=3306, user='12F1HSutPL', passwd='LB8D9pgJuP',db='12F1HSutPL')
        conn.autocommit(True)
        cursor = conn.cursor()
        cursor.execute("UPDATE SCHEMA_NAME.users SET name = 'george' WHERE ID = '1'")
        cursor.close()
        conn.close()
        return {'status': 'ok',"user_update":user_name}, 200  # status code
    else:
        return {'status':"error","reson":"no such id"}, 500 # status code

    if request.method == 'DELETE':
        res = requests.delete('http://127.0.0.1:5000/users/1')
        conn = pymysql.connect(host='remotemysql.com', port=3306, user='12F1HSutPL', passwd='LB8D9pgJuP',db='12F1HSutPL')
        conn.autocommit(True)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM 12F1HSutPL.users WHERE ID = 1")
        cursor.close()
        conn.close()
        return {'status': 'ok',"user_deleted":user_id}, 200  # status code
    else:
        return {'status':"error","reson":"no such id"}, 500 # status code


app.run(host='127.0.0.1', debug=True, port=5000)