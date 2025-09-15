class company:
    companyname = "IBM"
    def __init__(self,id,name,city):
        self.id = id
        self.name = name
        self.city = city

    def show(self):
        print("company name :",company.companyname)
        print("ID:",self.id)
        print("name:",self.name)
        print("city:",self.city)
    @classmethod
    def companyname_change(cls):
        cls.companyname ="INFOSYS"

obj = company(101,"Tejas","pune")
obj.show()
company.companyname_change()
obj.show()