from rest_app import user
from db_connector import select
import pymysql

res = requests.post('http://127.0.0.1:5000/users/2', json={"user_name": "david"})

res = requests.get('http://127.0.0.1:5000/users/2')

select()