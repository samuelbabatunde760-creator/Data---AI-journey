# 1. Fixed the name to 'scores'
scores = [85, 78, 92, 66, 74]

first_score = scores[0]
last_score = scores[-1] # Gets 74
new_score = 89

# 2. Add the new score to the list
scores.append(new_score)

# 3. Fixed the math: (Sum of everything) / Total Count
avg = (scores[0] + scores[1] + scores[2] + scores[3] + scores[4] + scores[5]) / 6

print("The first score is:", first_score)
print("The last score is:", last_score)
print("The full list with new score:", scores)
print("The average score is:", avg)

#Loop through the scores
scores = [85, 78, 92, 66, 74, 89]

print("Score Results")

for s in scores:
    if s >= 70:
        result = "Pass"
    else:
        result = "Fail"
    
    print(f"Score: {s} | Result: {result}")

#Dictionaries
student = {
    "name": "Ade",
    "age": 20,
    "scores": [85, 78, 92]
}

#find the average score
score_list = student["scores"]
average_score = sum(score_list)/ len(score_list)

#function to return improvement
def performance(avg):
    if avg >= 80:
        return "Excellent"
    elif 70 <= avg <= 79:
        return "Good"
    else:
        return "Needs improvement"

    
print (f"Student name : {student['name']}")
print (f"The average scoree is : {average_score}")
print (f"The  student performance is : {performance(average_score)}")


#Connect to Day 1
#Taking student dictionary
def student_summary(student_dict):
    name = student_dict["name"]
    age = student_dict["age"]
    scores = student_dict["scores"]

#calculating the average
    avg = sum(scores)/len(scores)

    return f"{name} is {age} years old and has an average score of {avg}"
#Testing
student = {
    "name": "Ade",
    "age": 20,
    "scores": [85, 78, 92]
}

print(student_summary(student))


#Mini Data pipeline
students = [
    {"name": "Ade", "age": 20, "scores": [85, 78, 92]},
    {"name": "Bola", "age": 19, "scores": [68, 74, 70]},
    {"name": "Tunde", "age": 21, "scores": [90, 88, 94]}
]

#Logic fuunction
def performance(avg):
    if avg >= 80:
        return "Excellent"
    elif 70 <= avg <= 79:
        return "Good"
    else:
        return "Needs improvement"
    
#Summary
print("___CLASSROOM SUMMARY___")

for student in students:
    pscore = student["scores"]
    average = sum(pscore)/len(pscore)

    status = performance(average)

    print(f"{student['name']} (Age {student['age']}): Avg = {avg:.1f} | Result: {status}")

total_class_score = 0
total_class_score = total_class_score + average
final_class_avg = total_class_score / len(students)
print("-------------------------")
print(f"THE ENTIRE CLASS AVERAGE IS: {final_class_avg:.1f}")
