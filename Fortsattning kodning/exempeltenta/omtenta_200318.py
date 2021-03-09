##2

def funkis (str):    
    if str:        
        print(str)        
        no_funkis (str[1:])
        
def no_funkis (str):    
    if str:        
        funkis (str[1:])        
        print(str)

funkis("Hello")
print()
no_funkis("Helllo")


""" ##8

class Product:
    def __init__(self,name,stock,price):
        self.name = name
        self.stock = stock 
        self.price = price

    def prod_info(self):
        return '%-5s %-5s %-5s' % (self.name,self.stock,self.price)

    def get_stock(self):
        return self.stock

    def set_stock(self, stock):
        self.stock = stock

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

prod1 = Product("Bok", 120, 200)

prod1.set_stock(300)
prod1.set_price(2000)

print(prod1.get_stock())
print(prod1.get_price())

print(Product.prod_info(prod1)) """