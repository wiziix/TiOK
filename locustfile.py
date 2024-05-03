from locust import HttpUser, task, between
from main import getUsernames

class HelloWorldUser(HttpUser):

    wait_time = between(1,5)

    @task
    def view_homepage(self):
        self.client.get("/")

    @task(3)
    def view_albums(self):
        self.client.get("/albums")

    @task(2)
    def view_posts(self):
        self.client.get("/posts")

    @task(3)
    def view_photos(self):
        usernames = getUsernames()
        for username in usernames:
            self.client.get(f"/albums/photos/{usernames[username]}", name='/usernames')
