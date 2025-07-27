# #dictionary are store data values in keyvalues pairs 
# #the are changeable & don't allow duplicate keys

# dictionary_name = {
#     "key1": "value1",
#     "key2": "value2"
# }




# student = {
#     'key': 'values',
#     "name": "Alice",
#     "age": 25,
#     "department": "CSE",
#     "is_adult":True,
#     "learing":"code",
#     "age":21,
#     'topic':('dic','set'),
#     "subject":[ 'python',"java",'c'],  #list
#     12.6:94.5     
# }
# print(student)
# print(student['name'])
# print(student['topic'])
# print(student["department"])

# #Nested Dictionary 
# info={
#     'Name':"tanzim ahamed",
#     'Subject':{
#         'PHY': 94,
#         'MATH': 89,
#         'CHE':96,  
#     }
   
# }

# #______________-

# #reail life use 
# contacts = {
#     "mom": {"phone": "017xxxxxxxx", "email": "mom@mail.com"},
#     "dad": {"phone": "018xxxxxxxx", "email": "dad@mail.com"}
# }

# print(contacts["mom"]["phone"])  # Output: 017xxxxxxxx




# Write a program to:

# Add 3 students with marks in 3 subjects.

# Store in a nested dictionary.

# Calculate and print average marks for each student.

students={
    
    '101':{
        "name":"Tanzim Ahamed",
        "marks":{"Math":85,"English":78,"Science":90,"Biology":81}
    },
    "102":{
        "name": "Arunima",
        "marks": {"Math": 92, "English": 88, "Science": 95,"Biology":88}

    },
     "103": {
        "name": "Majedul Karim",
        "marks": {"Math": 75, "English": 70, "Science": 80}
    }
    
} 
# Display name and average marks
for student_id, info in students.items():
    name = info["name"]
    marks = info["marks"]
    
    total = sum(marks.values())
    average = total / len(marks)
    
    print(f"ID: {student_id}")
    print(f"Name: {name}")
    print(f"Average Marks: {average:.2f}")
    print("-" * 30)
    