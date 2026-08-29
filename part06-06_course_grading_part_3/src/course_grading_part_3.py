# write your solution here


s_input_file = input("Student information: ")
e_input_file = input("Exercises Completed: ")
exam_points = input("Exam points:")
# s_input_file = "src/students1.csv"
# e_input_file = "src/exercises1.csv"
# exam_points = "src/exam_points1.csv"


stud = {}
with open(s_input_file) as sFile:

    for i in sFile: 
        line = i.strip()
        part = line.split(";")

        if part[0] == "id":
            continue

        stud[part[0]] = part[1] + " " + part[2]


# print(stud)

exerc = {}

with open(e_input_file) as eFile:

    for i in eFile:
        line = i.strip()

        part = line.split(";")

        if part[0] == "id":
            continue

        exerc[part[0]] = sum(int (x) for x in part[1:])

# print(exerc)


examPoint = {}
with open(exam_points) as examFile:

    for i in examFile:

        line =  i.strip()
        part = line.split(";")

        if part[0] == "id":
            continue
        examPoint[part[0]] = sum(int (x) for x in part[1:])

# print(examPoint)


x = stud.keys()
y = exerc.keys()
z = examPoint.keys()


examp_and_exerp = {}


for i in y:

    if i in z:
        examp_and_exerp[i] = exerc[i] // 4 + examPoint[i]

# print(examp_and_exerp)



grade = {}

score = 0

for i in examp_and_exerp:

    if examp_and_exerp[i] <= 14:
        score = 0
    elif examp_and_exerp[i] >= 15 and examp_and_exerp[i] <=17:
        score = 1
    elif examp_and_exerp[i] >= 18 and examp_and_exerp[i] <=20:
        score = 2
    elif examp_and_exerp[i] >= 21 and examp_and_exerp[i] <=23:
        score = 3
    elif examp_and_exerp[i] >= 24 and examp_and_exerp[i] <=27:
        score = 4
    elif examp_and_exerp[i] >= 28:
        score = 5

    # print(i)


    grade[i] = score

# print (grade)

print(f'{"name":<30}{"exec_nbr":<10}{"exec_pts.":<10}{"exm_pts.":<10}{"tot_pts.":<10}{"grade":<10}')
for i in stud:
    tot_pts = exerc[i] // 4 + examPoint[i]
    if i in grade.keys():
        print(f'{stud[i]:<30}{exerc[i]:<10}{exerc[i] // 4:<10}{examPoint[i]:<10}{tot_pts:<10}{grade[i]:<10}')
    else:
        print(f"{i} not in file")





