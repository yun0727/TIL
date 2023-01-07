#230103
#1 정수를 입력받고 0보다 크면 True 아니면 False
A = int(input("정수를 입력하세요"))
if A>0:
    print(True)
else:
    print(False)

#2 정수 두개를 입력 받고 크기가 더 큰 정수를 출력, 
# 두 정수가 같으면 False
A=int(input("첫 번째 정수를 입력하세요"))
B=int(input("두 번째 정수를 입력하세요"))
if A>B:
    print(A)
elif A<B:
    print(B)
else:
    print(False)

#3 정수 한개를 입력 받고 
#해당 정수가 1보다 크고, 3=10보다 작으면 True
#아니면 False
A = int(input("정수를 입력하세요"))
if (A>1 and A<10):
    print(True)
else:
    print(False)

#4 정수 한개를 입력 받고
#0보다 크고, 짝수라면 True
#아니면 False
A=int(input("정수를 입력하세요"))
if (A>0 and A%2==0):
    print(True)
else:
    print(False)

#5 정수 한개를 입력받고
# 값이 100초과, 0미만이면 "에러" 출력
# 값이 60이상이면 "합격" 출력
# 값이 60미만이면 "불합격" 출력
A=int(input("정수를 입력하세요"))
if (A>100 or A<0):
    print("에러")
elif(A>=60):
    print("합격")
else:
    print("불합격")

# 6
# 문자열 입력받고
# 입력 받은 문자열을 반대로 한 글자씩 출력    
word=input("문자열을 입력하세요")
for char in word[::-1]:
    print(char)

# 7 정수 두개를 입력받고
# 두 수 사이의 정수를 오름차순으로 출력
# 두 값이 같으면 False 출력
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

# 8
# 정수 두개를 입력 받고
# 두 수 사이의 정수를 내림차순으로 한줄에 출력
# 두 값이 같으면 False
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

# 9 정수 한개를 입력 받고
# 1부터 입력 값 사이의 정수 중 홀수만 출력
# 입력 값이 1보다 작으면 False 출력
A=int(input("정수를 입력하세요"))
if A<1:
    print(False)
else:
    for num in range(1,A,2):
        print(num)

#10 구구단 출력
for a in range(2,10):
    for b in range(1,10):
        print(a,"*",b,"=",a*b)