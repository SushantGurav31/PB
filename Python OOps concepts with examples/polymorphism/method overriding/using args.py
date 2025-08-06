class calculator:
    def add(self, *args):
        return sum(args)
    

calc = calculator()

print(calc.add(5))                  #output:5

print(calc.add(1, 2, 3))            #outpit:6

print(calc.add(10, 20, 30))         #output:60

