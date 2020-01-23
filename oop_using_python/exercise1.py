class laptop:
    def __init__(self, name, model,price):
        self.name = name
        self.model = model
        self.price = price

laptop1 = laptop("asus","x510u",49000)
print(laptop1.model)
