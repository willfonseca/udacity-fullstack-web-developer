import webbrowser

class Movie():
    # self is the object that will be created when instantiated
    def __init__(self,
                movie_title,
                movie_storyline,
                poster_image,
                trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url

    # Class method to open a trailer in browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
