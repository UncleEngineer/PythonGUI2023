from basicclass1 import Product

class StaticClass:
    def run():
        print('นี่คือเมธอด static')

if __name__ == '__main__':
    product = Product('กระทิงแดง', 2, 10)
    print(product.name)
    print(product.quantity)
    print(product.price)

    StaticClass.run()