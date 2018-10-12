class Dog():

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+ " is sitting now.")

    def roll_over(self):
        print(self.name.title()+ " rolled over!")

my_dog = Dog('Kiki',4)
print(my_dog.name)
my_dog.sit()
my_dog.roll_over()
