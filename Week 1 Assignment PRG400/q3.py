class Animal:
    def _init_(self,name):
        self.name = name
    
    def spak(self):
        return "Some sound"
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
        
dog = Dog("Buddy")
print(dog.name)
print(dog.speak()) 