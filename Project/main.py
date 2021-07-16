from flask import Flask, request, render_template
import sqlite3

# Flask constructor
app = Flask(__name__)


con = sqlite3.connect('database.db', check_same_thread=False)
cur = con.cursor()
#cur.execute('''CREATE TABLE Sum(num1 real, num2 real, sum real)''')
#cur.execute('''DROP TABLE Accounts''')
#cur.execute('''CREATE TABLE Accounts(username text NOT NULL, password text NOT NULL, email text NOT NULL,UNIQUE(username, email))''')
#cur.execute('''DROP TABLE Uchenici''')
cur.execute('''CREATE TABLE "Uchenici" (
	"Godini"	INTEGER,
	"Pol"	TEXT,
	"uchilishte_id"	INTEGER,
	FOREIGN KEY(uchilishte_id) REFERENCES Uchilishte(id)
)''')
@app.route('/')

@app.route('/sum', methods=["GET", "POST"])

@app.route('/login', methods=["GET", "POST"])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        if username == '' or password == '':
            return render_template('login.html', msg = "error logging in")
        cur.execute('SELECT * FROM Accounts WHERE username = "{u1}" AND password = "{p1}"'.format(u1=username,p1=password, ))
        account = cur.fetchone()
        if account:
            msg = username
            return render_template('Main.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)


@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        if username == '' or password == '' or email == '':
            return render_template('register.html', msg = "error registering")
        execute = "insert into Accounts (username, password, email) values('{u1}','{p1}','{e1}')".format(u1 = username, p1 = password, e1 = email)
        cur.execute(execute)
        con.commit()
        msg += "Hello " + username + '\n' + "Please log in."
        return render_template('login.html', msg = msg)
    return render_template('register.html', msg = msg)


if __name__ == '__main__':
    app.run()
