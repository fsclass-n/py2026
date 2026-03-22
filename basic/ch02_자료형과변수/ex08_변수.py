from copy import copy
# 변수는 어떻게 만들까?
# a, b, c를 '변수'라고 한다.

a = 1
b = "python"
c = [1, 2, 3]

# 변수를 만들 때는 =(assignment) 기호를 사용한다.
# 변수_이름 = 변수에_저장할_값
# C나 JAVA 같은 언어에서는 변수를 만들 때 자료형을 직접 지정해야 한다.
# 파이썬은 변수에 저장된 값을 스스로 판단하여 자료형을 지정하므로 더 편리하다.

# 변수 명명 규칙
# 1. 영문자, 숫자, 언더스코어(_)만 사용할 수 있다.
# 2. 숫자로 시작할 수 없다.
# 3. 예약어는 사용할 수 없다.
# 4. 대소문자를 구분한다.

# 올바른 변수명 예시
name = "홍길동"
age = 25
user_name = "gildong"
userName = "gildong" # 카멜 케이스
_private = "비공개"
count1 = 10

# 잘못된 변수명 예시
# 1name = "홍길동" -> 숫자로 시작
# user-name = "홍길동" -> 하이픈 사용
# if = 10 -> 예약어 사용

# 파이썬 예약어
# False, None, True, and, as, assert, break, class, continue,
# def, del, elif, else, except, finally, for, from, global,
# if, import, in, is, lambda, nonlocal, not, or, pass,
# raise, return, try, while, with, yield

# 변수명 권장 사항
# 1. 의미가 명확한 이름을 사용한다.
# 2. snake_case(단어 사이에 언더스코어)를 권장한다.
# 3. 너무 짧거나 긴 이름은 피한다.

# 좋은 예
# student_name = 김철수
# total_score = 95
# user_age = 20

# 피야할 예
a = 100 #의미 불명확
studentNameFromKorea = "김철수" # 너무 긴 이름

# 변수란? 변수는 객체를 가리키는 것
# 객체란? 자료형의 데이터(값)와 같은 것
a = [1, 2, 3]
# [1, 2, 3] 값을 가지는 리스트 객체가 자동으로 메모리에 생성되고,
# 변수 a는 [1, 2, 3] 리스트가 저장된 메모리의 주소를 가리키게 된다.
# 메모리란 컴퓨터가 프로그램에서 사용하는 데이터를 기억하는 공간이다.
# 메모리 주소 확인
a = [1, 2, 3]
# id는 변수가 가리키는 객체의 주소 값을 반환하는 파이썬 내장 함수이다.
print(id(a)) # 3071923881664

# 리스트를 복사할 때
a = [1, 2, 3]
b = a
print(id(a)) # 1741634779520
print(id(b)) # 1741634779520

# 동일한 객체를 가리키는지 판단하는 is 명령어
print(a is b) # a와 b가 가리키는 객체가 같을까? True
a[1] = 4
print(a) # [1, 4, 3]
print(b) # [1, 4, 3]

# b 변수를 생성할 때 a 변수의 값을 가져오면서
# a와는 다른 주소를 가리키도록 만들 수는 없을까?
# 방법1: 리스트 전체를 가리키는 [:]을 사용해서 복사
a = [1, 2, 3]
b = a[:]
print(id(a)) # 1938439387584
print(id(b)) # 1938439761024
a[1] = 4
print(a) # [1, 4, 3]
print(b) # [1, 2, 3]

# 방법2: copy 모듈 이용하기
a = [1, 2, 3]
b = copy(a)
print(b is a) # false

# 방법3: copy 함수 사용하기
a = [1, 2, 3]
b = a.copy()
print(b is a) # false

# 변수를 만드는 여러 가지 방법
# 튜플로 a, b에 값을 대입할 수 있다.
a, b = ('python', 'life')
print(a) # python
print(b) # life
# 튜플은 괄호를 생략해도 된다.
(a, b) = 'python', 'life'
print(a) # python
print(b) # life
# 리스트로 변수를 만들 수도 있다.
[a, b] = ['python', 'life']
print(a) # python
print(b) # life
# 여러 개의 변수에 같은 값을 대입할 수도 있다.
a = b = 'python'
print(a)
print(b)
# 두 변수의 값을 간단하게 바꿀 수 있다.
a = 3
b = 5
a, b = b, a
print(a) # 5
print(b) # 3