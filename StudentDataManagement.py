
# 1
students = {"Alice" : { "age" : 23, "subjects": ["math"], "grades" : {90,82,91}},
             "Bob" : { "age" : 21, "subjects": ["programing","math","english","history"], "grades" : {96,83,72}}, 
             "robert" : { "age" : 26, "subjects" : ["history","programing","arabic"], "grades" : {80,92,71}}}

# 2
students["john"] = { "age" : 29, "subjects": ["arabic","english","history"], "grades" : {95,72,81}}
students["Bob"]["grades"].add(74)
students["Bob"]["grades"].add(83)
students["robert"]["subjects"].pop()

max_avg = 0
student_with_highest_grade = ""
for student, data in students.items():

    grades_list = []
    sum=0

    for grade in data["grades"]:
        grades_list.append(grade)

    for grade in grades_list:
        sum+=grade

    if sum/len(grades_list) > max_avg:
        max_avg = sum/len(grades_list)
        student_with_highest_grade = student

print(f"the student with the highest average grade: {student_with_highest_grade}, \
age: {students[student_with_highest_grade]['age']}, subjects: {students[student_with_highest_grade]['subjects']}")

# 3
listOfTuples = []
for student, data in students.items():
    listOfTuples.append((student,data["age"],len(data["subjects"])))
copyListOfTuples = listOfTuples

for i in range(len(listOfTuples)):
    max_subj_num = 0
    index_of_max = 0
    for i in range(len(listOfTuples)):
        if listOfTuples[i][2] > max_subj_num:
            max_subj_num = listOfTuples[i][2]
            index_of_max = i
    print(listOfTuples[index_of_max])
    listOfTuples.pop(index_of_max)

