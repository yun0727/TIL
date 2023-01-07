#230104 제어문(2)
#문제1 정수 값 입력받고 절대값 출력
a=int(input("정수를 입력하세요"))
if a<0:
    a=-a
else:
    a=a
print(a)

#문제2 리스트의 값 입력받고 리스트에 저장된 정수 개수 출력
number_list=list(input("number_list = ").split())
print(number_list)
b=0
for a in number_list:
    b=b+1
print(b)

#문제3 리스트의 값 입력받고 리스트에 저장된 정수 합 출력
number_list=list(input("number_list = ").split())
sum=0
for a in number_list:
    sum = sum+int(a)
print(sum)
    
#문제4 리스트의 값 입력받고 리스트에 저장된 정수 평균 출력
number_list=list(input("number_list = ").split())
sum=0
b=0
for a in number_list:
    sum = sum+int(a)
    b=b+1
print(float(sum/b))

#문제5 리스트의 값 입력받고 리스트에 저장된 정수 곱 출력
number_list=list(input("number_list = ").split())
mul=1
for a in number_list:
    mul=mul*int(a)
print(mul)

#문제6
number_list=list(map(int,input("number_list = ").split()))
max=number_list[0]
for a in number_list:
    if a>max:
        max=a
print(max)

#문제7
number_list=list(map(int,input("number_list = ").split()))
min=number_list[0]
for a in number_list:
    if a<min:
        min=a
print(min)