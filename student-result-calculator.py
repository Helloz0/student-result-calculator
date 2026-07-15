def grade(percent):
    if percent > 100:
        return "Error"
    elif percent >= 90:
        return "A"
    elif percent >= 80:
        return "B"
    elif percent >= 70:
        return "C"
    elif percent >= 60:
        return "D"
    elif percent >= 50:
        return "E"
    else:
        return "Failed"

def highest_marks (mark):    
    highest=mark[0]
    for num in mark:
        if num>highest:
            highest=num
    
    return highest

def display_highest_lowest (high,marks):
    print(f"{'highest marks':15}: {high}")
    print(f"{'lowest marks':15} {min(marks)}")


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
for i in range (n):
    while True:
        try:
            num = int(input(f"Enter marks of {subjects[i]}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

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
print("4. display the highest and lowest marks ")
print("5. log out")


while True :
    choice=int(input("enter no of your choice: "))
    if choice==1:
        display(name,roll,total,percent,avg,student_grades,high,marks)
    elif choice==2:
        print(f"{'highest marks':15}: {high}")
    elif choice==3:
        display_marks(marks,subjects,n)
    elif choice==4:
        display_highest_lowest(high,marks)
    elif choice==5:
        break 
    else:
        print("no correct choice! ")