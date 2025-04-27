students = {"Alice" : {"grade" : 80, "age" : 23}, "Bob" : {"grade" : 70, "age" : 21}, "robert" : {"grade" : 98, "age" : 25}}
students["john"]={"grade" : 97, "age" : 19}
students["Bob"]["grade"]=92
students.pop("Alice")

stud_with_highest_grade = ""
highest_grade = 0
sum = 0
count = len(students)

for key, value in students.items():
    for k, v in value.items():
        if k == "grade":
            sum+=v
            if v > highest_grade:
                highest_grade = v
                stud_with_highest_grade = key
            
print(f"avg is: {sum/count}")
print(f"the student with the highest grade: {stud_with_highest_grade}")