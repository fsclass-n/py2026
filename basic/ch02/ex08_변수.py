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
