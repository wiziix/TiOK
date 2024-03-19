import requests
from flask import Flask
from flask import render_template

response = requests.get("https://jsonplaceholder.typicode.com/")
print(response)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home_page.html')
@app.route("/albums")
def Albums():
    return render_template('albums.html')
