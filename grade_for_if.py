for i in range(1,5):
    name=input()
    num=int(input())
    if(num>=90):
        grade='A'
    elif(num>=80):
        grade='B'
    elif(num>=70):
        grade='C'
    elif(num>=60):
        grade='D'
    else:
        grade='F'
    print(name+'의 학점: '+grade)