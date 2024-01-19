from person import *
from movie import *
from cinema_hall import *
import datetime

class Employee(Person):
    last_id = 100
    def __init__(self, name, age, email, phone, position):
        super().__init__(name, age, email, phone)
        self.position = position
        self.employee_id = "emp" + str(Employee.last_id)
        Employee.last_id += 1
        self.movies_inf = MovieFetcher.fetch_movies()


    def __str__(self):
        return f"{self.employee_id}==> {super().__str__()}, Position: {self.position}"

    def show_info(self):
        print(f"Employee--------\n{self.name}'s Contact Info:\n Email--> {self.email},\n Phone--> {self.phone}")   

    def add_movie(self, movie_name):
        if movie_name in self.movies_inf:
            if movie_name not in CinemaHall.all_movies:
                CinemaHall.all_movies.append(movie_name)
                print("Movie added successfully.")

            else:
                print(f"{movie_name} is already added.")

        else:
            print(f"{movie_name} is not available.")

    def curr_showing(self, movie_name):
        if movie_name in CinemaHall.all_movies: 
            if movie_name not in CinemaHall.movies_showing:
                show_info = {"movie_name" : movie_name, "show_time" : datetime.datetime.now()}
                CinemaHall.movies_showing.append(show_info)
                print("Movie added successfully.")
            else:
                if CinemaHall.movies_showing[movie_name]["show_time"] < datetime.datetime.now():
                    CinemaHall.movies_showing.remove(CinemaHall.movies_showing[movie_name])
                    print("last showing ended")
                else:
                    print(f"{movie_name} is already showing.")

        
    