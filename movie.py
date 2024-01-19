import requests
class Movie :
    def __init__(self, id_, title, genere, rating, relesed, status):
        self.id_ = id_
        self.title = title
        self.genre = genere
        self.rating = rating
        self.relesed= relesed
        self.status = status
        self.feedback_list = []
        self.movies_inf = MovieFetcher.fetch_movies()


    def __str__(self):
        return f"movie with id number {self.id_} and title {self.title} rates : {self.rating} shows at {self.relesed}"

class MovieFetcher :
    url = "https://ott-details.p.rapidapi.com/advancedsearch"

    @staticmethod
    def fetch_movies():
        querystring = {"start_year":"1970","end_year":"2020","min_imdb":"6","max_imdb":"7.8","genre":"action","language":"english","type":"movie","sort":"latest","page":"1"}
        headers = {
        "X-RapidAPI-Key": "9e176df3b7msh28d79fe9e950efcp157193jsnd17436aa80c3",
        "X-RapidAPI-Host": "ott-details.p.rapidapi.com"
        }
        response = requests.get(MovieFetcher.url, headers=headers, params=querystring)
        if response.status_code == 200:
            movies = response.json().get("results")
        else:
            print("Failed to fetch data from API!")
        
        movies_list = []
        for mov in movies :
            movie = Movie(
                mov.get('imdbid','No Id'),
                mov.get('title', 'No Title'),
                mov.get('genre', 'No genere'),
                mov.get('imdbrating' ,'No rating'),
                mov.get('released','No time released'),
                mov.get('synopsis', 'No Discription')
            )
            movies_list.append(mov)
        return movies

if __name__ == "__main__":
    movie = MovieFetcher()
    movie.fetch_movies()