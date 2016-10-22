
from flask import Flask
app = Flask(__name__)

from secrets import API_KEY

@app.route("/")
def hello():
    return API_KEY 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
