class Product:
    # Attribute
    # name = 'Water'
    # quantity = 3
    # price = 8.50

    # Constructor
    def __init__(self, name='Water', quantity=3, price=8.50):
        self.name = name
        self.quantity = quantity
        self.price = price

    # Method
    def hello(self):
        print('สวัสดีคุณลูกค้า Uncle Shop')

class Customer(Product):
    # fullname = ชื่อลูกค้า
    # money = จำนวนเงิน
    def __init__(self, fullname, money, name, quantity, price):
        super().__init__(name, quantity, price)
        self.fullname = fullname
        self.money = money

    def calculate(self):
        self.total = self.quantity * self.price
        self.money -= self.total
        print(f'เหลือเงิน {self.money} บาท')

# ====================================================
# Instance
# product1 = Product('Water', 3, 8.50)
product1 = Product('Coffee', 2, 15)
print(product1.name)
print(product1.quantity)
print(product1.price)
product1.hello()
print('======================================')
product2 = Product('Juice', 5, 20)
print(product2.name)
print(product2.quantity)
print(product2.price)
product2.hello()

# print(type(product1))
# print(type(product2))
print('======================================')
customer1 = Customer('สมชาย สบายดี', 500, 'Water', 2, 8.50)
print(customer1.fullname)
# print(customer1.money)
customer1.calculate()
print('======================================')
customer2 = Customer('สมหญิง จริงใจ', 1000, 'Coffee', 3, 15)
print(customer2.fullname)
# print(customer2.money)
customer2.calculate()
print('======================================')
customer3 = Customer('ลุง วิศวกร', 10000, 'Green Tea', 2, 20)
customer3.calculate()