'''
Created on Jun 19, 2019
@author: Burkhard A. Meier
'''








class PythonClassNoInit():        
    def get_name_and_items(self):   
        return self.name, self.items
    
    
class PythonClass():   
    def __init__(self, name, items=None):
        self.name = name
        self.items = items
        
    def get_name_and_items(self):   
        return self.name, self.items            # returns a tuple 
        
inst = PythonClass("This is my name")     
print(inst.get_name_and_items())


#inst_no_init = PythonClassNoInit("This is my name")  
inst_no_init = PythonClassNoInit()    
print(inst_no_init.get_name_and_items())






















