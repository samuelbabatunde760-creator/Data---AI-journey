def age_category(years):
    if years < 0:
        return "Invalid Age"
    if years < 13:
        return "Child"
    elif 13 <= years <= 19:
        return "Teen"
    else:
        return "Adult"

# Testing it out
my_age = 16
print(f"Result for {my_age}: {age_category(my_age)}")
