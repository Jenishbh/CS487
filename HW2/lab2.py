import random
from typing import ItemsView, get_args

class Customer:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return "Customer: Name="+str(self.__name)


class Product:
    def __init__(self, productID, desc, price):
        self.__productID = productID
        self.__price = price
        self.__desc = desc

    @property
    def productID(self):
        return self.__productID

    @property
    def price(self):
        return self.__price

    @property
    def desc(self):
        return self.__desc

    @price.setter
    def price(self, price):
        self.__price = price

    def __str__(self):
        return "OderItem: Product: productID ="+str(self.__productID)+", desc ="+str(self.__desc)+", price ="+str(self.__price)



class OrderItem:
    def __init__(self, product, qty):
        self.__product = product
        self.__qty = qty

    @property
    def product(self):
        return self.__product

    @property
    def qty(self):
        return self.__qty

    @qty.setter
    def price(self, qty):
        self.__qty = qty

    def __str__(self):
        return "qty="+str(self.__qty)



class Order:
    def __init__(self, orderID,customer ):   # complete parameter list
        self.__orderID = orderID
        self.__orderItems = []
        self.__customer = customer

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        self.__customer = customer

    def getTotal(self):
        Product.price(get_args)
        return self.__getTotal
        


    def addItem(self, item):
        self.__orderItems.append(item)
        return 


    def __str__(self):
        return "Order: OrderID ="+str(self.__orderID)+str(self.__customer)+"\nOrderItem: Product: ProductID="+str(self.__orderItems)





def main():
    cust1 = Customer('Peter')
    cust2 = Customer('Lily')

    prod1 = Product(1000, 'Hammer', 25.5)
    prod2 = Product(2000, 'Book', 125.5)
    prod3 = Product(3000, 'Table', 625.5)

    # First Order
    order1 = Order(random.randint(1000, 2000), cust1) 
    order1.addItem(OrderItem(prod1, 10))
    order1.addItem(OrderItem(prod2, 20))
    order1.addItem(OrderItem(prod3, 30))
    print(order1)

    # Second Order
    order2 = Order(random.randint(1000, 2000),cust2)
    order2.customer = cust2
    order2.addItem(OrderItem(prod1, 15))
    order2.addItem(OrderItem(prod3, 35))
    print(order2)

if __name__ == "__main__": 
    main()




"""
EXPECTED OUTOUT
Order: orderID = 1506
Customer: name = Peter
OrderItem: Product: productID =  1000, desc = Hammer, price = 25.50, qty = 10
OrderItem: Product: productID =  2000, desc = Book, price = 125.50, qty = 20
OrderItem: Product: productID =  3000, desc = Table, price = 625.50, qty = 30
Total = 21530.00

Order: orderID = 1523
Customer: name = Lily
OrderItem: Product: productID =  1000, desc = Hammer, price = 25.50, qty = 15
OrderItem: Product: productID =  3000, desc = Table, price = 625.50, qty = 35
Total = 22275.00
"""
