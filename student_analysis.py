students = [
{"name": "Aarav", "Python": 85, "SQL": 78, "Maths": 90},
{"name": "Priya", "Python": 92, "SQL": 88, "Maths": 95},
{"name": "Rahul", "Python": 65, "SQL": 70, "Maths": 60},
{"name": "Sneha", "Python": 80, "SQL": 85, "Maths": 82},
{"name": "Rohan", "Python": 75, "SQL": 72, "Maths": 68}
]

print("STUDENT PERFORMANCE ANALYSIS")
print("-" * 40)

total_class_marks = 0

for student in students:
    total = student["Python"] + student["SQL"] + student["Maths"]
    percentage = total / 3

    print("\nStudent:", student["name"])
    print("Total Marks:", total, "/ 300")
    print("Percentage:", round(percentage, 2), "%")

    if percentage >= 75:
        print("Result: Excellent")
    elif percentage >= 60:
        print("Result: Good")
    elif percentage >= 40:
        print("Result: Pass")
    else:
        print("Result: Needs Improvement")

    student["Total"] = total
    student["Percentage"] = percentage

    total_class_marks += total

topper = max(students, key=lambda student: student["Total"])

class_average = total_class_marks / len(students)

print("\n" + "-" * 40)
print("CLASS AVERAGE:", round(class_average / 3, 2), "%")
print("TOPPER:", topper["name"])
print("TOPPER PERCENTAGE:", round(topper["Percentage"], 2), "%")

print("\nSUBJECT AVERAGES")

for subject in ["Python", "SQL", "Maths"]:
 average = sum(student[subject] for student in students) / len(students)
print(subject, "Average:", round(average, 2))
