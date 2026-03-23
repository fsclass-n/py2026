# 입력값이 몇 개가 될지 모를 때
# 1. 가변 매개변수, *args
# 여러 개의 입력값을 받는 함수
# def 함수_이름(*매개변수)
#   수행할_문장
#   ...

# 여러 개의 입력값을 모두 더하는 함수
# *args처럼 매개변수 이름 앞에 *을 붙이면
# 입력값을 전부 모아 튜플로 만들어 주기 때문이다.
# *args는 임의로 정한 변수 이름이다. *pey, *python처럼 아무 이름이나 써도 된다.
# args는 인수를 뜻하는 영어 단어 arguments의 약자이며 관례적으로 자주 사용한다.
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

# 2. 키워드 매개변수, **kwargs
# 함수 호출 시 키워드=값 형태로 전달하는 매개변수를 받을 때 사용한다.
# 키워드 매개변수를 사용할 때는 매개변수 앞에 별 2개(**)를 붙인다.
# 입력받은 키워드 매개변수들을 딕셔너리 형태로 출력
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1) # {'a': 1}
print_kwargs(name='foo', age=3) # {'name': 'foo', 'age': 3}
print_kwargs(name='홍길동', age=25, city='서울', job='개발자')
# {'name': '홍길동', 'age': 25, 'city': '서울', 'job': '개발자'}

def create_profile(**info):
    print("=== 프로필 정보 ===")
    for key, value in info.items():
        print(f"{key}: {value}")

create_profile(이름='길철수', 나이=30, 직업='프로그래머', 취미='독서')

# 일반 매개변수, 가변 매개변수(*args), 키워드 매개변수(**kwargs)를 모두 함께 사용
# 순서는 반드시 다음과 같아야 한다.
def mixed_function(name, *args, **kwargs):
    print(f"이름: {name}")
    print(f"추가 인수들: {args}")
    print(f"키워드 인수들: {kwargs}")

mixed_function('홍길동',1,2,3, age=25, city='서울')