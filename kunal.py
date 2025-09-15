class Employee:
    def __init__ (self, id, name, age, sal):
        self.id = id
        self.name = name
        self.age = age
        self.sal = sal

    def show(self):
        print("id:", self.id)
        print("name:", self.name)
        print("age:",self.age)
        print("sal:", self.sal)

obj = Employee( 102, "kunal", 25, 80000)
print(obj.show())


