def gradingStudents(grades):
    # Write your code here
    rounded_grades = []
    
    for grade in grades:
        value_to_add = 5 - (grade % 5)
        
        if grade < 38:
            rounded_grades.append(grade)
        elif grade >= 38 and value_to_add < 3:
            rounded_grades.append(grade + value_to_add)
        else:
            rounded_grades.append(grade)
            
    return rounded_grades
