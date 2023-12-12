class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print(f'The dog with name {self.name} is barking')
    
    def sit(self):
        print(f'{self.name} sit')
        
        
        
my_dog = Dog("Rex", 6)
my_dog.bark()
my_dog.sit()
        