from django.test import TestCase
import json
from comment.models import Comment
from movie.models import Movie


class TopApiTest(TestCase):
    fixtures = ["test_data.json"]

    def test_of_create_ranking(self):
        response = self.client.get("/api/top")
        self.assertEqual(response.status_code, 200)
        decoded_content = json.loads(str(response.content, encoding="utf8"))
        self.assertEqual(len(decoded_content), 4)
        self.assertEqual([x["rank"] for x in decoded_content].count(2), 2)
        self.assertEqual(
            sum([x["comments"] for x in decoded_content]), Comment.objects.count()
        )

    def test_of_get_top_with_from(self):
        response = self.client.get("/api/top/2019-09-27")
        self.assertEqual(response.status_code, 200)
        decoded_content = json.loads(str(response.content, encoding="utf8"))
        self.assertEqual(sum([x["comments"] for x in decoded_content]), 4)

    def test_of_get_top_within_range(self):
        response = self.client.get("/api/top/2019-09-28/2019-09-29")
        self.assertEqual(response.status_code, 200)
        decoded_content = json.loads(str(response.content, encoding="utf8"))
        self.assertEqual(sum([x["comments"] for x in decoded_content]), 2)

    def test_without_any_movie_in_database(self):
        Movie.objects.all().delete()
        response = self.client.get("/api/top")
        self.assertEqual(response.status_code, 400)
        decoded_content = json.loads(str(response.content, encoding="utf8"))
        self.assertEqual(
            decoded_content["error"], "No films in database. Populate database first."
        )
