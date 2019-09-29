from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView

from movie.models import Movie
from .serializer import CommentSerializer
from ..models import Comment


@permission_classes((permissions.AllowAny,))
class CommentApiView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)


@permission_classes((permissions.AllowAny,))
class CommentApiViewForFilm(APIView):
    def get(self, request, movie_id):
        movie_comments = Movie.objects.get(id=movie_id).comment_set.all()
        serializer = CommentSerializer(instance=movie_comments, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)

    def post(self, request, movie_id):
        if request.data.get("text"):
            movie = Movie.objects.get(id=movie_id)
            comment = Comment.objects.create(movie=movie, text=request.data.get("text"))
            serializer = CommentSerializer(instance=comment)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse({"error": 'lack of "text" data.'}, status=400)
