# with 문과 변수 스코프
# 함수가 변수의 유효 범위를 나누는 주요 기준이고,
# if, for, while, with 같은 코드 블록은 별도 지역 스코프를 만들지 않는다

# 1. 함수 스코프:
# 함수 안에서 선언된 변수는 함수 밖에서 접근할 수 없다.
# 함수는 독립적인 공간이라고 생각하면 된다.
def my_function():
    func_var = "함수 안의 변수"

my_function()
# NameError: name 'func_var' is not defined
# print(func_var) # error -> 함수 밖에서는 접근 불가

# 2. 코드 블록:
# if, for, while, with 블록 안에서 선언한 변수는
# 같은 함수(또는 모듈) 범위라면 블록 밖에서도 접근할 수 있다.
# if 문 블록의 예
if True:
    if_var = "if 블록 안의 변수"

print(if_var) # 정상 작동! "if 블록 안의 변수" 출력

# for 문 블록의 예
for i in range(3):
    loop_var = "반복문 안의 변수"

print(i)    # 정상 작동! 2 출력
print(loop_var) # 정상 작동! "반복문 안의 변수" 출력

# with 문에서도 블록 안에서 선언된 변수를 블록 밖에서 접근할 수 있다.
with open("test.txt", "w") as f:
    content = "Hello, Python!" # with 블록 내에서 변수 선언
    f.write(content)

# with 블록을 벗어난 후에도 변수에 접근 가능
print(content) # "Hello, Python!" 출력