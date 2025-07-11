def tot(marks):
    return sum(marks)
def cal_avg(marks):
    return tot(marks)//len(marks)
def stu_grade(avg):
    if (avg>=90 and avg<=100):
        return "A+"
    elif (avg>=80 and avg<90):
        return "A"
    elif (avg>=70 and avg<80):
        return "B"
    elif (avg>=60 and avg<70):
        return "C"
    elif (avg>=50 and avg<60):
        return "D"
    else:
        return "F"
def validate_marks(marks):
    return all(0 <= mark <= 100 for mark in marks)