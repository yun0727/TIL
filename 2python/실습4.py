#문제1
words = list(input("문자열을 입력하세요"))
count = 0
for word in words:
    if word == "e":
        count+=1
print(count)
    
#문제2
words = list(input("문자열을 입력하세요"))
count = 0
for word in words:
    if word == "e" or word =="E" :
        count+=1
    elif word == "a" or word =="A":
        count+=1
    elif word == "i" or word =="I":
        count+=1
    elif word == "o" or word =="O":
        count+=1
    elif word == "u" or word =="U":
        count+=1
print(count)

#문제3
dict_variable = {
    "이름": "정우영",
    "생년": "2000",
    "회사": "하이퍼그로스"
}
age = int(dict_variable["생년"])
print("나이 : ",2023-age+1,"세")

#문제4
name = input("이름을 입력하세요")
num = input("전화번호를 입력하세요")
adr = input("거주지를 입력하세요")
dict_variable={'이름':name,'전화번호':num , '거주지':adr}
print(dict_variable)
print("이름 : ",dict_variable['이름'])
print("전화번호 : ",dict_variable['전화번호'])
print("거주지 : ",dict_variable['거주지'])

# #문제5
input = list(input("문자열을 입력하세요"))
for word in input:
    cnt=0
    for words in input:
        if word == words:
            cnt =+ 1
    print(word,cnt)
