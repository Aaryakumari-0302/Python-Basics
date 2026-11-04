class AI:
    def __init__(self, name, age, city):
        self.name = name 
        self.age = age 
        self.city = city 
    def detail(self):
        print("My name is", self.name)
        print("My age is", self.age)
        print("I lived in", self.city)
ob = AI("Swati",26,"Patna")
ob.detail()