import requests
from flask import Flask
from flask import render_template, request
import json

response = requests.get("https://jsonplaceholder.typicode.com/albums/1")

users = requests.get("https://jsonplaceholder.typicode.com/users")

user = json.loads(users.content)

#usernames dictionary
#keys are userIDs
#values are usernames
usernames = {}

#filling the usernames dict
for i in range(10):
    usernames[user[i]['id']] = user[i]['username']



app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home_page.html')
@app.route("/albums", methods=['GET'])
def Albums():
    response = requests.get("https://jsonplaceholder.typicode.com/albums/1")
    y = json.loads(response.content)

    return render_template('albums.html', username = usernames[int(y['userId'])],
                           title = y['title'])
