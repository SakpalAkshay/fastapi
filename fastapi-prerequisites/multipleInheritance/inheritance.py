class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getInfo(self):
        print("Name: " + self.name + " Age: " + self.age)

class Boy(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)  # Call the constructor of the parent class
        self.school = school

    def moreInfo(self):
        print("Name: " + self.name + " Age: " + self.age + " School: " + self.school)

boy = Boy("John", "20", "CSUF")
boy.getInfo()
boy.moreInfo()


'''
OutPut - 
Name: John Age: 20
Name: John Age: 20 School: CSUF
'''
