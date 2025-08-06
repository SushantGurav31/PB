class animal:
    def speak(self):
        print("animal speaks")


class dog(animal):
    def speak(self):   #overloading the parent method 
        print("dog braks")



d = dog()

d.speak()  #output:Dog barks