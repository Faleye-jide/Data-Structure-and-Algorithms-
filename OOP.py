'''
Building a class for an organisation
'''

class Animal:

    def __init__(self, name, age, gender, location):
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location


    def set_age(self, value):
        self.age = value

    def get_the_age(self):
        return self.age

    def show(self):
        print("The name of the is {}, he is a {} and has lived for more than {} years".format(self.name, self.gender, self.age))

    def speak(self):
        print("I dont know what to say")

class Cat(Animal):
    def __init__(self,name, age, gender, location, color):
        super().__init__(name, age, gender, location)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"The name of the is {self.name}, he is a {self.gender} and has lived for more than {self.age} years and i am {self.color}")

class Dog(Animal):
    def __init__(self,name, age, gender, location, skin):
        super().__init__(name, age, gender, location)
        self.skin = skin

    def speak(self):
        print("Bark")

    def show(self):
        print(f"The name of the is {self.name}, he is a {self.gender} and has lived for more than {self.age} years and i have {self.skin} skin")


a = Animal("Tim",20,"Male","Essex")
a.show()
c = Cat("Bill",16,"Female","london", "black")
a.set_age(13)
print(a.get_the_age())
d = Dog("Bill",16,"Female","london", "dry")
