class person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def details(self):
        # print(f"{self.name} " is "{self.age}" & "{self.city}")
        print(f"{self.name} is {self.age} years old and lives in {self.city}.")


p1 = person("Nahid", 21, "Dhaka")
p1.details()


class Student(person):
    pass


s1 = Student("Nahid", 21, "Dhaka")
s1.details()
