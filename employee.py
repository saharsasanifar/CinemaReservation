from person import *
 
class Employee(Person):
    last_id = 100
    def __init__(self, name, age, email, phone, position):
        super().__init__(name, age, email, phone)
        self.position = position
        self.employee_id = "emp" + str(Employee.last_id)
        Employee.last_id += 1

    def __str__(self):
        return f"{self.employee_id}==> {super().__str__()}, Position: {self.position}"

    def show_info(self):
        print(f"Employee--------\n{self.name}'s Contact Info:\n Email--> {self.email},\n Phone--> {self.phone}")   

    def add_movie(self, movie):
        #self.movies.append(movie)
        pass 
        
    