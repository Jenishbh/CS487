class someobject:
    def __init__(self,name):
        self.name=name
    
    def act(self):
        print(self.name, "can act")
    
    def fly(self):
        print(self.name, "is Flying")

class decorector:
    def __init__(self, someobject):
        self.someobject=someobject

    def act(self):
        print("Decorated", end=" - ")
        self.someobject.act()

    def run(self):
        print(self.someobject.name, "is Run")

def main():
        obj=someobject("peter")
        obj.act()
        obj.fly()

        obj=decorector(obj)
        obj.act()
        obj.run()
main()



