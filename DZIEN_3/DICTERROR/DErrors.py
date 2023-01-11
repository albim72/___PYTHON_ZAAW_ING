class IntFloatValueError(Exception):
    def __init__(self,value):
        self.value = value
        
    def __str__(self):
        return f'zadana wartość: {self.value} jest niewłaściwa. Akceptowalne są tylko wartości w typie ' \
               f'int i float.'
    
class KeyValueConstructError(Exception):
    def __init__(self,key,value):
        self.key = key
        self.value = value
        
    def __str__(self):
        return f'klucze i wartości możemy przekazać tylko za pomocą krotek i list\n, ' \
               f'klucze {self.key} są w typie {type(self.key)}\n,' \
               f'wartości {self.value} są w typie {type(self.value)}\n'
