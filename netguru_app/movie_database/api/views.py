from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView

from movie.models import Movie
from .serializer import TopSerializer


@permission_classes((permissions.AllowAny,))
class TopApiView(APIView):
    def get(self, request, datetime_from=None, datetime_to=None):
        if Movie.objects.exists():
            serializer = TopSerializer(datetime_from, datetime_to)
            return JsonResponse(serializer.data, safe=False, status=200)
        return JsonResponse(
            {"error": "No films in database. Populate database first."}, status=400
        )
