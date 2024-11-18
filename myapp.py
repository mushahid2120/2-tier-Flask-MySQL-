
from flask import Flask,redirect,render_template,request,jsonify
import pymysql
import os

HOST=os.getenv('HOST')
USER=os.getenv('USER')
PASSWORD=os.getenv('PASSWORD')
DATABASE=os.getenv('DATABASE')

print("Environmental variable = ",HOST," ",USER," "," ",PASSWORD," ",DATABASE)

app=Flask(__name__)

myconnection=pymysql.connect(host=HOST,user=USER,passwd=PASSWORD,database=DATABASE)
print(myconnection)

def initDB():
    global myconnection
    try:
        cur=myconnection.cursor()
        print('connection ',cur)
        cur.execute('CREATE DATABASE IF NOT EXISTS myapp')
        cur.execute('USE myapp')
        if (cur.execute('CREATE TABLE IF NOT EXISTS Messages (data VARCHAR(30))')==0):
            print( "database created")
        cur.close()

    except pymysql.MySQLError as error:
        print(error)

@app.route('/')
def home():
    fetchMessage=fetchData()
    print("fetched data : ",fetchMessage)
    return render_template('index.html',messages=fetchMessage)


@app.route('/submit',methods=['POST'])
def submit():
    text=request.form.get('data')
    print(f"Received text: {text}")
    store(text)
    # return jsonify({'message':text})
    return redirect('/')

@app.route('/testing')
def test():
    return "I am testing !!!!!"


initDB()


def fetchData():
    global myconnection
    try:
        cur=myconnection.cursor()
        cur.execute('SELECT data FROM Messages where data is not null')
        retrievedMessages=cur.fetchall()
        cur.close()    
        return retrievedMessages
    except pymysql.MySQLError as error:
        print(error)



def store(text):
    print(text)
        # result=myconnection.query('create table student(name varchar(20)) ')
    global myconnection
    try:
        cur=myconnection.cursor()
        if (cur.execute('INSERT INTO Messages (data) VALUES (%s)', (text,))):
            print(f'query registered {text}')
        myconnection.commit()      
        cur.close()

    except pymysql.MySQLError as err:
        print(err); 



app.run(port=80,host='0.0.0.0')
