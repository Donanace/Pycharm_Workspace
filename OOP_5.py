#类的继承

class People():

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def gender_judge(self):
        if self.gender == 'male':
            gdr = 'he'
        elif self.gender == 'female':
            gdr = 'she'
        return gdr

    def sleep(self):
        gder = self.gender_judge()
        print(self.name.title() + ' works too much and {0} needs sleep .'.format(gder))



class Student(People):

    def work(self):
        gder = self.gender_judge()
        print(self.name.title() + ' is {0} years old and {1} is doing homework .'.format(self.age,gder))

one = Student('xiaoming',15,'male')
two = Student('xiaohong',15,'female')

one.sleep()
two.sleep()

one.work()
two.work()

