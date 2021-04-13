class Math:
    def divide(self, x,y):
        quotient = x // y
        remainder = x % y
        print("Quotiet =", quotient)
        print("Reminder =", remainder)

class Math2:
    def divide(self, x, y):
        quotient = x // y
        remainder = x % y
        return(quotient, remainder)

class Mathadp(Math2):
    def __init__(self, math):
        self.math=math

    def divide(self,x,y):
        quotient = x // y
        remainder = x % y
        print("Quotiet =", quotient)
        print("Reminder =", remainder)
        

        


class Factory:
    def getMath(self):
        math=Math2
        return Mathadp(math)



def main():
    math=Factory().getMath()
    math.divide(5,2)

main()