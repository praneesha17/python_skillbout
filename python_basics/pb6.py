from grade import cal_avg, stu_grade, tot, validate_marks
name=input("Enter student name:")
marks=list(map(int,input("Enter marks: ").split()))
if not validate_marks(marks):
    print("All marks are in between 0 and 100")
else:
    print("Student name:",name)
    print("Marks:",marks)
    print("Average marks:",cal_avg(marks))
    print("Student grade:",stu_grade(cal_avg(marks)))