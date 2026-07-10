def grade(percent):
    if 90 < percent <= 100:
        return "A"
    elif 80 < percent <= 90:
        return "B"
    elif 70 < percent <= 80:
        return "C"
    elif 60 < percent <= 70:
        return "D"
    elif 50 < percent <= 60:
        return "E"
    elif percent > 100:
        return "error"
    else:
        return "failed"

def highest_marks (mark):    
    highest=mark[0]
    for num in mark:
        if num>highest:
            highest=num
    return highest

def display (name,roll,total,percent,avg,student_grades,high,marks):
    print("="*35)
    print("       RESULT:-")
    print("="*35)
    print(f"{'name':15}: {name}")
    print(f"{'roll no':15}: {roll}")
    print(f"{'total marks':15}: {total}")
    print(f"{'percentage':15}: {percent:.2f}%")
    print(f"{'average':15}: {avg:.2f}")
    
    print(f"{'grade':15}: {student_grades}")
    print(f"{'highest marks':15}: {high}")
    print(f"{'lowest marks':15} {min(marks)}")
    print("="*35) 

def display_marks (marks,subjects,n):
    print("="*35)
    for i in range (n) :
        print(f"marks in {subjects[i]} :{marks[i]} ")
    print("="*35)

name=input("enter your name: ")
roll=input("enter your roll no: ")
n=int(input("enter the number of subjects: "))
subjects = []

for i in range(n):
    subject = input(f"Enter the name of subject {i+1}: ")
    subjects.append(subject)

total=0
marks=[]
for i in range (1,n+1):
    while True:
        num = int(input(f"enter the marks of sub{i}: "))

        if 0 <= num <= 100:
            break

        print("Invalid input! Marks should be between 0 and 100.")

    marks.append(num)
    total+=num

percent=(total/(n*100))*100
avg=total/n
student_grades=grade(percent)
high=highest_marks(marks)
#display(name,roll,total,percent,avg,student_grades,high)
print("1. display result ")
print("2. display highest marks")
print("3. display marks of each sub")
choise=int(input("enter no of your choise: "))
match choise:
    case 1 :
        display(name,roll,total,percent,avg,student_grades,high,marks)
    case 2:
        print(f"{'highest marks':15}: {high}")
    case 3:
        display_marks(marks,subjects,n)
    case _:
        print("no correct choise! ")

