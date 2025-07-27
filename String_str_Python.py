#single-line str 
s1= 'hello'
s2= 'world'
# multi-line str
s3= '''Multi-line str'''

#python str are indexed ,starting from 0 & -1
text= 'Python'
print(text[0])    # P
print(text[-1])   # n last character



# Str Slicing 
s= "Hello , Python"
print(s[0:5])   # Hello
print(s[:5])    # Hello

print(s[7:])    #Python
print(s[3:5])   #lo
print(s[-6:])   # Python  


# Strings in Python are immutable — cannot be changed after creation.


s = "Python"
# s[0] = 'J'  # Error: strings are immutable
s = "Jython"  # Reassigning creates a new string


a = "Hello"
b = "World"

print(a + " " + b)     # Hello World
print(a * 3)           # HelloHelloHello

# Str-Method 

#upper() / lower() / title() / capitalize()-str method
s = "hello world"
print(s.upper())       # HELLO WORLD
print(s.lower())       # hello world
print(s.title())       # Hello World
print(s.capitalize())  # Hello world



#strip() / lstrip() / rstrip()-str mrthod 
s = "  Hello  "
print(s.strip())       # "Hello"
print(s.lstrip())      # "Hello  "
print(s.rstrip())      # "  Hello"


# replace()-str method 
s = "banana"
print(s.replace("a", "o"))  # bonono



#find() / index()
s = "Python is awesome"
print(s.find("is"))    # 7
# print(s.index("java"))  # ValueError


#startswith() / endswith()
s = "Python"
print(s.startswith("Py"))  # True
print(s.endswith("on"))    # True



#Reversing a String
s = "Python"
print(s[::-1])  # nohtyP

#Palindrome Check
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # True


# str- comparison
a = "apple"
b = "banana"

print(a == b)    # False
print(a < b)     # True (lexicographic order)


# isX String Methods
# Method	    Description
# isalpha()-	Only letters
# isdigit()-	Only digits
# isalnum()-	Letters and digits
# isspace()-	Only whitespace
# islower()-	All lowercase
# isupper()-	All uppercase

s = "123"
print(s.isdigit())  # True



# Str- splitting & Joining
s = "one,two,three"
parts = s.split(",")
print(parts)          # ['one', 'two', 'three']

joined = "-".join(parts)
print(joined)         # one-two-three




