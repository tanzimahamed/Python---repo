# #A while loop runs as long as the condition is True.
# 🧠 Use while when you don’t know beforehand how many times to run.
#x = 1
# while x <= 5:
#     print("x is", x)
#     x += 1


# password = ""
# while password != "1234":
#     password = input("Enter password: ")
# print("Access granted.")



#break is used to immediately exit the current loop, regardless of the condition.
for i in range(1, 10):
    if i == 5:
        break
    print(i)