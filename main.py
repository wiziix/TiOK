import requests
from flask import Flask
from flask import render_template

response = requests.get("https://jsonplaceholder.typicode.com/")
print(response)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    return render_template('home_page.html')
