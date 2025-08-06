class cat:
    def sound(self):
        print("meow")



class dog:
    def sound(self):
        print("bark")



# polymorphism in action 
def animal_sound(animal):
    animal.sound()


animal_sound(cat())    #output:meow

animal_sound(dog())    #output:Bark

