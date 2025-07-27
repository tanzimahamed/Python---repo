#Method_Overloading = same method name but diffrent parameter

# class my_Calculator:
#     def product(self,num1,num2):
#         print(num1* num2)
#     def product(self,num1,num2,num3):
#         print(num1* num2 * num3)

# #=======================================
# c1= my_Calculator()
# c1.product(22,34)
# c1.product(33,45,33)  # Outpot : Error
# #=========================================
# # in python can not support drictly Method overloding  

# class my_Calculator:
#     def product(self,*nums):  # Using *args &**kwargs 
#         pro = 2
#         print(nums)
#         for x in nums:
#             pro = pro * x
#         print(pro)    
#     #==================================== 
#     # def product(self,num1,num2=None,num3=None):
#     #     if num1!=None and num2 != None and num3 != None:
#     #         print(num1*num2*num3)
        
#     #     elif num1!= None and num2 != None:
#     #         print(num2*num1)
#     #     else:
#     #         # print( 1* num1)
#     # ========================================    
# c1= my_Calculator()
# c1.product(4)
# c1.product(23,45,56,45,7,8)
# c1.product(3,8,7,9,2,0)   






# In genareal prosses Method overloading in python 

# from functools import singledispatchmethod
# class Greet:
#     def say(self,arg):
#         print("Hello")
#     def say( self,arg:str):
#         print(f"Hello,{arg}")
#     def say(self,arg:int):
#         print(f"Hello number {arg}")
# # create object 
# g= Greet()
# g.say("Tanzim")
# g.say(10)
# g.say(3.1416)            
# 
from functools import singledispatchmethod

class Greet:
    @singledispatchmethod
    def say(self, arg):
        print("Hello!")

    @say.register
    def _(self, arg: str):
        print(f"Hello, {arg}!")

    @say.register
    def _(self, arg: int):
        print(f"Hello number {arg}!")

g = Greet()
g.say("Tanzim Ahamed")   # Hello, Alice!
g.say(10)        # Hello number 10!
g.say(3.14)      # Hello!



