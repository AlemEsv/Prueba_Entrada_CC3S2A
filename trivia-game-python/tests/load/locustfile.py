from locust import HttpUser, task
class triviaUser(HttpUser):
    @task
    def play_trivia(self):
        self.client.get("/play")