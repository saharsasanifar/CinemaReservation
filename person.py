from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, email, phone):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

    @abstractmethod
    def show_info(self):
        pass

    def __str__(self):
        return f"Name: {self.name},Contact Info: {self.email}, {self.phone}"
    
    def edit(self, n_name=None, n_email=None, n_phone=None, n_age=None):
        self.name = n_name or self.name
        self.email = n_email or self.email
        self.phone = n_phone or self.phone
        self.age = n_age or self.age

