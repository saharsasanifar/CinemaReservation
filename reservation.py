from cinema_hall import *
class Reservation:
    last_id =1000
    def __init__(self, movie_id, showtime, seat_number, user_name):
        self.reservation_id = "reserv" + str (User.last_id)
        self.reservation_id = reservation_id
        self.movie_id = movie_id
        self.showtime = showtime
        self.seat_number = seat_number
        self.user_name = user_name
        self.movie_reserved = {}
        User.last_id +=1

    def __str__(self):
        return f"dear {self.user_name} you reserved {self.movie_id} that will show at {self.showtime} with reservation id {self.reservation_id}"

    def reserve(self):
        if CinemaHall.use_seats:
            if CinemaHall.flag == True:
                self.movie_reserved[self.movie_id] = [self.reservation_id, self.showtime, self.seat_number,self.user_name]
            else:
                print("sorry we dont have enough seats!")
        else:
            print("first please check the number of seats...")

                