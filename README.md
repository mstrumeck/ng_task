Movie Database Application based on REST API

Endpoints:
<h2>Movie Endpoints</h2>
- GET /api/movie - shows all movie within database with information<br>
- POST /api/movie - show information about movie based on provided title. App will create an new record in case
when movie with provided title non exist in database. Need 'title' field in request.<br>

<h2>Comments Endpoints</h2> 
- GET /api/comment - provide all comments in database.<br>
- GET /api/comment/<movie_id> - provide all comments related with given film.<br>
- POST /api/comment/<movie_id> - create new comment for given movie. Need 'text' field in request.<br>

<h2>Top Endpoints</h2>
- GET /api/top - provide rankings for all movies within database, based on number of comments.<br>
- GET /api/top/<yyyy-mm-dd> - provide ranking based on comment from given date.<br>
- GET /api/top/<yyyy-mm-dd>/<yyyy-mm-dd> - provide ranking based on comment in given date range.<br>
