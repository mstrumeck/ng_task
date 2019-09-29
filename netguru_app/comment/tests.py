import json

from django.test import TestCase

from comment.models import Comment


class CommentApiTest(TestCase):
    fixtures = ["test_data.json"]

    def test_simple_get_for_all_comments(self):
        response = self.client.get("/api/comment")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(str(response.content, encoding="utf8").split("}, {")),
            Comment.objects.count(),
        )

    def test_simple_get_when_comments_not_exist(self):
        Comment.objects.all().delete()
        response = self.client.get("/api/comment")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.content, encoding="utf8"), "[]")

    def test_simple_get_comments_for_movie(self):
        self.assertEqual(Comment.objects.count(), 8)
        self.assertEqual(Comment.objects.filter(movie_id=1).count(), 4)
        response = self.client.get("/api/comment/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(str(response.content, encoding="utf8").split("}, {")),
            Comment.objects.filter(movie_id=1).count(),
        )
        self.assertEqual(Comment.objects.filter(movie_id=1).count(), 4)
        self.assertEqual(Comment.objects.count(), 8)

    def test_post_new_comment(self):
        self.assertEqual(Comment.objects.count(), 8)
        self.assertEqual(Comment.objects.filter(movie_id=1).count(), 4)
        response = self.client.post("/api/comment/1", {"text": "test text"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Comment.objects.count(), 9)
        self.assertEqual(Comment.objects.filter(movie_id=1).count(), 5)

    def test_post_new_comment_without_text_field(self):
        self.assertEqual(Comment.objects.count(), 8)
        self.assertEqual(Comment.objects.filter(movie_id=1).count(), 4)
        response = self.client.post("/api/comment/1", {"othet_field": "test text"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Comment.objects.count(), 8)
        self.assertEqual(Comment.objects.filter(movie_id=1).count(), 4)
