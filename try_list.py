name=input("enter your name: ")
roll=int(input("enter your roll no: "))
n=int(input("enter the number of subjects: "))
total=0
marks=[]
for i in range (1,n+1):
    num=int(input(f"enter the marks of sub{i}: "))
    marks.append(num)
    total+=num

def highest_marks (mark):    
    highest=0
    for num in mark:
        if num>highest:
            highest=num
    return highest
high=highest_marks(marks)
print("highest marks among sub is: ",high)