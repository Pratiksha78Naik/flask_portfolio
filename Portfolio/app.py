from flask import Flask,render_template,request
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Pratu@123"
app.config['MYSQL_DB']="adit"
mysql=MySQL(app)
@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method=='POST':
     username=request.form['username']
     email=request.form['email']
     cur=mysql.connection.cursor()
     cur.execute("INSERT INTO user(username,email) VALUES(%s, %s)",(username,email))
     mysql.connection.commit()
     cur.close()
     return"Success"
    return render_template('index.html')
if __name__== "__main__":
    app.run(debug=True)