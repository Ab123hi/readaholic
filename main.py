from flask import Flask, render_template

app = Flask(__name__)

website_name = "Readaholic"
data={
    "website_name": "Readaholic",
    "author": "Abhishek",
    "msg": "You will become a coder in future"
}

@app.route("/")
def home():
    return render_template("home.html", data=data)

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

if __name__ == "__main__":
    app.run(debug=True)
