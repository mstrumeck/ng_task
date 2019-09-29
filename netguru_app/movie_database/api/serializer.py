from ranking import Ranking, DENSE

from movie.models import Movie


class TopSerializer:
    def __init__(self, datetime_from, datetime_to):
        self.datetime_from = datetime_from
        self.datetime_to = datetime_to
        self.data = []
        self._create_data()

    def _create_data(self):
        movies = Movie.objects.all()
        self._create_list_of_movies_with_comments(movies)
        self._sort_by_number_of_comments()
        self._add_rank()

    def _create_list_of_movies_with_comments(self, movies):
        self.data = [
            {"movie_id": m.id, "comments": self._get_movie_comments(m)} for m in movies
        ]

    def _get_movie_comments(self, movie):
        if self.datetime_from:
            return movie.comment_set.filter(created__gt=self.datetime_from).count()
        elif self.datetime_from and self.datetime_to:
            return movie.comment_set.filter(
                created__range=[self.datetime_from, self.datetime_to]
            ).count()
        return movie.comment_set.count()

    def _sort_by_number_of_comments(self):
        self.data = sorted(self.data, key=lambda t: t["comments"], reverse=True)

    def _add_rank(self):
        for movie, rank in zip(self.data, self._get_ranking_for_movies()):
            movie["rank"] = rank[0]

    def _get_ranking_for_movies(self):
        return list(
            Ranking([m["comments"] for m in self.data], start=1, strategy=DENSE)
        )
