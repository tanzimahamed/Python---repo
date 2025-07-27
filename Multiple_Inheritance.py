#A class inherits from more than one parent class.
#   Parent1   Parent2
#       \      /
#        \    /
#         Child
# parent class 1 
class Father:
    def skill1(self):
        print("Father: Driving")

#parent class 2 
class Mother:
    def skill2(self):
        print("Mother: Cooking")
#child class 
class Child(Father, Mother):
    def skill3(self):
        print("Child: Coding")

obj = Child()
obj.skill1()
obj.skill2()
obj.skill3()



