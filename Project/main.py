from flask import Flask, request, render_template
import sqlite3

# Flask constructor
app = Flask(__name__)


con = sqlite3.connect('database.db', check_same_thread=False)
cur = con.cursor()
#cur.execute('''CREATE TABLE Sum(num1 real, num2 real, sum real)''')

@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        first_number = request.form.get("fn")
        second_number = request.form.get("sn")
        sum = int(first_number) + int(second_number)

        cur.execute('insert into Sum (num1, num2, sum) values (' + str(first_number) + ',' + str(second_number) + ',' + str(sum) + ')')
        con.commit()
        cur.execute('''select * from Sum''')
        data = cur.fetchall()
        for x in data:
            print(x)
        return str(int(sum))
    return render_template("Main.html")


if __name__ == '__main__':
    app.run()
