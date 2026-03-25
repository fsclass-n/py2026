# 파이썬 내장(built-in) 함수
# 파이썬 내장 함수는 모듈과 달리 import가 필요하지 않기 때문에
# 아무런 설정 없이 바로 사용할 수 있다.

# abs, all, any, chr, dir,
# divmod, enumerate, eval, filter, hex,
# id, input, int, isinstance, len,
# list, map, max, min, oct,
# open, ord, pow, range, round,
# sorted, str, sum, tuple, type,
# zip

# abs
# abs(x)는 숫자를 입력받아 그 숫자의 절댓값을 반환
print(abs(3)) # 3
print(abs(-3)) # 3
print(abs(-1.2)) # 1.2

# all
# all(x)는 반복 가능한 데이터 x를 입력값으로 받아
# x의 요소가 모두 참이면 True,
# 거짓이 하나라도 있으면 False를 반환한다.
# 반복 가능한 데이터란?
# for 문에서 사용할 수 있는 자료형을 의미한다.
# 리스트, 튜플, 문자열, 딕셔너리, 집합 등이 있다.
print(all([1,2,3])) # True
# 요소 0은 거짓
print(all([0,2,3])) # False
# all의 입력 인수가 빈 값인 경우에는 True를 반환한다.
print(all([])) # True

# any
# any(x)는 반복 가능한 데이터 x를 입력으로 받아
# x의 요소 중 하나라도 참이 있으면 True를 반환하고,
# x가 모두 거짓일 때만 False를 반환한다.
# 즉, all(x)의 반대로 작동한다.
print(any([1, 2, 3, 0])) # True
print(any([0, ""])) # False
print(any([])) # False

# chr
# chr(i)는 유니코드 숫자 값을 입력받아 그 코드에 해당하는 문자를 반환
# 유니코드는 전 세계의 모든 문자를 컴퓨터에서
# 일관되게 표현하고 다룰 수 있도록 설계된 산업 표준 코드이다.
print(chr(97)) # a
print(chr(44032)) # 가

# dir
# 객체가 지닌 변수나 함수를 보여 주는 함수
print(dir([1,2,3]))
print(dir({'1':'a'}))

# divmod
# divmod(a, b)는 2개의 숫자 a, b를 입력으로 받아
# a를 b로 나눈 몫과 나머지를 튜플로 반환
print(divmod(7,3)) # (2, 1)
print(7 // 3) # 2
print(7 % 3) # 1

# enumerate
# enumerate는 '열거하다'라는 뜻이다.
# 순서가 있는 데이터(리스트, 튜플, 문자열)를 입력으로 받아
# 인덱스 값을 포함하는 enumerate 객체를 반환
# 보통 enumerate 함수는 for 문과 함께 사용한다.
# 자료형의 현재 순서(index)와 그 값을 쉽게 알 수 있다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

# eval
# eval(expression)은 문자열로 구성된 표현식을 입력으로 받아
# 해당 문자열을 실행한 결괏값을 반환
# eval은 입력 문자열을 실제로 실행하므로,
# 신뢰할 수 없는 외부 입력에는 사용하면 안 된다.
print(eval('1+2')) # 3
print(type(eval('1+2'))) # <class 'int'>
print(eval("'hi' + 'a'")) # hia
print(eval('divmod(4, 3)')) # (1, 1)

# filter
# filter란 '무엇인가를 걸러 낸다'라는 뜻
# filter(함수, 반복_가능한_데이터)
# 반복 가능한 데이터의 요소를 순서대로 함수에 전달하여
# 반환값이 참인 것만 묶어서 반환한다.
# positive는 리스트를 입력받아 각 요소를 판별해서 양수 값만 반환
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,6])) # [1, 2, 6]

def positive(x):
    return x > 0

# list 함수는 filter 함수의 반환값을 리스트로 출력하기 위해 사용했다.
print(list(filter(positive, [1,-3,2,0,-5,6]))) # [1,2,6]

# lambda 사용
print(list(filter(lambda x: x > 0, [1,-3,2,0,-5,6])))

# hex
# hex(x)는 정수를 입력받아
# 16진수(hexadecimal) 문자열로 변환하여 반환
print(hex(234)) # 0xea
print(hex(3)) # 0x3

# id
# id(object)는 객체를 입력받아 객체의 고유 주솟값(레퍼런스)을 반환
# id 값은 실행 환경과 시점에 따라 달라질 수 있다.
a = 3
print(id(3)) # 140719791494328
print(id(a)) # 140719791494328
b = a
print(id(b)) # 140719791494328
print(id(4)) # 140719791494360

# input
# input([prompt])는 사용자 입력을 받는 함수이다.
# 입력 인수로 문자열을 전달하면 그 문자열은 프롬프트가 된다.
a = input()
print(a)
b = input("Enter: ")
print(b)

# int
# int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자를
# 정수로 반환하는 함수이다.
# 정수가 입력되면 그대로 반환한다.
print(int('3')) # 3
print(int(3.6)) # 3
# int(x, radix)는 radix 진수로 표현된
# 문자열 x를 10진수로 변환하여 반환한다.
print(int('11', 2)) # 3
print(int('1A', 16)) # 26

# isinstance
# isinstance(object, class)는
# 첫 번째 인수로 객체,
# 두 번째 인수로 클래스를 받는다.
# 입력받은 객체가 해당 클래스의 인스턴스인지 판단하여
# 참이면 True, 거짓이면 False를 반환
class Person: pass
a = Person()
isinstance(a, Person)
b = 3
isinstance(b, Person)

# len
# len(s)는 입력값 s의 길이(요소의 전체 개수)를 반환
print(len("python")) # 6
print(len([1,2,3])) # 3
print(len((1, 'a'))) # 2

# list
# list(iterable)는 반복 가능한 데이터를 입력받아 리스트로 만들어 반환
print(list("python")) # ['p', 'y', 't', 'h', 'o', 'n']
print(list((1, 2, 3))) # [1, 2, 3]

a = [1, 2, 3]
b = list(a)
print(b) # [1, 2, 3]

# map
# map(f, iterable)은 함수(f)와 반복 가능한 데이터를 입력으로 받는다.
# 입력받은 데이터의 각 요소에 함수 f를 적용한 결과를 반환
# map 함수는 map 객체를 반환한다.
# 리스트를 입력받아 각 요소에 2를 곱해 반환하는 함수
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result

result = two_times([1, 2, 3, 4])
print(result) # [2,4,6,8]

def two_times(x):
    return x * 2

print(list(map(two_times, [1, 2, 3, 4]))) # [2, 4, 6, 8]

# lambda 사용
print(list(map(lambda a: a*2, [1, 2, 3, 4])))

# max
# max(iterable)는 반복 가능한 데이터를 입력받아 최댓값을 반환
print(max([1,2,3])) # 3
print(max("python")) # y

# min
# min(iterable)는 max 함수와 반대로,
# 반복 가능한 데이터를 입력받아 최솟값을 반환
print(min([1,2,3])) # 1
print(min("python")) # h

# oct
# oct(x)는 정수를 8진수 문자열로 바꾸어 반환
print(oct(34)) # 0o42
print(oct(12345)) # 0o30071

# open
# open(filename, [mode])은 '파일 이름'과 '읽기 방법'을 입력받아
# 파일 객체를 반환
# 읽기 방법(mode)을 생략하면
# 기본값인 읽기 모드(r)로 파일 객체를 만들어 반환
# w: 쓰기 모드로 파일 열기
# r: 읽기 모드로 파일 열기
# a: 추가 모드로 파일 열기
# b: 바이너리 모드로 파일 열기
# f = open("binary_file", "rb")

# ord
# ord(c)는 문자의 유니코드 숫자 값을 반환
print(ord('a')) # 97
print(ord('가')) # 44032

# pow
# pow(x, y)는 x를 y제곱한 결괏값을 반환
print(pow(2, 4)) # 16
print(pow(3, 3)) # 27

# range
# range([start,] stop [,step])은 for 문과 함께 자주 사용하는 함수
# 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 반환
# 시작 숫자를 지정하지 않으면 range 함수는 0부터 시작한다.
print(list(range(5))) # [0, 1, 2, 3, 4]
print(list(range(5, 10))) # [5, 6, 7, 8, 9]
# 세 번째 인수는 숫자 사이의 거리를 말한다.
print(list(range(1, 10, 2))) # [1, 3, 5, 7, 9]
print(list(range(0, -10, -1)))
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

# round
# round(number [,ndigits])는 숫자를 입력받아 반올림해 반환
print(round(4.6)) # 5
print(round(4.2)) # 4
print(round(5.678, 2)) # 5.68

# sorted
# sorted(iterable)는 입력 데이터를 정렬한 후 그 결과를 리스트로 반환
print(sorted([3,1,2])) # [1, 2, 3]
print(sorted(['a','c','b'])) # ['a','b','c']
print(sorted("zero")) # ['e','o','r','z']
print(sorted((3, 2, 1))) # [1, 2, 3]

# str
# str(object)는 객체를 문자열 형태로 변환하여 반환
print(str(3)) # 3
print(str('hi')) # hi

# sum
# sum(iterable)은 입력 데이터의 합을 반환
print(sum([1,2,3])) # 6
print(sum((4,5,6))) # 15

# tuple
# tuple(iterable)은 반복 가능한 데이터를 튜플로 바꾸어 반환하는 함수
# 입력이 튜플인 경우에는 그대로 반환한다.
print(tuple("abc")) # ('a','b','c')
print(tuple([1,2,3])) # (1, 2, 3)
print(tuple((1,2,3))) # (1, 2, 3)

# type
# type(object)는 입력값의 자료형이 무엇인지 알려 주는 함수
print(type("abc")) # <class 'str'>
print(type([])) # <class 'list'>
print(type(open("test", 'w'))) # <class '_io.TextIOWarpper'>

# zip
# zip(*iterable)은 동일한 개수로 이루어진 데이터들을 묶어서 반환
print(list(zip([1,2,3], [4,5,6]))) # [(1, 4), (2, 5), (3, 6)]
print(list(zip([1,2,3],[4,5,6],[7,8,9])))
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print(list(zip("abc", "def")))
# [('a', 'd'), ('b', 'e'), ('c', 'f')]




