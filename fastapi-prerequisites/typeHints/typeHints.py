from typing import List, Dict

def typeBasic(a : int, b: int) -> int:
    return a + b


def typeListAndDict(names : List['str']) -> Dict['str', 'int']:
    namesDict = {name : len(name) for name in names}
    return namesDict

class Person:
    def __init__(self, name:str, age: int):
       self.name = name
       self.age = age
       
#using custom class
def greet(per: Person):
    print("Hi "+ per.name + " you are "+ str(per.age)+ " old")


#using Optional to indicate value maybe None
from typing import Optional
DB ={1:"Value"}

def getValueFromDb(id: int) -> Optional['str']:
    
    if id not in DB:
        return None
    
    return DB[id]

#Union to specify multiple possible types for a variable.
#here x can be either int or float
from typing import Union
def squareRoot(x :Union['int','float']) -> float:
    return x**0.5
