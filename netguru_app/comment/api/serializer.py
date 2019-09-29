from rest_framework import serializers

from movie.models import Movie
from ..models import Comment


class CommentSerializer(serializers.ModelSerializer):
    # movie_id = serializers.

    class Meta:
        model = Comment
        fields = ("movie", "text")

    # def create(self, validated_data):
    #     movie = validated_data.pop('movie')
    #     return Comment.objects.create(movie=movie, **validated_data)
