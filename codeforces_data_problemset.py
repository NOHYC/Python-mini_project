import time
import random
import json
import hashlib
import requests
import mysql.connector as mc
from mysql.connector import Error as mce
import sys

my_key='b432cf2b7fab4b0b4b19115828cdbdbf64e85349'
my_secret='44e8945437f56c7f3940104c10e66d97a23539ed'
rand_prefix = str(random.randint(100000,999999))
now = str(int(time.time()))
method_name = 'problemset.problems'
method_param=[]
hash_in = rand_prefix+ '/' + method_name + '?' + f'apiKey={my_key}&time={now}' + '#' + my_secret
hash_code = hashlib.sha512(str(hash_in).encode('utf-8')).hexdigest()

url = f'https://codeforces.com/api/{method_name}?apiKey={my_key}&time={now}&apiSig={rand_prefix}{hash_code}'

res = requests.get(url)
j_dict = json.loads(res.text)
if j_dict['status']=='OK':
    tag_set=set()
    for prob in j_dict['result']['problems']:
        for tag in prob['tags']:
            tag_set.add(tag)
    tag_list=list(tag_set)
else:
    print(j_dict['comment'])
    sys.exit()

conn = mc.connect(user='root', password='1203', host='127.0.0.1')
cur = conn.cursor()
cur.execute('create database if not exists code_forces_api_re')
cur.execute('use code_forces_api_re')

cur.execute('show tables')
if 'Prob_set' not in cur.fetchall():
    set_arg = ','.join([*map(lambda x: "'"+x+"'",tag_list)])
    sql=f'''create table Prob_set(
        id varchar(50) not null,
        name varchar(65) not null,
        difficulty int(11) not null,
        tags set({set_arg}),
        primary key(`id`)
    )'''
    cur.execute(sql)
#primary key(`name`)
    for prob in j_dict['result']['problems']:
        pid = str(prob['contestId'])+'/'+prob['index']
        name = prob['name']
        name = name.replace("'","\'")
        name = name.replace('''"''','''\'''')
        # tags = '('+','.join(prob['tags'])+')'

        tags = ','.join(prob['tags'])
        try:
            diff = prob['rating']
        except KeyError:
            diff = 0
        try:
            cur.execute(f'''insert into code_forces_api_re.Prob_set values("{pid}","{name}",{diff},"{tags}")''')
        except Exception as e:
            print(e)

    conn.commit()
else:
    pass

conn.close()
print('DB generation completed')