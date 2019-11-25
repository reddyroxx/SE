
from flask import Flask,render_template ,redirect, url_for , request
#import requests
import sqlite3 as sql
#import os.path
import datetime
from werkzeug import secure_filename

conn=sql.connect("database.db")

 
app = Flask(__name__)
@app.route('/home')
def home():
    return render_template("registration.html")


@app.route("/video",methods=["POST","GET"])
def video():
    if request.method=='POST':
        return render_template("video.html")

@app.route("/user_profile",methods=["POST","GET"])
def user_profile():
    if request.method=='POST':
        return render_template("user.html")

@app.route("/add_user",methods=["POST","GET"])
def add_user():
    if request.method=='POST':
        si = request.form['id']
        name = request.form['name']
        contact_no = request.form['contact_no']
        ty = request.form['t']
        p = request.form['pwd']
    
        
    conn = sql.connect("database.db")
    
    insert_command = "INSERT INTO stakeholder values\
                        ('"+si+"','"+name+"','"+contact_no+"','"+ty+"','"+p+"');"
    conn.execute(insert_command)
    conn.commit()    
    return render_template("homepage.html")

@app.route("/check_user",methods=["POST","GET"])
def check_user():
    if request.method == 'POST':
        si=request.form['id']
        p = request.form['pwd']
        ty = request.form['t']
    conn=sql.connect("database.db")
    command = "select password from stakeholder where customer_id ='"+si+"';" 
    command1 = "select Type from stakeholder where customer_id ='"+si+"';"    
    a = list(conn.execute(command))[0][0]
    b = list(conn.execute(command1))[0][0]
    if a==p:
        if b==ty and b=='L':
            return render_template("Laywer.html")
        elif b==ty and b=='O':
            return render_template("homepage.html")
        elif b==ty and b=='T':    
            return render_template("homepage.html")
        else:
            return render_template('homepage.html')
    else:
        return render_template("registration.html")

@app.route("/branch",methods=["POST","GET"])
def branch():
    if request.method == 'POST':
        tableName=request.form['branch']
    conn=sql.connect("database.db")
    command="select branch_id from branch where location = '"+tableName+"';"
    b_id = list(conn.execute(command))[0][0]
    
    return render_template("branch_"+b_id+".html")

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        return render_template("h2.html")   


if __name__ == '__main__':
    app.run(debug=True)
    

