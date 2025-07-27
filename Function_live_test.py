
def hours_to_minutes(hours):
    return hours * 60

# user input
hour_input = float(input("Enter number of hours: "))

result = hours_to_minutes(hour_input)
print(f"{hour_input} hour(s) = {result} minute(s)")

