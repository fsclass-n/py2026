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

