class Student():

    school = 'The science and technology university of Anhui'
    location = 'Huainan city of Anhui province'

    def __init__(self,name,age,hobbit):
        self.name = name
        self.age = age
        self.hobbit = hobbit

    def discription(self):
        print(str(self.name) + 'is a student of ' + __class__.school + ',')
        print('this university is in ' + __class__.location + '.')
        print(self.name + ' is {} years old,'.format(self.age) + 'and his hobbit is ' + self.hobbit + '.')

example = Student('Donan',20,'football')
example.discription()
