from person import *
from movie import *
from reservation import*

class User(Person):
    last_id = 100
    def __init__(self, name, age, email, phone):
        super().__init__(name, age, email, phone)
        self.user_id = "user" + str(User.last_id)
        User.last_id += 1
        reservations = []

    def __str__(self):
        return f"{self.user_id}==> {super().__str__()}"
    
    def show_info(self):
        print(f"User\n{self.name}'s Contact Info:\n Email--> {self.email},\n Phone--> {self.phone}")

    def add_reservation(self, movie_name):
        for name in Movie.movies_inf:
            if name.title == movie_name :
                seat_number = input("enter the seats you want :")
                show_time = input("enter the show time you want :")
                re = Reservation(name.imdbid, show time, seat_number,self.name)
                re.Reservation.reserve()
            else:
                print("movie dosent exsist")
    
    def remove_reservation(self, reservation):
        pass
        #self.reservations.remove(reservation)
    

if __name__ == "__main__":
    user = User("John", 25, "johndoe@me.com", "555-555-5555")
    print(user)
    user.display_contact_info()
