# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-2)

# show(20)



def print_list(list,indx=0):
    if(indx==len(list)):
        return
    print(list(indx))
    print_list(list,indx+1)

fruits=["mango","litchi","apple","banana"]

print_list(fruits)