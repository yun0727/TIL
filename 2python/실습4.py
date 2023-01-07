#230105 딕셔너리&예외처리
#문제1
#문자열을 입력받고
#문자열에서 e의 개수를 구해서 출력
words = input("문자열을 입력하세요")
count = 0
for word in words:
    if word == "e":
        count+=1
print(count)
    
#문제2
# 문자열을 입력받력
# 문자열 중 알파벳 모음의 총 개수를 출력
words = list(input("문자열을 입력하세요"))
count = 0
for word in words:
    if(
        word == "e"
        or word =="E"
        or word =="a"
        or word =="A"
        or word =="i"
        or word =="I"
        or word =="o"
        or word =="O"
        or word =="u"
        or word =="U"
    ):
        count+=1
print(count)

#문제3
#입력과 같은 딕셔너리 변수가 있을 때
#해당 인물의 나이 출력
dict_variable = {
    "이름": "정우영",
    "생년": "2000",
    "회사": "하이퍼그로스"
}
# age = int(dict_variable["생년"])
# print("나이 : ",2023-age+1,"세")
dict_variable["나이"] = 2023-int(dict_variable["생년"])+1
print(dict_variable["나이"])

#문제4
#이름, 전화번호, 거주지 정보를 입력받아
#딕셔너리 구조로 저장하고
#해당 딕셔너리와 딕셔너리의 정보를 구분해서 출력
name = input("이름을 입력하세요")
num = input("전화번호를 입력하세요")
adr = input("거주지를 입력하세요")
dict_variable={
    '이름':name,
    '전화번호':num , 
    '거주지':adr}
print(dict_variable)
# print("이름 : ",dict_variable['이름'])
# print("전화번호 : ",dict_variable['전화번호'])
# print("거주지 : ",dict_variable['거주지'])
for key, value in dict_variable.items():
    print(f"{key} : {value}")

#문제5
#이름, 전화번호, 이메일, 거주지 정보를 입력받아
#출력 예시와 동일한 딕셔너리 구조를 출력
name = input("이름을 입력하세요")
num = input("전화번호를 입력하세요")
mail = input("이메일을 입력하세요")
adr = input("거주지를 입력하세요")
dict_variable = {
    name:{
        "전화번호":num,
        "이메일":mail,
        "거주지":adr
    }
}
print(dict_variable)


#문제6
#문자열을 입력받고, 문자열에서 개별 문자가 나오는 횟수를 출력하세요
input = list(input("문자열을 입력하세요"))
dict_variable={}
for word in input:
    if word in dict_variable.keys():
        dict_variable[word] +=1
    elif word not in dict_variable.keys():
        dict_variable[word] = 1
for key,value in dict_variable.items():
    print(key,value)
