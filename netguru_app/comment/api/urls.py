from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path("", csrf_exempt(views.CommentApiView.as_view())),
    path("/<movie_id>", csrf_exempt(views.CommentApiViewForFilm.as_view())),
]
