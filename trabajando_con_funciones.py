
def doble(n):
   return n*2

class Persona():
    def __init__(self,name,age):

        self.name = name
        self.age = age

luis = Persona ('Luis', 19)
mon = Persona('Mon', 50)

    print (doble(luis.age))