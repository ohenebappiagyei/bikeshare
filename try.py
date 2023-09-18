# Get and process input for a list of names
names_input = input("Enter a list of student names separated by commas: ")
names = names_input.title().split(',')

# Get and process input for a list of the number of assignments
assignments_input = input("Enter a list of the number of missing assignments separated by commas: ")
assignments = [int(x) for x in assignments_input.split(',')]

# Get and process input for a list of grades
grades_input = input("Enter a list of grades separated by commas: ")
grades = [int(x) for x in grades_input.split(',')]

# Message string to be used for each student
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. Your current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# Iterate through each set of names, assignments, and grades to print each student's message
for name, assignment_count, grade in zip(names, assignments, grades):
    potential_grade = grade + 2 * assignment_count
    print(message.format(name.strip(), assignment_count, grade, potential_grade))
