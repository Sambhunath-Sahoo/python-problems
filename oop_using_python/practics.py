class laptop:
    discount_percentage = 10
    def __init__(self, name, model,price):
        self.name = name
        self.model = model
        self.price = price

     def discount(self):
        amount = (laptop.discount_percentage/100)*self.price
        return self.price - amount

laptop1 = laptop("asus","x510u",49000)
print(laptop1.model)
print(laptop1.discount(24))
