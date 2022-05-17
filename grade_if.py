name=input()
num=int(input())
if(num in range(90,101)):
    grade='A'
elif(num in range(80,90)):
    grade='B'
elif(num in range(70,80)):
    grade='C'
elif(num in range(60,70)):
    grade='D'
else:
    grade='F'
print(name+'의 학점: '+grade)