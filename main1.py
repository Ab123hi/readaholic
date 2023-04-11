from flask import Flask 

app = Flask(__name__)

#grouping of routes together
@app.route("/route1")
@app.route("/route2")
@app.route("/route3")
def name():
    return "<h1>Hello, Abhishek</h1>"

if __name__ == "__main__":
    app.run(debug=True)
