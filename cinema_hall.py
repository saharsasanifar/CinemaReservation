class CinemaHall :
    def __init__(self, name, total_seats, movies_showing) :
        self.name = name 
        self.total_seats = total_seats
        self.movies_showing = []
        self.employees = []
        self.flag = False
    def __str__(self):
        return f"the cinema {self.name} with total seats {self.total_seats} shoe this movies : {self.movies_showing}"

    def use_seats(self,num_seats):
        if self.total_seats >= num_seats :
            self.total_seats -= num_seats
            print(f"task managed ,the number of seats that exsist : {self.total_seats}")
            self.flag = True
        else :
            print(f"we dont have enough seats,the number of seats is {self.total_seats}")
            self.flag = False
            
    def show_employee(self):
        for employee in Employee.employees.values() :
            print (f"employee {employee.id} with positoin {employee,positoin}") 