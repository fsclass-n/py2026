# print 자세히 알기
# print() 함수의 용도는 데이터를 출력하는 것
a = 123
print(a) # 123

a = "Python"
print(a) # Python

a = [1, 2, 3]
print(a) # [1, 2, 3]

# 큰따옴표로 둘러싸인 문자열은 + 연산과 동일하다
# 1번과 2번은 동일한 결괏값을 출력한다.
print("life" "is" "too short") # 1번 -> lifeistoo short
print("life"+"is"+"too short") # 2번 -> lifeistoo short

# 문자열 띄어쓰기는 쉼표로 한다
print("life", "is", "too long") # life is too short

# sep(셉, Separator) 매개변수로 구분자 설정하기
# sep의 기본값은 공백(' ')이다.
print("2025", "08", "17", sep="-")
print("점프", "파이썬", sep=" To ")

# 한 줄에 결괏값 출력하기
# end 매개변수를 사용해 끝 문자를 지정한다.
# end의 기본값은 줄바꿈(\n) 문자이다.
for i in range(10):
    print(i, end=' ')
