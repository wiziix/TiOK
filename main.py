import logging
import requests
from flask import Flask, render_template, request, jsonify
import json
from src.app import create_app
import datetime

# Setting up the Flask app
app = create_app()

# Setting up logging
logger = logging.getLogger('main.py')
logger.setLevel(logging.ERROR)
formatter = logging.Formatter(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n%(process)d-%(levelname)s: %(message)s')
file_handler = logging.FileHandler('basic.log', encoding='utf-8', mode='w')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Function that fetches user data and fills the dictionary with all the fetched unique usernames
def getUsernames():
    try:
        user_data = requests.get("https://jsonplaceholder.typicode.com/users")
        user_data.raise_for_status()  # Raise exception for non-200 status codes
        users = json.loads(user_data.content)
        usernames = {}
        for i in range(10):
            usernames[users[i]['id']] = users[i]['username']
        return usernames
    except Exception as e:
        logger.error(f"Error fetching user data: {str(e)}")
        return {}

# Function that fetches photo data and fills the thumbnails dictionary with all the unique thumbnail urls
def getThumbnails():
    try:
        photo_data = requests.get("https://jsonplaceholder.typicode.com/photos/")
        photo_data.raise_for_status()  # Raise exception for non-200 status codes
        photos = json.loads(photo_data.content)
        thumbnails = {}
        for i in range(0, len(photos), 50):
            thumbnails[photos[i]['albumId']] = photos[i]['thumbnailUrl']
        return thumbnails
    except Exception as e:
        logger.error(f"Error fetching photo data: {str(e)}")
        return {}

# Route for the home page
@app.route("/")
def hello_world():
    return render_template('home_page.html')

# Route for fetching albums
@app.route("/albums", methods=['GET'])
def Albums():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/albums/")
        response.raise_for_status()  # Raise exception for non-200 status codes
        album_content = json.loads(response.content)
        initial_albums = album_content[:10]  # Load the first 10 albums initially

        return render_template('albums.html',
                               albums=initial_albums,
                               username=getUsernames(),
                               cover=getThumbnails())
    except Exception as e:
        logger.error(f"Error fetching albums data: {str(e)}")
        return render_template('error.html')

# Route for fetching more albums
@app.route("/load_more_albums", methods=['POST'])
def load_more_albums():
    try:
        current_album_count = int(request.form.get('current_album_count'))
        response = requests.get("https://jsonplaceholder.typicode.com/albums/")
        response.raise_for_status()  # Raise exception for non-200 status codes
        album_content = json.loads(response.content)
        new_albums = album_content[current_album_count:current_album_count + 10]
        username = getUsernames()
        thumbails = getThumbnails()
        thumbailCount = current_album_count + 1

        for album in new_albums:
            album.update({"username" : username.get(album.get("userId"))})
            album.update({"thumbnail" : thumbails.get(thumbailCount)})
            thumbailCount += 1

        return jsonify(new_albums)
    except Exception as e:
        logger.error(f"Error fetching more albums data: {str(e)}")
        return jsonify([])

# Route for fetching posts
@app.route("/posts")
def Posts():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        response.raise_for_status()  # Raise exception for non-200 status codes
        posts_content = json.loads(response.content)
        response = requests.get("https://jsonplaceholder.typicode.com/comments")
        response.raise_for_status()  # Raise exception for non-200 status codes
        comments_content = json.loads(response.content)
        return render_template('posts.html',
                               posts=posts_content,
                               username=getUsernames(),
                               comment=comments_content)
    except Exception as e:
        logger.error(f"Error fetching posts data: {str(e)}")
        return render_template('error.html')

# Route for fetching photos by username
@app.route("/albums/photos/<username>")
def photos(username):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/photos")
        response.raise_for_status()  # Raise exception for non-200 status codes
        photos_content = json.loads(response.content)
        return render_template('photos.html',
                               photo=photos_content,
                               user=username,
                               index=find_key(getUsernames(), username))
    except Exception as e:
        logger.error(f"Error fetching photos data: {str(e)}")
        return render_template('error.html')

# Function to find a key in a dictionary based on its value
def find_key(input_dict, value):
    for key, val in input_dict.items():
        if val == value:
            return key
    return "None"


def temp():
        response = requests.get("https://jsonplaceholder.typicode.com/albums/")

        album_content = json.loads(response.content)
        thumbnails = getThumbnails()

        print(thumbnails)

        #album_content[0].update({"username" : username.get(1)})

        print(album_content[0])

temp()