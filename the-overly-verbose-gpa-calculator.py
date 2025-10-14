while True:
    grades_input = input("Enter all of your grades, separating them with spaces: ").split
    try:
        grades = [float(n) for n in grades_input.split()]
    except ValueError:
        print("Please enter only numbers for grades.")
        continue

    if any(g > 4.0 or g <= 0.0 for g in grades):
        print("Please enter grades between 0.0 and 4.0.")
        continue
    else:
        break

print(f"Your GPA is {sum(grades) / len(grades):.2f}")
while True:
    semester = input("Which semester would you like to focus on? (1 or 2): ")
    if semester == 1:
        print(f"Your GPA for semester 1 is {sum(grades[3:]) / len(grades[3:]):.2f}\nYour GPA is {sum(grades[3:]) / len(grades[3:])} - {sum(grades) / len(grades):.2f} compared to your overall GPA.")
        break
    elif semester == 2:
        print(f"Your GPA for semester 2 is {sum(grades[:3]) / len(grades[:3]):.2f}")
        break
    else:
        print("Invalid semester choice. Please choose 1 or 2.")
        continue