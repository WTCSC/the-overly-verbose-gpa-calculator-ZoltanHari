import sys 
import time

def type_out(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

while True:
    grades_input = type_out("Enter all of your grades, separating them with spaces (Ex. 3.2 4.0 2.9): ")
    grades_input = input().split()
    try:
         grades = [float(n) for n in grades_input]
    except ValueError:
        print("Please only enter numbers for grades.")
        continue

    if any(g > 4.0 or g <= 0.0 for g in grades):
        print("Please only enter grades between 0.0 and 4.0.")
        continue
    else:
        gpa = sum(grades) / len(grades)
        tot_gpa = round(gpa, 2)
        half_grades = len(grades_input) // 2
        break

type_out(f"Your GPA for the year is {tot_gpa}")
while True:
    semester = type_out("Which semester would you like to focus on? 1st Semester (first half of classes) or 2nd Semester (second half of classes):")
    semester = input()
    if semester == "1" or semester == "1st":
        fir_gpa = sum(grades[:half_grades]) / len(grades[:half_grades])
        if fir_gpa == tot_gpa:
            type_out("Your GPA for the 1st semester is the same as your GPA for the entire year.")
            break
        elif fir_gpa > tot_gpa:
            type_out(f"Your GPA for the 1st semester of {fir_gpa} is higher than your total gpa")
            break
        elif tot_gpa > fir_gpa:
            type_out(f"Your GPA for the 1st semester of {fir_gpa} is lower than your total GPA")
            break
    elif semester == "2" or semester == "2nd":
        sec_gpa = sum(grades[half_grades:]) / len(grades[half_grades:])
        if sec_gpa == tot_gpa:
            type_out("Your GPA for the 2nd semester is the same as your GPA for the entire year.")
            break
        elif sec_gpa > tot_gpa:
            type_out(f"Your GPA for the 2nd semester of {sec_gpa} is higher than your total gpa")
            break
        elif tot_gpa > sec_gpa:
            type_out(f"Your GPA for the 2nd semester of {sec_gpa} is lower than your total GPA")
            break
    else:
        type_out("Invalid semester choice. Please choose 1 or 2.")
        continue
while True:
    target_gpa_input = type_out("What is your target GPA? ")
    target_gpa_input = input()
    try:
        target_gpa = float(target_gpa_input)
    except ValueError:
        type_out("Please enter a number for your target GPA.")
        continue

    if target_gpa > 4.0 or target_gpa <= 0.0:
        type_out("Please enter a GPA between 0.0 and 4.0.")
        continue
    elif tot_gpa >= target_gpa:
        type_out("You have already met your target GPA!")
        break
    else:
        for i in range(len(grades)):
            new_grade = grades.copy()
            new_grade[i] = 4.0
            new_gpa = sum(new_grade) / len(new_grade)
        if new_gpa == target_gpa:
            type_out(f"Changing grade {i+1} to 4.0 gives you a GPA of {new_gpa:.2f}, which meets your target GPA.")
            break
        elif new_gpa > target_gpa:
            type_out(f"Changing grade {i+1} to 4.0 gives you a GPA of {new_gpa:.2f}, which exceeds your target GPA.")
            break
        else:
            type_out("Changing any single grade to 4.0 will not reach your target GPA.")
            break
