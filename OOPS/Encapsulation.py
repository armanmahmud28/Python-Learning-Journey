class person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age is not valid")


p1 = person("Nahid", 25)

print(p1.name, "is", p1.get_age())   # prints 25

p1.set_age(21)

print("NO!", p1.get_age())   # prints 21
