class Teacher():

    def __init__(self,age,address):
        self.age = age
        self.address = address

    def information(self):
        print(self.age)
        print(self.address)

Lijun = Teacher(45,'Beijing')
Lijun.information()