
from flask import Flask
from flask import request, render_template
app = Flask(__name__)

from secrets import API_KEY

@app.route("/login")
def hello():
    return render_template('login.html') 

@app.route("/")
def login():
    return render_template('index.html') 


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
