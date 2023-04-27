from flask import render_template, flash, redirect, url_for
from readaholic.forms import AdminRegistrationForm, AdminLoginForm, AdminAddBooksForm, AdminCommentForm
from readaholic import db, app, bcrypt
from readaholic.models import User, Comment

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
        _email = form.data['email']
        _password = form.data['password']
        _password = bcrypt.generate_password_hash(_password).decode("utf-8")
        user = User(email=_email, password=_password)
        try:
            db.session.add(user)
            db.session.commit()
            flash("Account successfully created, you may now login","success") 
            return redirect(url_for("login"))
        except:
            flash("Something went wrong with database","warning")
        # print("registered")
    return render_template("register.html",form=form)

@app.route("/login", methods=["GET","POST"])
def login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        _email = form.data['email']
        _password = form.data['password']
        user = User.query.filter_by(email=_email).first()
        if not user:
            flash(f"No user with email{_email} found! Register today.","danger")
            return redirect(url_for("register"))
        else:
            if bcrypt.check_password_hash(user.password, _password):
                flash("Successfully logged in!","success")
                return redirect(url_for("home"))
            else:
                flash("You've entered wrong password, please try again!")
    return render_template("login.html",form=form)

@app.route("/books", methods=["GET","POST"])
def books():
    form = AdminAddBooksForm()
    if form.validate_on_submit():
        print(form.data)
    return render_template("book.html",form=form)

@app.route("/comment", methods=["GET","POST"])
def comment():
    form = AdminCommentForm()
    if form.validate_on_submit():
        _name = form.data['name']
        _email = form.data['email']
        _comment = form.data['comment']
        comment = Comment(name=_name, email=_email, comment=_comment)
        db.session.add(comment)
        db.session.commit()
        print(" comment added")
    return render_template("comment.html",form=form)