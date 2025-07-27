# Function to calculate average of two numbers
def calculate_average(a, b):
    return (a + b) / 2

# Calling the function with different values
print("Average of 10 and 20 is:", calculate_average(10, 20))
print("Average of 5 and 7 is:", calculate_average(5, 7))
print("Average of 1.5 and 3.5 is:", calculate_average(1.5, 3.5))






# Function to sort strings alphabetically
def sort_strings(string_list):
    return sorted(string_list)

# List of fruits
fruits = ["apple", "banana", "cherry", "kiwi", "grape"]

# Sorting and printing the result
sorted_fruits = sort_strings(fruits)
print("Sorted list:", sorted_fruits)





# Function to find duplicates in a list
def find_duplicates(lst):
    duplicates = []
    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

# Given list
numbers = [1, 5, 6, 5, 1, 2, 3]

# Finding and printing duplicates
duplicate_items = find_duplicates(numbers)
print("Duplicate elements:", duplicate_items)

