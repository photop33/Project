import pymysql,json,os,signal
from flask import Flask, request

app = Flask(__name__)
# server runing on flask, back html and json content.
# local users storage
users = {}
# supported methods
@app.route('/users/get_user_data/<user_id>')
def user(user_id):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='12F1HSutPL', passwd='LB8D9pgJuP', db='12F1HSutPL')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM 12F1HSutPL.users WHERE ID")
    r = cursor.fetchall()
    return "<H1 id='user'>" + json.dumps(r) + "</H1>"
    if user_name == None:
        return "<H1 id='error'>" + "no_such_user" + user_id + "</H1>"

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'
app.run(host='127.0.0.1', debug=True, port=5001)
