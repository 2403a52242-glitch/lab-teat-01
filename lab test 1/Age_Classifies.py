def classify_age(age):
    if age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <= 19:
        return "Teen"
    elif age >= 20 and age <= 59:
        return "Adult"
    elif age >= 60:
        return "Senior"
    else:
        return "Invalid age"

# Example usage:
age = int(input("Enter age: "))
group = classify_age(age)
print(f"Age group: {group}")