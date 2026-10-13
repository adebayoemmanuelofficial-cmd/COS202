prev_cgpa = float(input("Previous CGPA (0 if none): "))
prev_units = int(input("Previous total units (0 if none): "))
n = int(input("Number of courses this semester: "))

units_sum = 0
points_sum = 0
i = 1

while i <= n:
    print("Course", i)
    units = int(input("Units: "))
    score = float(input("Score (0-100): "))

    if score < 0 or score > 100:
        print("Score must be between 0 and 100, try again")
        continue

    if score >= 70:
        grade = "A"
        point = 5
    elif score >= 60:
        grade = "B"
        point = 4
    elif score >= 50:
        grade = "C"
        point = 3
    elif score >= 45:
        grade = "D"
        point = 2
    else:
        grade = "F"
        point = 0

    print("Grade:", grade)
    units_sum = units_sum + units
    points_sum = points_sum + units * point
    i = i + 1

if units_sum == 0:
    print("No courses entered")
else:
    gpa = points_sum / units_sum
    cgpa = (prev_cgpa * prev_units + points_sum) / (prev_units + units_sum)
    print("GPA:", round(gpa, 2))
    print("CGPA:", round(cgpa, 2))

    if cgpa >= 4.5:
        print("Class: First Class")
    elif cgpa >= 3.5:
        print("Class: Second Class Upper")
    elif cgpa >= 2.4:
        print("Class: Second Class Lower")
    elif cgpa >= 1.5:
        print("Class: Third Class")
    else:
        print("Class: Pass or Fail, see your adviser")