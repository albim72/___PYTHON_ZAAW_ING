from dataclasses import dataclass, Field
from datetime import datetime

#Field - 'default', 'default_factory', 'init', 'repr', 'hash','compare', 'metadata','kw_only'
params = {
    'firstname':Field(None,None,True,True,True,True,None,None),
    'lastname':Field(None,None,True,True,True,True,None,None),
    'year_of_birth':Field(None,None,True,True,True,True,None,None)
}

def age(self):
    return datetime.now().year - self.year_of_birth

MetaPerson = dataclass(type('MetaPerson',(),{'__annotations__':params,'age':property(age)}))


p = MetaPerson('Romulada','Tracz',1954)
print(p)
print(p.age)
