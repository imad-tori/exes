
students = [{"name":"bob", "grades":[10,22,47]},
            {"name":"jack", "grades":[72,93,76]},
            {"name":"frank", "grades":[39,52,99]}]

calc_avg = True
for s in students:

    if len(s["grades"]) == 0:
        print(s["name"]+" has no grades!")
        calc_avg = False

if calc_avg:

    print("\nstudents avg:")
    func = lambda student : [student["name"] , str(round(sum(student["grades"])/len(student["grades"]),2))]
    students_avg_list = list(map(func,students))
    for student in students_avg_list:
        print(student[0], student[1])

    print("\npassed:")
    y = lambda student : float(student[1]) >= 50
    passed = list(filter(y,students_avg_list))
    for student in passed:
        print(student[0], student[1])

    print("\nsorted:")
    x = lambda student : student[1]
    print(sorted(students_avg_list,key=x,reverse=True))


print("\nIncrease each student's grade by 5 points:")
z = lambda student : [student["name"] , [x+5 for x in student["grades"]]]
inc_list=list(map(z,students))
for student in inc_list:
    for i in range(len(student[1])):
        if student[1][i]>100:
            student[1][i] = 100
print(inc_list)

# 6

list_of_tuples = [tuple(x) for x in students_avg_list]
print("list of tuples: ",list_of_tuples)
max_grade=0
t = lambda student : [student["name"] , max(student["grades"])]
x = lambda student : student[1]
print("The student who achieved the highest grade:",sorted(list(map(t,students)),key=x,reverse=True)[0])
