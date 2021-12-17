class Human:
    def __init__(self,name,surname,age,place_of_birth):
        self.name=name
        self.surname=surname
        self.age=age
        self.place_of_birth=place_of_birth

        
    
    def info(self):
        print(f"{self.name} {self.surname} {self.age} {self.place_of_birth}")

p1 = Human("Vlad","Shatrov",17,"UA")
p1.info()



