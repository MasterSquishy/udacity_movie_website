import webbrowser

<<<<<<< HEAD

class Movie():

    """
    Attributes:
        title (str): Title of movie
        storyline (str): Short plot summary
        poster_image_url (str): URL to movie poster
        trailer_youtube_url (str): URL to youtube trailer (MUST BE YOUTUBE)
        rating (str): MPAA rating
        year (str): Year of movie release
        starring (str): 3 to 4 starring actors -- separated by commas
        wallpaper (str): URL to movie wallpaper
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, rating, year, starring, wallpaper):
=======
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, rating, year, starring, wallpaper):
>>>>>>> 77f55fd32f997edad424c6aa19b1509672636072
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = rating
        self.year = year
        self.starring = starring
        self.wallpaper = wallpaper
<<<<<<< HEAD
=======

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
>>>>>>> 77f55fd32f997edad424c6aa19b1509672636072
