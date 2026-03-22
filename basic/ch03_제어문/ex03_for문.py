# for문 기본 구조
# for 변수 in 리스트(또는 튜플, 문자열):
#   수행할_문장1
#   수행할_문장2
#   ...
# 리스트나 튜플, 문자열의 첫 번째 요소부터 마지막 요소까지
# 차례로 변수에 대입되어 '수행할_문장1', '수행할_문장2' 등이 수행된다.

# 전형적인 for 문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

# 댜양한 for 문의 사용
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

# for 문의 응용
# 총 5명의 학생이 시험을 보았는데
# 시험 점수가 60점 이상이면 합격이고
# 그렇지 않으면 불합격이다.
# 합격인지, 불합격인지 결과를 보여 주시오.
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

# for문과 continue문
# for 문 안의 문장을 수행하는 도중 continue 문을 만나면 for 문의 처음으로 돌아간다.
# 상황:
# 60점 이상인 사람에게는 축하 메시지를 보내고
# 나머지 사람에게는 아무런 메시지도 전하지 않는 프로그램
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

# for문과 함께 자주 사용하는 range 함수
# 숫자 리스트를 자동으로 만들어 주는 range 함수
a = range(10)
print(a) # range(0, 10)
# range(10)은 0부터 10 미만의 숫자를 포함하는 range 객체를 만들어 준다.
# range(시작_숫자, 끝_숫자) 이때 끝 숫자는 포함되지 않는다.
a = range(1, 11)
print(a) # range(1, 11)

# 1부터 10까지 더하기
add = 0
# range(1, 11)은 숫자 1부터 10까지(1 이상 11 미만)의 숫자를 데이터로 가지는 객체이다.
for i in range(1, 11):
    add += i
print(add)

# 합격 축하 문장 출력
marks = [90, 25, 67, 45, 80]
# len 함수는 리스트 안의 요소 개수를 리턴하는 함수이다.
# range(5)는 0부터 4까지의 숫자
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

# for와 range를 이용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        # print 문의 end 매개변수에는 줄바꿈 문자(\n)가 기본값으로 설정되어 있다.
        print(i*j, end=" ")
    print('')

# a 리스트의 각 항목에 3을 곱
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result) # [3, 6, 9, 12]

# list comprehension
# 리스트 안에 for 문을 포함
# [표현식 for 항목 in 반복_가능_객체 if 조건문]
# if 조건문은 생략 가능
a = [1,2,3,4]
# result = [num * 3 for num in a]
result = [num * 3 for num in a if num % 2 == 0]
print(result) # [6, 12]

# 구구단의 모든 결과를 리스트에 담기
# [표현식 for 항목1 in 반복_가능_객체1 if 조건문1
#       for 항목2 in 반복_가능_객체2 if 조건문2
#       ...
#       for 항목n in 반복_가능_객체n if 조건문n]
result = [x*y for x in range(2, 10)
              for y in range(1, 10)]
print(result)

# for문과 break문
# break 문은 for 문을 강제로 빠져나가고 싶을 때 사용한다.
for i in range(10):
    if i == 5:
        break
    print(i)

# for-else문
# for 문이 정상적으로 종료되었을 때(break로 빠져나가지 않았을 때) else 절이 실행된다.
for i in range(5):
    print(i)
else:
    print("for 문이 정상 종료되었습니다.")

# enumerate 함수
# 리스트의 순서(인덱스)와 값을 함께 구하고 싶을 때
# enumerate는 0부터 시작하는 인덱스 번호를 자동으로 생성해 준다.
fruits = ["apple", "banana", "orange"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

fruits = ["apple", "banana", "orange"]
for i, fruit in enumerate(fruits, 1): # 1부터 시작
    print(f"{i}: {fruit}")

# zip 함수로 여러 리스트 함께 순회하기
# 두 개 이상의 리스트를 동시에 순회
names = ['홍길동', '김철수', '이영자']
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}점")

# 세 개 이상의 리스트 순회
names = ['홍길동', '김철수', '이영자']
korean = [85, 92, 78]
english = [90, 88, 95]
for name, kor, eng in zip(names, korean, english):
    print(f"{name}: 국어 {kor}점, 영어 {eng}점")