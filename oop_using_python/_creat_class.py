#init methode/constructor
class person:
    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

person1 = person("sambhu","sahoo",19)
print(person1.last_name)
