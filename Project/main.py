from flask import Flask, request, render_template
import sqlite3

# Flask constructor
app = Flask(__name__)


con = sqlite3.connect('database.db', check_same_thread=False)
cur = con.cursor()
#cur.execute('''CREATE TABLE Sum(num1 real, num2 real, sum real)''')

@app.route('/')

@app.route('/sum', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        first_number = request.form.get("fn")
        second_number = request.form.get("sn")
        sum = int(first_number) + int(second_number)

        cur.execute('insert into Sum (num1, num2, sum) values (' + str(first_number) + ',' + str(second_number) + ',' + str(sum) + ')')
        con.commit()
        cur.execute('''select Count(*) from Sum''')
        data = cur.fetchall()
        data_str = str(data[0])
        return data_str[1:-2] + ":" + str(sum)
    return render_template("login.html")


@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
    return render_template('login.html', msg = msg)

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        msg += "Hello "
        msg += username
        return render_template('login.html', msg = msg)
    return render_template('register.html', msg = msg)


if __name__ == '__main__':
    app.run()
