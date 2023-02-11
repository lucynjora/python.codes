#grading system
sub1=int(input("enter marks for sub1"))
sub2=int(input("enter marks for sub2"))
sub3=int(input("enter marks for sub3"))
average=((sub1+sub2+sub3)/3)
if(average>=70):
    print("A")
elif(average>=60 and average<=69):
    print("B")
elif(average>=50 and average<=59):
    print("C")
elif(average>=40 and average<=49):
    print("D")
else:
        print("FAIL")
    