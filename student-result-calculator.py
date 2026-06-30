name=input("enter your name: ")
roll=int(input("enter your roll no: "))
n=int(input("enter the number of subjects: "))
total=0
marks=[]
for i in range (1,n+1):
    num=int(input(f"enter the marks of sub{i}: "))
    marks.append(num)
    total+=num

percent=(total/(n*100))*100
avg=total/n
def grade (percent):
    if percent>90 and percent<=100:
        return "grade A"
    elif percent>80 and percent<=90:
        return "grade B"
    elif percent>70 and percent<=80:
        return "grade C"
    elif percent>60 and percent<=70:
        return "grade D"
    elif percent>50 and percent<=60:
        return "grade E"
    elif percent>100:
        return "error"
    else:
        return "failed"

def highest_marks (mark):    
    highest=0
    for num in mark:
        if num>highest:
            highest=num
    return highest



print("RESULT:-")
print("name: ",name)
print("roll no: ",roll)
print("total marks: ",total)
print(f"percentage: {percent:.2f}%")
print("average: ",avg)
student_grades=grade(percent)
print(student_grades)
high=highest_marks(marks)
print("highest marks among sub is: ",high)