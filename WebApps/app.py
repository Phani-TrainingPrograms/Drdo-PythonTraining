from flask import Flask, render_template, request, redirect, url_for

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
        print(f"User: {user_name}. Email : {user_email}, Password: {user_pwd}")
        return redirect(url_for('success', name = user_name))
    else:
        render_template('register.html')

@app.route("/success/<name>")
def success(name):
    return render_template('success.html', name = name)


if __name__ == '__main__':
    app.run(debug=True)