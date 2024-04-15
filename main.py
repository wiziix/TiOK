import requests
from flask import Flask, render_template, request
import json
from src.app import create_app

app = create_app()

#function that fetches the userdata then fills
#the dictionary with all the fetched unique usernames

def getUsernames():
    user_data = requests.get("https://jsonplaceholder.typicode.com/users")
    users = json.loads(user_data.content)
    usernames = {}

    for i in range(10):
        usernames[users[i]['id']] = users[i]['username']

    return usernames


#function that fetches the photo data
#then fills the thumbnails dictionary
#with all the unique thumbnail urls
#then returns the filled dictionary
def getThumbnails():
    photo_data = requests.get("https://jsonplaceholder.typicode.com/photos/")
    photos = json.loads(photo_data.content)
    thumbnails = {}
    for i in range(0, len(photos), 50):
        thumbnails[photos[i]['albumId']] = photos[i]['thumbnailUrl']

    return thumbnails



@app.route("/")
def hello_world():
    return render_template('home_page.html')
@app.route("/albums", methods=['GET'])
def Albums():
    response = requests.get("https://jsonplaceholder.typicode.com/albums/")
    album_content  = json.loads(response.content)


    return render_template('albums.html',
                    albums = album_content,
                    username = getUsernames(),
                    cover = getThumbnails())

@app.route("/posts")
def Posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts_content = json.loads(response.content)

    response = requests.get("https://jsonplaceholder.typicode.com/comments")
    comments_content = json.loads(response.content)


    return render_template('posts.html',
            posts = posts_content,
            username = getUsernames(),
            comment = comments_content)
@app.route("/albums/photos/<username>")
def photos(username):
    response = requests.get("https://jsonplaceholder.typicode.com/photos")
    photos_content = json.loads(response.content)

    return render_template('photos.html',
                photo = photos_content,
                user = username,
                index = find_key(getUsernames(), username),
                        )

def find_key(input_dict, value):
    for key, val in input_dict.items():
        if val == value: return key
    return "None"

