import json

from django.test import TestCase

from movie.models import Movie


class MovieApiTest(TestCase):
    fixtures = ["test_data.json"]

    def test_simple_get_with_movies(self):
        response = self.client.get("/api/movie")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(str(response.content, encoding="utf8").split("}, {")), 4)

    def test_get_without_any_movie(self):
        Movie.objects.all().delete()
        response = self.client.get("/api/movie")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.content, encoding="utf8"), "[]")

    def test_post_with_existet_movie_title_in_request(self):
        self.assertEqual(Movie.objects.count(), 4)
        response = self.client.post("/api/movie", data={"title": "Doctor Strange"})
        self.assertEqual(response.status_code, 200)
        encoded_json = json.loads(str(response.content, encoding="utf8"))
        self.assertEqual(encoded_json["id"], 4)
        self.assertEqual(encoded_json["title"], "Doctor Strange")
        self.assertEqual(len(encoded_json), 14)
        self.assertEqual(Movie.objects.count(), 4)

    def test_post_with_movie_title_in_request_but_not_in_database(self):
        self.assertEqual(Movie.objects.count(), 4)
        response = self.client.post("/api/movie", data={"title": "Spider"})
        self.assertEqual(response.status_code, 201)
        encoded_json = json.loads(str(response.content, encoding="utf8"))
        self.assertEqual(encoded_json["id"], 5)
        self.assertEqual(encoded_json["title"], "Spider")
        self.assertEqual(len(encoded_json), 14)
        self.assertEqual(Movie.objects.count(), 5)

    def test_post_without_movie_title_in_request(self):
        response = self.client.post("/api/movie")
        encoded_json = json.loads(str(response.content, encoding="utf8"))
        self.assertEqual(encoded_json, {"error": "You have to provide film title!"})
