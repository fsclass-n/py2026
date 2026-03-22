# 정수형
a = 123
print(a)
a = -178
print(a)
a = 0
print(a)

# 실수형
a = 1.2
print(a)
a = -3.45
print(a)
# e와 E 대소문자 구별 없음!
a = 4.24E10
print(a)
a = 4.24e-10
print(a)
# 8진수(octal)는 0o 또는 0O(숫자 0 + 알파벳 소문자 o 또는 대문자 O)로 시작
a = 0o177
print("8진수:", a)
# 16진수(hexadecimal)는 0x로 시작
a = 0x8ff
b = 0xABC
print(b)

# 사칙 연산
a = 9
b = 2
print(a + b) # 11
print(a - b) # 7
print(a * b) # 18
print(a / b) # 4.5
print(a ** b) # 9의 2승 -> 81
print(a // b) # 9를 2로 나눈 몫 4
print(a % b) # 9를 2로 나눈 나머지 1

# 복합 연산자
# +=, -=, *=, /=, //=, %=, **=
a = 1
a = a + 1
print(a)
a += 1
print(a)

a = 1
a -= 1
print(a)


