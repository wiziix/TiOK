import requests
from flask import Flask, render_template, request
import json

users = requests.get("https://jsonplaceholder.typicode.com/users")
user = json.loads(users.content)

res = requests.get("https://jsonplaceholder.typicode.com/photos/")
photos = json.loads(res.content)

#album thumbnails dictionary
#where keys are albumIDs
#and values are thumbnail URLs
thumbnails = {}

for i in range(0,len(photos), 50):
    thumbnails[photos[i]['albumId']] = photos[i]['thumbnailUrl']


#usernames dictionary
#where keys are userIDs
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
    response = requests.get("https://jsonplaceholder.typicode.com/albums/")
    album_content  = json.loads(response.content)


    return render_template('albums.html',
                           albums = album_content,
                           username = usernames,
                           cover = thumbnails)

@app.route("/posts")
def Posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts_content = json.loads(response.content)

    response = requests.get("https://jsonplaceholder.typicode.com/comments")
    comments_content = json.loads(response.content)

    comments = {}

    for i in range(0, len(comments_content), 4):
        comments[comments_content[i]['postId']] = comments_content[i]['id']

    print(comments)


    return render_template('posts.html',
                           posts = posts_content,
                           username = usernames)
