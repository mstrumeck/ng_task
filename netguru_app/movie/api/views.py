import requests
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView

from movie.api import utils
from movie_database.settings import API_KEY
from .serializers import MovieSerializer
from ..models import Movie


@permission_classes((permissions.AllowAny,))
class MovieApiView(APIView):
    def get(self, request):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        if request.data.get("title"):
            movie_title = request.data.get("title")
            if Movie.objects.filter(title__contains=movie_title).exists():
                movie = Movie.objects.filter(title__contains=movie_title).first()
                serializer = MovieSerializer(instance=movie)
                return JsonResponse(serializer.data, status=200)
            else:
                response = requests.get(
                    f"http://www.omdbapi.com/?t={movie_title}&plot=full&apikey={API_KEY}"
                )
                data = {
                    utils.camel_case_split(key): val
                    for key, val in response.json().items()
                }
                serializer = MovieSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        return JsonResponse({"error": "You have to provide film title!"}, status=400)
