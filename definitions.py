from enum import Enum

class Car():
    
    def __init__(self, kind, name, age):
        self.kind = kind
        self.name = name
        self.age = age

    def to_dic(self):
        return {
            "kind" : self.kind,
            "name" : self.name,
            "age" : self.age
        }
    
class Actions(Enum):
      PRINT = 1
      ADD = 2
      UPDATE = 3
      DELETE = 4
    
