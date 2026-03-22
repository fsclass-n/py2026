# 입력값이 몇 개가 될지 모를 때
# def 함수_이름(*매개변수)
#   수행할_문장
#   ...

# 여러 개의 입력값을 모두 더하는 함수
# *args처럼 매개변수 이름 앞에 *을 붙이면
# 입력값을 전부 모아 튜플로 만들어 주기 때문이다.
# args는 인수를 뜻하는 영어 단어 arguments의 약자이며 관례적으로 자주 사용한다.
# *args는 임의로 정한 변수 이름이다. *pey, *python처럼 아무 이름이나 써도 된다.
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

result = add_many(1, 2, 3)
print(result) # 6
result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result) # 55

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

result = add_mul("add", 1, 2, 3, 4, 5)
print(result) # 15
result = add_mul("mul", 1, 2, 3, 4, 5)
print(result) # 120
