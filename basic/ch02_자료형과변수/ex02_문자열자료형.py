# 문자열을 만드는 방법 4가지
print("Hello World")
print('Python is fun')
print("""Life is too short, You need python""")
print('''Life is too short, You need python''')

# 문자열에 작은따옴표 포함하기
food = "Python's favorite food is perl"
print(food)

# 문자열에 큰따옴표 포함하기
say = '"Python is very easy." he says'
print(say)

# 역슬래시를 사용해서 작은따옴표와 큰따옴표를 문자열에 포함
food = 'Python\'s favorite food is perl'
print(food)
say = "\"Python is very easy.\" he says"
print(say)

# 여러 줄인 문자열을 변수에 대입
# 줄바꿈 문자인 \n을 삽입
multiline = "Life is too short\nYou need python"
print(multiline)

multiline='''
Lift is too short
You need python
'''
print(multiline)

multiline="""
Lift is too short
You need python
"""
print(multiline)

# 문자열 연산
head = "Python"
tail = " is fun!"
# 문자열 연결
print(head + tail)
a = "Python"
# 문자열 반복
print(a * 2)

print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 길이
a = "Life is too short"
print(len(a))

# 문자열 인덱싱과 슬라이싱
# 인덱싱(indexing)은 무엇인가를 '가리킨다'
a = "Life is too short, You need Python"
print(a[3]) # e
print(a[0]) # L
print(a[-0]) # L
print(a[12]) # s
print(a[-1]) # n
print(a[-2]) # o
print(a[-5]) # y

# 슬라이싱(slicing)은 무엇인가를 '잘라 낸다'
b = a[0] + a[1] + a[2] + a[3]
print(b) # Life
# a[시작번호:끝번호], 끝 번호에 해당하는 문자는 포함하지 않는다.
# 0 <= a < 4, 4는 포함하지 않음!
print(a[0:4]) # 'Life'
print(a[0:5]) # 'Life '
print(a[0:2]) # Li
print(a[5:7]) # is
print(a[12:17]) # short
# 끝 번호 부분을 생략하면 시작 번호부터 그 문자열의 끝까지
print(a[19:]) # You need Python
# 시작 번호를 생략하면 문자열의 처음부터 끝 번호까지
print(a[:17]) # Life is too short
# 시작 번호와 끝 번호를 생략하면 문자열의 처음부터 끝까지
print(a[:]) # Life is too short, You need Python
# -(빼기) 기호를 사용할 수 있다.
# a[19]에서 a[-8]까지를 의미한다.
print(a[19:-7]) # You need

# 슬라이싱으로 문자열 나누기
a = "20230331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

a = "20230331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)

# Pithon 문자열을 Python으로 바꾸려면?
a = "Pithon"
print(a[1]) # i
# 문자열의 요솟값은 바꿀 수 없는 값이기 때문이다
# 그래서 문자열을 '변경 불가능한(immutable) 자료형'이라고도 부른다.
# a[1] = 'y' -> error
print(a)

a = "Pithon"
print(a[:1])
print(a[2:])
print(a[:1] + 'y' + a[2:])

# 문자열 포매팅
# 숫자를 넣기 위해서는 %d,
# 문자열을 넣기 위해서는 %s를 써야 한다.
print("I eat %d apples." % 3) # I eat 3 apples
print("I eat %s apples." % "five") # I eat five apples.

number = 3
print("I eat %d apples." % number) # I eat 3 apples.

number = 10
day = "three"
# 2개 이상의 값을 넣으려면?
# 마지막 % 다음 괄호 안에 쉼표(,)로 구분하여 각각의 값을 넣어 주면 된다.
print("I ate %d apples. so I was sick for %s days." % (number, day))
# I ate 10 apples. so I was sick for three days.
# %% -> Literal % (문자 % 자체)
# print("Error is %d%." % 98) -> error
print("Error is %d%%." % 98)
print("Error is %.")

# 포멧 코드와 숫자 함께 사용
# %10s는 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고
# 그 앞의 나머지는 공백으로 남겨 두라는 의미다.
print("%10s" % "hi")
# 왼쪽 정렬은 %-10s가 된다.
print("%-10sjane." % 'hi')
# 소숫점 표현하기
# 소수점 네 번째 자리까지만 나타내고 싶은 경우
#  '.'는 소수점 포인트, 그 뒤의 숫자 4는 소수점 뒤에 나올 숫자의 개수다.
# %0.4f는 0을 생략하여 %.4f처럼 사용하기도 한다.
print("%0.4f" % 3.42134234) # 3.4213
# 전체 길이가 10개인 문자열 공간에서 오른쪽으로 정렬
print("%10.4f" % 3.42134234) # '    3.4213'

# format 함수를 사용한 포매팅
print("I eat {0} apples".format(3)) # I eat 3 apples
print("I eat {0} apples".format("five")) # I eat five apples

number = 3
print("I eat {0} apples".format(number)) # I eat 3 apples

number = 10
day = "three"
# 2개 이상의 값을 넣을 경우,
# 문자열의 {0}, {1}과 같은 인덱스 항목이 format 함수의 입력값으로 순서에 맞게 바뀐다.
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
# I ate 10 apples. so I was sick for three days.

# 이름으로 넣기
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
# I ate 10 apples. so I was sick for 3 days.

# 인덱스와 이름을 혼용
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))
# I ate 10 apples. so I was sick for 3 days

# 왼쪽 정렬
# :<10 표현식을 사용하면
# 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞출 수 있다.
print("{0:<10}".format("hi"))

# 오른쪽 정렬
print("{0:>10}".format("hi"))
# 가운데 정렬
print("{0:^10}".format("hi"))

# 공백 채우기
# 정렬할 때 공백 문자 대신 지정한 문자 값으로 채워 넣을 수도 있다.
# 채워 넣을 문자 값은 정렬 문자 <, >, ^ 바로 앞에 넣어야 한다.
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))

# 소수점 표현하기
y = 3.42134234
print("{0:0.4f}".format(y)) # 3.4213
print("{0:10.4f}".format(y)) #'    3.4213'

# { 또는 } 문자 표현하기
# 중괄호 문자를 포매팅 문자가 아닌 문자 그대로 사용하고 싶은 경우
# {{}}처럼 2개를 연속해서 사용하면 된다.
print("{{ and }}".format()) # { and }

# f 문자열 포매팅
# 파이썬 3.6 버전부터는 f 문자열 포매팅 기능을 사용할 수 있다.
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
# 나의 이름은 홍길동입니다. 나이는 30입니다.

# 표현식이란 중괄호 안의 변수를 계산식과 함께 사용하는 것이다.
age = 30
print(f'나는 내년이면 {age + 1}살이 된다.')
# 나는 내년이면 31살이 된다.

# 딕셔너리, f 문자열 포매팅
# 딕셔너리는 Key와 Value라는 것을 한 쌍으로 가지는 자료형이다.
d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
# 나의 이름은 홍길동입니다. 나이는 30입니다.

# 정렬
# 왼쪽 정렬
print(f'{"hi":<10}') # 'hi        '
# 오른쪽 정렬
print(f'{"hi":>10}') # '        hi'
# 가운데 정렬
print(f'{"hi":^10}') # '    hi    '

# 공백 채우기
# 가운데 정렬하고 '=' 문자로 공백 채우기
print(f'{"hi":=^10}') # ====hi====
# 왼쪽 정렬하고 '!' 문자로 공백 채우기
print(f'{"hi":!<10}') # hi!!!!!!!!

# 소수점
y = 3.42134234
# 소수점 4자리까지만 표현
print(f'{y:0.4f}') # 3.4213
# 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤
print(f'{y:10.4f}') # '    3.4213'

# {}를 문자 그대로 표시
print(f'{{ and }}') # { and }

# f 문자열을 사용하여 금액에 콤마(,) 삽입하기
# 난 1500000원이 필요해
# f 문자열을 활용하면 숫자에 자동으로 콤마(,)를 삽입
print(f"난 {1500000:,}원이 필요해") # 난 1,500,000원이 필요해

# 문자열 내장 함수
# 내장 함수를 사용하려면?
# 문자열 변수 이름 뒤에 '.'를 붙인 후 함수 이름을 써 주면 된다.
# 문자 개수 세기 - count
a = "hobby"
print(a.count('b')) # 2

# 위치 알려 주기 - find
a = "Python is the best choice"
print(a.find('b')) # 14
# 찾는 문자나 문자열이 존재하지 않는다면 -1을 반환한다.
print(a.find('k')) # -1

# 위치 알려 주기 - index
a = "Life is too short"
print(a.index('t')) # 8
# 찾는 문자나 문자열이 존재하지 않는다면 오류가 발생한다.
# ValueError: substring not found
# print(a.index('k')) -> error

# 문자열 삽입 - join
# 문자열의 각각의 문자 사이에 ','를 삽입
print(",".join('abcd')) # a,b,c,d
print(",".join(['a','b','c','d'])) # a,b,c,d

# 소문자를 대문자로 바꾸기 - upper
a = "hi"
print(a.upper()) # HI

# 대문자를 소문자로 바꾸기 - lower
a = "HI"
print(a.lower()) # hi

# 왼쪽 공백 지우기 - lstrip
a = " hi "
# 가장 왼쪽에 있는 한 칸 이상의 연속된 공백들을 모두 지운다.
print(a.lstrip()) # 'hi '

a = " hi "
# 가장 오른쪽에 있는 한 칸 이상의 연속된 공백을 모두 지운다.
print(a.rstrip()) # ' hi'

# 양쪽 공백 지우기 - strip
a = " hi "
print(a.strip()) # 'hi'

# 문자열 바꾸기 - replace
# 문자열 안의 특정한 값을 다른 값으로 치환
a = "Life is too short"
# replace(바뀔_문자열, 바꿀_문자열)
print(a.replace("Life", "Your leg"))
# Your leg is too short

# 문자열 나누기 - split
a = "Life is too short"
# a.split()처럼 괄호 안에 아무 값도 넣어 주지 않으면
# 공백([Space], [Tab], [Enter])을 기준으로 문자열을 나누어 준다.
print(a.split()) # ['Life', 'is', 'too', 'short']
b = "a:b:c:d"
# b.split(':')처럼 괄호 안에 특정 값이 있을 경우에는
# 괄호 안의 값을 구분자로 해서 문자열을 나누어 준다.
print(b.split(':')) # ['a', 'b', 'c', 'd']

# 문자열이 알파벳으로만 구성되어 있는지 확인 - isalpha
# 문자열의 모든 문자가 문자이면 True를 반환하며,
# 공백이나 숫자, 특수 문자가 포함되어 있으면 False를 반환한다.
s = "Python"
print(s.isalpha()) # True
s = "Python3"
print(s.isalpha()) # False
s = "Hello World"
print(s.isalpha()) # False

# 문자열이 숫자로만 구성되어 있는지 확인 - isdigit
# 문자열의 모든 문자가 숫자 문자일 경우 True를 반환하고,
# 하나라도 숫자 문자가 아닌 문자가 포함되어 있으면 False를 반환한다.
s = "12345"
print(s.isdigit()) # True
s = "1234a"
print(s.isdigit()) # False
s = "12 34"
print(s.isdigit()) # False

# 문자열이 특정 문자(열)로 시작하는지 확인 - startswith
s = "Life is too short"
print(s.startswith("Life")) # True
print(s.startswith("short")) # False

# 문자열이 특정 문자(열)로 끝나는지 확인 - endswith
# 지정한 문자열로 끝나면 True를 반환하고,
# 그렇지 않으면 False를 반환한다.
s = "Life is too short"
print(s.endswith("short")) # True
print(s.endswith("too")) # False

# 착각하기 쉬운 문자열 함수
# upper 함수는 a 변수의 값 자체를 변경하는 것이 아니라
# 대문자로 바꾼 값을 반환
#  문자열은 자체의 값을 변경할 수 없는 immutable 자료형이다.
a = 'hi'
print(a.upper()) # HI
print(a) # hi

a = a.upper()
print(a) # HI