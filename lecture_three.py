#         # 0 ,1 ,2 ,3  ,4  ,5 ,6
# marks= [ 85,67,90,745,165,65 ,88]  # list sliccing 
#          # -7,-6 ,-5,-4 ,-3 ,2, -1  


# print(marks[3:5])                  #[745,165]
# print(marks[:5])                   # 0 to 5 index 
# print(marks[3:])                   # 3 index to last                   # 
# print(marks[-1:-4])                #[88, 65...........-4 index]






# # Initial list
# numbers = [1, 2, 3, 4, 5, 67]
# print("Initial list:", numbers)


# # 1. append() → Adds one item at the end
# # [1, 2, 3, 4, 5, 67, 100]
# numbers.append(100)
# print("After append(100):", numbers)


# # 2. extend() → Adds multiple elements from another list
# # [1, 2, 3, 4, 5, 67, 100, 200, 300]
# numbers.extend([200, 300])
# print("After extend([200, 300]):", numbers)


# # 3. insert(index, item) → Insert item at specific index
# #[1, 2, 99, 3, 4, 5, 67, 100, 200, 300]
# numbers.insert(2, 99)
# print("After insert(2, 99):", numbers)


# # 4. remove(item) → Removes the first occurrence of item
# # [1, 2, 99, 4, 5, 67, 100, 200, 300]
# numbers.remove(3)
# print("After remove(3):", numbers)

# # 5. pop(index) → Removes and returns item at index (default: last)
# # [1, 2, 99, 4, 5, 67, 100, 200]
# last_item = numbers.pop()
# print("After pop():", numbers)
# print("Popped item:", last_item)  # 300


# # 6. clear() → Removes all items from the list
# #  সম্পূর্ণ লিস্ট খালি করে
# backup = numbers.copy()
# numbers.clear()
# print("After clear():", numbers)


# # Restore list from backup
# numbers = backup.copy()
# print("Restored list:", numbers)

# # 7. index(item) → Finds index of first occurrence
# #  উপাদানের অবস্থান রিটার্ন করে
# index_99 = numbers.index(99)
# print("Index of 99:", index_99)


# # 8. count(item) → Counts number of times item appears
# #  একটি উপাদান কতবার আছে তা গননা করে
# numbers.append(2)
# count_2 = numbers.count(2)
# print("Count of 2:", count_2)


# # 9. sort() → Sorts list in ascending order
# #  ছোট থেকে বড় সাজায়
# numbers.sort()
# print("After sort():", numbers)


# # 10. reverse() → Reverses list
# #  লিস্ট উল্টে দেয়
# numbers.reverse()
# print("After reverse():", numbers)


# # 11. copy() → Copies the list
# #  লিস্টের কপি তৈরি করে
# copy_list = numbers.copy()
# print("Copied list:", copy_list)


# # 12. len() → Length of the list
# #  লিস্টের উপাদান সংখ্যা
# print("Length of the list:", len(numbers))


# # 13. in / not in → Membership test
# #  উপাদান আছে কিনা পরীক্ষা করে
# print("Is 100 in the list?", 100 in numbers)
# print("Is 50 not in the list?", 50 not in numbers)


# list= ['tanzim','Asma','ruhul Amain','Arunima']
# print(list.sort())
# print (list)


# list= [2,1,4,3]
# list.insert(1,7)
# print(list)



# WAP to ask the user to enter of the their 3 fvrt movie & store them in a list 

movies =[]
movies.append(input('Enter the 1st movies:'))
movies.append(input(' Enetr the 2nd movies :'))
movies.append(input('Enter the 3rd movies:'))

print(movies)
