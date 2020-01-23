class person:
    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.name = first_name + ' ' + last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18


person1 = person("sambhu","sahoo",19)
print(person1.last_name)
print(person1.full_name)
print(person1.is_above_18)
print(person1.name)