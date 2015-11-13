import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, rating, year, starring, wallpaper):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = rating
        self.year = year
        self.starring = starring
        self.wallpaper = wallpaper

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
