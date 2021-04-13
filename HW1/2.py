class Apple:
def __init__(self, type, weight, price):
self.__type = type
self.__weight = weight
self.__price = price
@property
def price(self):
return self.__price
@price.setter
def price(self, price):
if price < 0:
raise ValueError('Apple price must be greater than zero,')
else:
self.__price = price
@property
def weight(self):
return self.__weight
@property
def type(self):
return self.__typr
def __str__(self):
return self.__type + ', ' \
+ "{:.2f}".format(self.__weight) \
+ ', ' + "{:.2f}".format(self.__price)
class Barrel:
def __init__(self, capacity):
self.__list = []
self.__capacity = capacity
@property
def list(self):
return self.__list
@property
def capacity(self):
return self.__capacity
def getTotalWeight(self):
totalWeight = 0.0
for apple in self.list:
totalWeight += apple.weight;
return totalWeight
def addApple(self, apple):
# check if it is over weight
if self.getTotalWeight() + apple.weight > self.capacity:
print("Error! Total weight exceeds the capacity.")
return False
self.list.append(apple)
return True
def __str__(self):
output = 'capacity: ' + "{:.2f}".format(self.capacity) + '\n'
for apple in self.list:
output += str(apple) + '\n'
return output
def main():
print("The Market Test Program")
print()
while True:
capacity = float(input("Enter the capacity of the barrel: "))
barrel = Barrel(capacity)
while True:
type = input("Enter apple type: ")
weight = float(input("Enter apple weight: "))
price = float(input("Enter apple price: "))
apple = Apple(type, weight, price)
barrel.addApple(apple)
choice = input("Add more apples? (y/n): ")
print()
if choice != "y":
print('Your barrel has these apples:')
print(barrel)
break
choice = input("Get another barrel? (y/n): ")
print()
if choice != "y":
print("Bye!")
break

if __name__ == "__main__":
main()