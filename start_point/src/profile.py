class Profile:

    def __init__ (self, username, password):
        self.username = username
        self.password = password
        self.favourites = []

    def add_movie(self, new_fave):
        self.favourites.append(new_fave)
        return len(self.favourites)
    
    # def remove_movieself, (old_fave):
    #     pass
    # input fave to remove
    # remove first film.

    def return_favourites(self, favourites):
        return(self.favourites)
    # if movie is in favourites amend to new list
    # return list
    # 