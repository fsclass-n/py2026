# 사용자 입력: input()
# input은 사용자가 키보드로 입력한 모든 것을 문자열로 저장한다.
a = input()
print(a)

# 프롬프트를 띄워 사용자 입력받기
# input("안내_문구")
# 괄호 안에 입력한 문구가 프롬프트로 나타난다.
# input은 입력되는 모든 것을 문자열로 취급하므로
# number는 숫자가 아닌 문자열이라는 것에 주의
number = input("숫자를 입력하세요: ")
print(number)

# 입력값을 숫자로 변환하기
# 1. 정수로 변환하기
# int() 함수는 문자열이나 실수를 정수로 변환하는 파이썬 내장 함수이다.
age = input("나이를 입력하세요: ")
age = int(age) # 문자열을 정수로 변환
print(age + 1)

# 2. 실수로 변환하기
# float() 함수는 문자열이나 정수를 실수로 변환하는 파이썬 내장 함수이다.
height = input("키를 입력하세요(cm): ")
height = float(height) # 문자열을 실수로 변환
print(height / 100) # 미터 단위로 변환

# 3. 한 번에 변환하기
# input과 int(또는 float)를 한 줄에 작성할 수도 있다.
age = int(input("나이를 입력하세요: "))
print(type(age)) # <class 'int'>

# print 자세히 알기
# print() 함수의 용도는 데이터를 출력하는 것
a = 123
print(a)
