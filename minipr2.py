s =int(input("enter number of student: "))
students =[]
for i in range(s):
    name =input("enter student name: ")
    mark1 =float(input("enter mark of sub 1: "))
    mark2 =float(input("enter mark of sub 2: "))
    mark3 =float(input("enter mark of sub 3: "))
    total =mark1+mark2+mark3
    avg =total/3
    if avg>=90:
        grade ="A"
    elif avg>=75:
        grade ="B"
    elif avg>=65:
        grade ="C"
    elif avg>=45:
        grade ="E"
    else:
        grade ="F"

    student ={
        "name":name,
        "marks":[mark1,mark2,mark3],
        "total":total,
        "avg":avg,
        "grade":grade
    }
    students.append(student)
print("ALL STUDENT RESULT")
for s in students:
    print(f"\nName: {s['name']}")
    print(f"Marks: {s['marks']}")
    print(f"Total: {s['total']}")
    print(f"Avg: {s['avg']}")
    print(f"Grade: {s['grade']}")
    search_name =input("enter student name to search: ") 
    found = False
for s in students:
    print(f"\nName: {s['name']}")
    print(f"Marks: {s['marks']}")
    print(f"Total: {s['total']}")
    print(f"Avg: {s['avg']}")
    print(f"Grade: {s['grade']}")
    found = True
    break
if not found:
    print("student not found!")


