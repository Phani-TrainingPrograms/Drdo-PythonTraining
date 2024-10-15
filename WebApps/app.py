from flask import Flask, render_template, request, redirect, url_for
import datetime

from mysql_database import MySqlDatabase

app = Flask(__name__)

@app.route("/")
def index():
    # data for the Html:
    # user_name = "Phaniraj"
    # address = "RR Nagar, Bangalore"
    user_info ={
        'name' : "Phaniraj",
        'address' : "RR Nagar, Bangalore",
        'email' : "phanirajbn@gmail.com"
    }
    return  render_template("index.html", admin = user_info)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_name = request.form['username']
        user_pwd = request.form['password']
        user_email = request.form['email']
        db = MySqlDatabase()
        db.add_user(user_name, user_pwd, user_email)
        return redirect(url_for('allusers'))
    else:
        return render_template('register.html')

@app.route("/success/<name>")
def success(name):
    return render_template('success.html', name = name)

@app.route("/allusers")
def allusers():
    db = MySqlDatabase()
    users = db.get_all_users()
    year = datetime.datetime.today().year
    return render_template("allusers.html", year = year, users = users)

@app.route("/details")
def user_details():
    user_id = request.args.get('id')
    db = MySqlDatabase()
    user = db.get_user_by_id(user_id)
    if user:
        return render_template('details.html', user = user)
    else:
        return 'User not found', 404

@app.route("/update_user", methods = ['POST'])
def update_user():
    user_id = int(request.form['user_id'])
    name = request.form['username']
    password = request.form['password']
    email = request.form['email']
    db = MySqlDatabase()
    print(f"{user_id}, {name}, {password}, {email}")
    db.update_user(user_id, name, password, email)
    return redirect(url_for('allusers'))

if __name__ == '__main__':
    app.run(debug=True)