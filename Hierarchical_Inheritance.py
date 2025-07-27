#Multiple child classes inherit from the same parent.
#         Parent
#        /     \
#    Child1   Child2
class Parent:
    def method1(self):
        print("This is method1 in Parent.")

class Child1(Parent):
    def method2(self):
        print("This is method2 in Child1.")

class Child2(Parent):
    def method3(self):
        print("This is method3 in Child2.")

c1 = Child1()  # create obj in child 1
c1.method1()
c1.method2()

c2 = Child2()  #create obj in child 2
c2.method1()
c2.method3()
