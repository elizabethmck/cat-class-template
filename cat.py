#Revmoe pass and complete the cat class
class Cat():
    def __init__(self):
        self.name = "Unknown"
        self.age = 0
    
    def speak(self):
        print("Meow")

#Create objects here
#These should NOT be indented inside the class
stella = Cat()
stella.name = "Stella"
stella.age = 7
assert stella.speak() == "Meow"

garfield = Cat()
garfield.name = "Garfield"
garfield.age = 50
assert garfield.speak() == "Meow"
