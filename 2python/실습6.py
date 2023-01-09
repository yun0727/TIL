#구현 230109

#1 문자열을 입력받고, e가 처름 나오는 위치를 출력하세요
#문자열에서 e가 없으면 -1을 출력하세요
str=list(input("문자열을 입력하세요 > "))
sum=0
for i in range(0,len(str)):
    if str[i] == "e": 
        sum+=0
        print(sum)
        break
    else:
        sum+=1
if "e" not in str:
    print("-1")

#2 문자열을 입력받고
# 각 단어의 등장 횟수를 출력
str=list(input("문자열을 입력하세요 > ").split())
sum = 0
words={}
for word in str:
    if word not in words:
        words[word]=1
    elif word in words:
        words[word] +=1
for word,count in words.items():
    print(f"{word} {count}")

#3 문자열을 입력받고 
#e를 제거한 결과를 출력하세요
str=list(input("문자열을 입력하세요 > "))
sum = 0
words={}
for i in range(0,len(str)):
    if str[i] != "e":
        words[i]=str[i]
    elif str[i] == "e":
        words[i] = ""
for i in range(0,len(words)):
    print(words[i],end="")

#4 문자열과 알파벳을 공백으로 구분해서 입력받고
#문자열에서 입력한 알파벳의 개수를 출력하세요
words, a =input("문자열을 입력하세요 > ").split()
sum=0
for word in words:
    if a == word:
        sum += 1
    elif a != words:
        sum += 0
print(sum)

#5 양의 정수 3개를 입력 받고
#3개의 양수를 - 로 연결해서 출력하세요
num=list(input("문자열을 입력하세요 > ").split())
for i in range(0,len(num)-1):
    num[i] = num[i]+"-"
for i in range(0,len(num)):
    print(num[i],end="")

#6 양의 정수를 입력받고
#자리수의 합을 출력하세요
#만약, 입력 받은 값이 0보다 작으면 -1을 출력하세요
#단, 양의 정수를 문자열로 변경하지마세요
num=list(input("문자열을 입력하세요 > "))
sum=0
if num[0] == '-':
    print("-1")
else:    
    for i in range(0,len(num)):
        sum += int(num[i])
    print(sum)


