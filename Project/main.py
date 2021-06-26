from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_number = request.form.get("fn")
       # getting input with name = lname in HTML form
       second_number = request.form.get("sn")
       return str(int(first_number) + int(second_number))
    return render_template("Main.html")

if __name__=='__main__':
   app.run()
