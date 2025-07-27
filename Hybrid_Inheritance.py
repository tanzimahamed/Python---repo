
    #     A
    #    / \
    #   B   C
    #    \ /
    #     D


# Base class
class A:
    def feature1(self):
        print("Feature A")

# Class B inherits A
class B(A):
    def feature2(self):
        print("Feature B")

# Class C also inherits A
class C(A):
    def feature3(self):
        print("Feature C")

# Class D inherits both B and C
class D(B, C):
    def feature4(self):
        print("Feature D")

# Object of D
d = D()
d.feature1()  # From A
d.feature2()  # From B
d.feature3()  # From C
d.feature4()  # From D

# Hybrid inheritance a akadik  path thake  inheritance jay.
