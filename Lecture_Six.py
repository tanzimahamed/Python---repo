#A function is a block of reusable code that performs a specific task. It helps to make your code organized, reusable, and easy to understand.

# Built-in Functions – যেমন: print(), len(), sum(), range()
# User-defined Functions – আপনি নিজে বানান, যেমন:

#syntex:
# def function_name(parameters):
#     # code bloc

#_______________________
# def greet(name):
#     print("Hello,", name)

# greet("Tanzim")

#_____________________________
def student_info(name, age, dept):
    print("Name:", name)
    print("Age:", age)
    print("Department:", dept)

student_info("Tanzim", 20, "ICE")



#_______________________
def calc_sum(a ,b ):
    add= a+b
    sub= a-b
    mul= a*b
    dev= a/b
    #print(add,sub,mul,dev)
    return add,sub,mul,dev



calc_sum(23,8)

calc_sum(7,8)


