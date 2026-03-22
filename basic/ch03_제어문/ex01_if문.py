# if문
# 조건을 판단하여 해당 조건에 맞는 상황을 수행
# 상황: '돈이 있으면 택시를 타고 가고, 돈이 없으면 걸어간다.'
money = True
if money:
    print("택시를 타고 간다.")
else:
    print("걸어 간다.")

money = True
if money:
    print("택시를")
# IndentationError: unexpected(예기치 않은) indent
# print("타고") -> error
    print("간다.")

# 들여쓰기는 언제나 같은 깊이로 해야 한다.
money = True
# 조건문 다음에 콜론(:)을 잊지 말자!
if money:
    print("택시를")
    print("타고")
        # print("간다.") -> error

# '조건문'이란 참과 거짓을 판단하는 문장
x = 3;
y = 2;
print(x > y); # True
print(x < y); # False
print(x == y); # False
print(x != y); # True

# 상황:
# 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 가고,
# 그렇지 않으면 걸어가라.
money = 2000
if money >= 3000:
    print("택시를 타고 간다.")
else:
    print("걸어간다.")

# 상황:
# 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 가고,
# 그렇지 않으면 걸어가라.
money = 2000
card = True
if money >= 3000 or card:
    print("택시 타고 간다.")
else:
    print("걸어간다.")

# in, not in
print(1 in [1, 2, 3]) # True
print(1 not in [1, 2, 3]) # False
print('a' in ('a', 'b', 'c')) # True
print('j' not in 'python') # True

# 상황:
# 만약 주머니에 돈이 있으면 택시를 타고 가고,
# 없으면 걸어가라.
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 간다.")
else:
    print("걸어간다.")

# 조건문에서 아무 일도 하지 않게 설정하고 싶다면?
# 이럴 때 사용하는 것이 바로 pass이다.
# 상황:
# 주머니에 돈이 있으면 가만히 있고,
# 주머니에 돈이 없으면 카드를 꺼내라.
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼낸다.")

# 상황:
# 주머니에 돈이 있으면 택시를 타고 가고,
# 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고,
# 돈도 없고 카드도 없으면 걸어가라.
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("돈이 있으니, 택시를 타고 간다.")
else:
    if card:
        print("카드가 있으니, 택시를 타고 간다.")
    else:
        print("걸어간다.")

# 다양한 조건을 판단하는 elif
# elif는 개수에 제한 없이 사용할 수 있다.
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("돈이 있으니, 택시를 타고 간다.")
elif card:
    print("카드가 있으니, 택시를 타고 간다.")
else:
    print("걸어간다.")

# 수행할 문장이 한 줄일 때
# 좀 더 간략하게 코드를 작성하는 방법이 있다.
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket: pass
else: print("카드를 꺼낸다.")


# 상황:
# 학점이 A이면 "탁월한 성적입니다."를,
# B이면 "우수한 성적입니다."를,
# C이면 "보통입니다."를,
# 그 외에는 "노력이 필요합니다."를 출력하라.
# grade ==이 반복되어 읽기에 깔끔하지 않다.
grade = 'B'
if grade == 'A':
    print("탁월한 성적입니다.")
elif grade == 'B':
    print("우수한 성적입니다.")
elif grade == 'C':
    print("보통입니다.")
else:
    print("노력이 필요합니다.")

# match-case 문
# 파이썬 3.10 버전부터 사용할 수 있다.
# 하나의 변수 값에 따라 분기하는 경우
# match 뒤에 비교할 변수를 쓰고,
# case 뒤에 해당 변수와 비교할 값을 적는다.
# case _는 생략할 수 있다.
# 생략하면 어떤 case에도 일치하지 않을 때 아무 일도 하지 않는다.
grade = 'B'
match grade:
    case 'A':
        print("탁월한 성적입니다.")
    case 'B':
        print("우수한 성적입니다.")
    case 'C':
        print("보통입니다.")
    case _:
        print("노력이 필요합니다.")

# 여러 패턴을 하나의 case에서 처리하기
# 하나의 case에 여러 값을 지정할 수도 있다.
# | 기호를 사용하면 된다.
grade = "B"
match grade:
    case "A" | "B" | "C":
        print("합격입니다.")
    case _:
        print("불합격입니다.")

# 연쇄 비교 연산자
# 수학에서처럼 비교 연산자를 연쇄적으로 사용할 수 있다.
x = 5
# x가 1보다 크고 10보다 작은가?
print(1 < x < 10) # True
# x가 10 이상 20 이하인가?
print(10 <= x <= 20) # False

# 다음과 같이 쓰는 것과 같다.
x = 5
print((1 < x) and (x < 10)) # True
print((10 <= x) and (x <= 20)) # False

# 상황:
# 점수가 60점 이상이면 "합격",
# 미만이면 "불합격"이라는 메시지를 저장하고 싶다
score = 85
if score >= 60:
    result = "합격"
else:
    result = "불합격"
print(result) # 합격

# 조건부 표현식
# 기본 형태:
# 변수 = 참일_때_값 if 조건 else 거짓일_때_값
score = 85
result = "합격" if score >= 60 else "불합격"
print(result) # 합격

age = 19
status = "성인" if age >= 18 else "미성년"
print(status) # 성인

temperature = 25
weather = "따뜻함" if temperature > 20 else "추움"
print(weather) # 따뜻함

money = 1500
transportation = "버스" if money >= 1000 else "도보"
print(transportation) # 버스