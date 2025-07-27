#Basic Syntex:
#for Item in sequence:



# List r opor for loop 
# fruits =["apple ","banana","cherry"]
# for fruit in  fruits:
#     print(fruit)


#str r opor loop 
# name = "Tanzim Ahamed "    
# for chr in name :
#     print(chr)

#Number with range 
# for i in range(4,10,2):  #(start ,stop ,step )
#     print(i)    


#loop through dictionary 
# student= {'name ': "Tanzim",'Age':20,"marks":98}
# for key in student:
#     print(key, ":",student[key])



#Even / odd number _ loop use 
# for i in range(1,20):    
#     if i % 2==0:
#         print(i , "is Even ")
#     else:
#         print(i , "is Odd")    

#Nested loop 

# for i in range(1,10):
#     for j in range(1,4):
#         print(i,"*",j,"=",i*j)
#     print("----------")     



# Break = loop off kore day 
for i in range(1,10 ):
    if i == 5: #jekhane i=5 pabe tokhon loop off kore dibe  
        break
    print(i)


# Continue - skip kore cole jay 
for j in range(1,10):
    if j == 5:   # 5 skip kore cole jabe 
        continue
    print(j)    
   