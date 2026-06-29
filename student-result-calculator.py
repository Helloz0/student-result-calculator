name=input("enter your name: ")
roll=int(input("enter your roll no: "))
total=0
for i in range (1,6):
    num=int(input(f"enter the marks of sub{i}: "))
    total+=num

percent=(total/500)*100
avg=total/5
def grade (percent):
    if percent>90 and percent<=100:
        print("grade A")
    elif percent>80 and percent<=90:
        print("grade B")
    elif percent>70 and percent<=80:
        print("grade C")
    elif percent>60 and percent<=70:
        print("grade D")
    elif percent>50 and percent<=60:
        print("grade E")
    elif percent>100:
        print("error")
    else:
        print("failed")

print("RESULT:-")
print("name: ",name)
print("roll no: ",roll)
print("total marks: ",total)
print(f"percentage: {percent:.2f}%")
print("average: ",avg)
grade(percent)
