class Account:
    def __init__ (self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.profiles = []
    
    def add_profile(self, profile):
        self.favourites.append(profile)
    

    def remove_profile(self, profile):
        self.favourites.remove(profile)
    

    def get_profiles(self):
        return(self.profiles)