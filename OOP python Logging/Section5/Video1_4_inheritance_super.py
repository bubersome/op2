'''
Created on May 12, 2019
@author: Burkhard A. Meier
'''





#--------------------------------------------------
# Create class 'blue print'
#--------------------------------------------------

class BaseClass():
    
    def __init__(self, name='default'):         # BaseClass now has initializer with default arg
        self.name = name
    
    def print_base(self):
        print('Hello {} from BaseClass'.format(self.name))


class PythonClass(BaseClass):           # inherit from BaseClass
    
    def __init__(self):             
        super().__init__()              # call initializer of Base (super) class

                     
#--------------------------------------------------
# Create instance(s) of class
#--------------------------------------------------

instance = PythonClass()
instance.print_base()                   # call inherited method
























