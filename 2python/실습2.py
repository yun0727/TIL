A = int(input("정수를 입력하세요"))
if A>0:
    print(True)
else:
    print(False)

A=int(input("첫 번째 정수를 입력하세요"))
B=int(input("두 번째 정수를 입력하세요"))
if A>B:
    print(A)
elif A<B:
    print(B)
else:
    print(False)

A = int(input("정수를 입력하세요"))
if (A>1 and A<10):
    print(True)
else:
    print(False)

A=int(input("정수를 입력하세요"))
if (A>0 and A%2==0):
    print(True)
else:
    print(False)

A=int(input("정수를 입력하세요"))
if (A>100 or A<0):
    print("에러")
elif(A>=60):
    print("합격")
else:
    print("불합격")
    
word=input("문자열을 입력하세요")
for char in word[::-1]:
    print(char)

A=int(input("첫 번째 정수를 입력하세요"))
B=int(input("두 번째 정수를 입력하세요"))
if A>B:
    for num in range(B+1,A):
        print(num)
elif A<B:
    for num in range(A+1,B):
        print(num)
else:
    print(False)

A=int(input("첫 번째 정수를 입력하세요"))
B=int(input("두 번째 정수를 입력하세요"))
if A>B:
    for num in range(A-1,B,-1):
        print(num,end=" ")
elif A<B:
    for num in range(B-1,A,-1):
        print(num,end=" ")
else:
    print(False)

A=int(input("정수를 입력하세요"))
if A<1:
    print(False)
else:
    for num in range(1,A,2):
        print(num)
        
for a in range(2,10):
    for b in range(1,10):
        print(a,"*",b,"=",a*b)