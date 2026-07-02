def grade (percent):
    if percent>90 and percent<=100:
        return "A"
    elif percent>80 and percent<=90:
        return "B"
    elif percent>70 and percent<=80:
        return "C"
    elif percent>60 and percent<=70:
        return "D"
    elif percent>50 and percent<=60:
        return "E"
    elif percent>100:
        return "error"
    else:
        return "failed"

def highest_marks (mark):    
    highest=mark[0]
    for num in mark:
        if num>highest:
            highest=num
    return highest

name=input("enter your name: ")
roll=input("enter your roll no: ")
n=int(input("enter the number of subjects: "))
total=0
marks=[]
for i in range (1,n+1):
    num=int(input(f"enter the marks of sub{i}: "))
    marks.append(num)
    total+=num

percent=(total/(n*100))*100
avg=total/n
print("="*35)
print("       RESULT:-")
print("="*35)
print(f"{'name':15}: {name}")
print(f"{'roll no':15}: {roll}")
print(f"{'total marks':15}: {total}")
print(f"{'percentage':15}: {percent:.2f}%")
print(f"{'average':15}: {avg:.2f}")
student_grades=grade(percent)
print(f"{'grade':15}: {student_grades}")
high=highest_marks(marks)
print(f"{'highest marks':15}: {high}")
print(f"{'lowest marks':15} {min(marks)}")
print("="*35)