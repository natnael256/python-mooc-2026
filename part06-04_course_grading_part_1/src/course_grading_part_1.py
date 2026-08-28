# write your solution here

file_name_student_info =  input("Student informatin: ")
file_name_exercises_completed = input("Exercises completed: ")
# file_name_student_info = "src/students1.csv"
# file_name_exercises_completed  = "src/exercises1.csv"
stud = {}

exercise = {}



with open(file_name_student_info) as new_file:

    for i in new_file:
        line = i.strip()
        part = line.split(';')
        if part[0] == "id":
            continue
        stud[part[0]] = (part[1]) + " " + (part[2])


# print(stud)


with open(file_name_exercises_completed) as new_file: 

    for i in new_file:

        line = i.strip()

        part = line.split(';')

        if part [0] == "id":
            continue
        exercise[part[0]] = sum(int(x)for x in part[1:8])
    # print (part)
# print(exercise)
x = stud.keys()
y = exercise.keys()



for i in x:
    if i in exercise.keys():
        print(f"{stud[i]} {exercise[i]}")
    else:
        print(f"{i} not in file")


