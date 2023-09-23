# Used two different class to get their properties

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def getInfo(self):
        print("Name: "+ self.name + " Age: "+ self.age)

class Football:
    
    def __init__(self):
        pass
    
    def playsFootball(self):
            print("Boy Play football")
    
class Boy(Person,Football):
    def __init__(self,name,age,school):
        super().__init__(name,age)
        self.school = school

    
    def moreInfo(self):
        print("Name: "+ self.name + " Age: "+ self.age + " School: "+ self.school)
        
        

boy = Boy("Joh","20","CSUF")
boy.getInfo()
boy.moreInfo()
boy.playsFootball()
