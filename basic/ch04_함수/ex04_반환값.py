# 함수의 반환값은 언제나 하나이다
# 2개의 입력 인수를 받아 더한 값과 곱한 값을 반환
def add_and_mul(a, b):
    return a + b, a * b

# a+b와 a*b는 튜플값 하나인 (a+b, a*b)로 반환된다.
result = add_and_mul(3, 4)
print(result) # (7, 12)

result1, result2 = add_and_mul(3, 4)
print(result1, result2) # 7 12

# 함수는 return 문을 만나는 순간,
# 반환값을 반환한 다음 함수를 빠져나간다.
def add_and_mul(a, b):
    return a+b
    return a*b

result = add_and_mul(2, 3)
print(result) # 5

# 반환값이 없는 함수에서 return으로 함수를 빠져나가는 방법
# return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다.
def say_nick(nick):
    if nick == "야호":
        return
    print("나의 별명은 %s 입니다." % nick)

say_nick('야호')
say_nick('호호') # 나의 별명은 호호 입니다.