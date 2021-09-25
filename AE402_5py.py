class Person():
    def __init__(self,name,age,weight,height):
        self.name = name
        self.age =  age
        self.weight = weight
        self.height = height
    def BMI(self):
        result = self.weight/self.height**2
        return result
class Boy(Person):
    def __init__(self,name,age,weight,height,sex):
        super().__init__(name,age,weight,height)
        self.sex = sex
name = input("what is your name")
age = int(input('how old are you'))
weight = int(input("Weight?"))
height = int(input('height'))
a = Boy(name,age,weight,height,"Male")
print("Your name is",a.name)
print("Yout age is =",a.age)
print("Your BMI is =",a.BMI())
print("your sex is ",a.sex)


    