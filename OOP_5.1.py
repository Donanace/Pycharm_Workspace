#类中函数的调用

class People():

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def gender_judge(self):
        if self.gender == 'male':
            gender_jdg = 'he'
        elif self.gender == 'female':
            gender_jdg = 'she'
        return gender_jdg

    def sleep(self):
        h_s = self.gender_judge() #调用gender_judge()函数，注意调用格式！
        print(self.name.title() + ' works too much and {0} needs sleep .'.format(h_s))

one_example = People('lucy',20,'female')
two_example = People('frank',21,'male')
one_example.sleep()
two_example.sleep()