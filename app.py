from flask import Flask, render_template, abort, session, url_for, redirect
from forms import LoginForm, RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "dfewfew123213rwdsgert34tgfd1234trxf"

users = [
    {"id":1, "name":"admin", "email":"admin@test.com", "password":"admin"},
]

@app.route("/")
def landingPage():
    return render_template("landing-page.html")

@app.route("/login", methods=["POST","GET"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = next((user for user in users if user["email"] == form.email.data and user["password"] == form.password.data), None)
        if user is None:
            return render_template("login.html", form = form, message = "Akun tidak terdaftar !")
        else:
            return redirect(url_for('home'))

    return render_template("login.html", form = form)

@app.route("/register", methods=["POST","GET"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = {"id":len(users)+1, "name":form.name.data, "email":form.email.data, "password":form.password.data}
        users.append(new_user)
        return render_template("register.html", message = "Akun berhasil dibuat !", form = form)

    return render_template("register.html", form = form)

@app.route("/home")
def home():
    return render_template("home.html")

if  __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=3400)