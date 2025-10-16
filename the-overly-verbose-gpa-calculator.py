import sys 
import time

def type_out(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

while True:
    grades_input = type_out("Oi, git! Chuck in all yer gradez, wiv spacez between 'em (Ex. 3.2 4.0 2.9): ")
    grades_input = input().split()
    try:
         grades = [float(n) for n in grades_input]
    except ValueError:
        print("Use numbaz, ya grot! Wot are ya, stoopid?.")
        continue

    if any(g > 4.0 or g <= 0.0 for g in grades):
        print("Da gradez gotta be between 0.0 an' 4.0, or I'll krump ya!")
        continue
    else:
        gpa = sum(grades) / len(grades)
        tot_gpa = round(gpa, 2)
        half_grades = len(grades_input) // 2
        break

type_out(f"Yer total krumpin' average fer da year iz {tot_gpa}")
while True:
    semester = type_out("Wich bit d'ya wanna looksee at? Da furst 'alf or da sekund 'alf (type 1 or 2):")
    semester = input()
    if semester == "1":
        fir_gpa = sum(grades[:half_grades]) / len(grades[:half_grades])
        round_fir_gpa = round(fir_gpa, 2)
        if fir_gpa == tot_gpa:
            type_out("Yer krumpin' average fer da furst 'alf iz da same as da whole zoggin' year.")
            break
        elif fir_gpa > tot_gpa:
            type_out(f"Yer krumpin' average fer da furst 'alf of {round_fir_gpa} is betta dan yer total!")
            break
        elif tot_gpa > fir_gpa:
            type_out(f"Yer krumpin' average fer da furst 'alf of {round_fir_gpa} is rubbish compared ta yer total!")
            break
    elif semester == "2":
        sec_gpa = sum(grades[half_grades:]) / len(grades[half_grades:])
        round_sec_gpa = round(sec_gpa, 2)
        if sec_gpa == tot_gpa:
            type_out(f"Yer krumpin' average fer da sekund 'alf iz da same as da whole zoggin' year.")
            break
        elif sec_gpa > tot_gpa:
            type_out(f"Yer krumpin' average fer da sekund 'alf of {round_sec_gpa} is betta dan yer total!")
            break
        elif tot_gpa > sec_gpa:
            type_out(f"Yer krumpin' average fer da sekund 'alf of {round_sec_gpa} is rubbish compared ta yer total")
            break
    else:
        type_out("Dat's da rong choice, ya git! Pick 1 or 2!")
        continue
while True:
    target_gpa_input = type_out("Wot's da krumpin' average ya wanna get?")
    target_gpa_input = input()
    try:
        target_gpa = float(target_gpa_input)
    except ValueError:
        type_out("Dat 'ent a numba! Put in a proppa one!")
        continue

    if target_gpa > 4.0 or target_gpa <= 0.0:
        type_out("Itz gotta be between 0.0 an' 4.0, ya stoopid git.")
        continue
    elif tot_gpa >= target_gpa:
        type_out("Zog me, you'ze already done it! Dat's proppa kunnin'!")
        break
    else:
        for i in range(len(grades)):
            new_grade = grades.copy()
            new_grade[i] = 4.0
            new_gpa = sum(new_grade) / len(new_grade)
            round_new_gpa = round(new_gpa, 2)
        if new_gpa >= target_gpa:
            type_out(f"If ya change grade numba {i+1} ta a 4.0, ya get {round_new_gpa:.2f}, an' dat stomps all over yer target!")
            break
        else:
            type_out("Zog it! Changin' just wun grade ta 4.0 'ent gonna be enuff.")
            break
