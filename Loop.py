# #A for loop is used to iterate (loop) over a sequence like a list, tuple, dictionary, string, or range.
# syntex:for variable in sequence:
#     # loop body


fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit.capitalize())


for i in range(1, 6):    # 1 to 5
    print("Counting:", i)


for i in range(2, 10, 2):    #range(start, stop, step)
    print(i)                 # 2, 4, 6, 8
