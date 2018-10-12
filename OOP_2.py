class Tiger():
    state = 'the king of the forest'
    strength = 'so strong'

    def __init__(self,name,age,kind):
        self.name = name
        self.age =age
        self.kind = kind

    def information(self):
        print('This tiger is named {} , it is {} years old , and it belongs to {}.'.format(self.name,self.age,self.kind))

Nor_tiger = Tiger('kika',9,'northest tiger')
Nor_tiger.information()
