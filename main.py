from flask import Flask, render_template
from forms import AdminRegistrationForm
from forms import AdminLoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='secret_key_33'

# website_name = "Readaholic"
# data={
#     "website_name": "Readaholic",
#     "author": "Abhishek",
#     "msg": "You will become a coder in future"
# }

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register", methods=["GET","POST"])
def register():
    form = AdminRegistrationForm()
    if form.validate_on_submit():
        print(form.data)
    return render_template("register.html",form=form)

@app.route("/login", methods=["GET","POST"])
def login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        print(form.data)
    return render_template("login.html",form=form)

if __name__ == "__main__":
    app.run(debug=True)
