class Profile:

    def __init__ (self, username, password):
        self.username = username
        self.password = password
        self.favourites = []

    def add_movie(self, new_fave):
        self.favourites.append(new_fave)
        return len(self.favourites)
