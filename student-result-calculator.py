name=input("enter your name: ")
roll=int(input("enter your roll no: "))
sum=0
for i in range (1,6):
    num=int(input(f"enter the marks of sub{i}: "))
    sum+=num
    
percent=(sum/500)*100
avg=sum/5

print("RESULT:-")
print("name: ",name)
print("roll no: ",roll)
print("total marks: ",sum)
print("percentage: ",percent,"%")
print("average: ",avg)
