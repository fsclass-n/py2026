# 함수 안에서 선언한 변수의 효력 범위
# 함수 안에서 사용하는 매개변수는 함수 밖의 변수 이름과는 전혀 상관없다.
# a = 1
# def vartest(a):
#     a += 1
#
# vartest(a)
# print(a) # 1

# 함수 안에서 선언한 매개변수는 함수 안에서만 사용될 뿐,
# 함수 밖에서는 사용되지 않는다.
# def vartest(a):
#     a += 1
#
# vartest(3)
# # NameError: name 'a' is not defined
# print(a) # error

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용하기
a = 1
def vartest(a):
    a += 1
    return a

a = vartest(a)
print(a) # 2

# 2. global 명령어 사용하기
# 함수 안의 global a 문장은 함수 안에서 함수 밖의 a 변수를 직접 사용하겠다는 뜻이다.
# 프로그래밍을 할 때 global 명령어는 사용하지 않는 것이 좋다.
# -> 함수는 독립적으로 존재하는 것이 좋기 때문이다.
a = 1
def vartest():
    global a
    a += 1

vartest()
print(a) # 2

# 리스트는 '변경 가능한(mutable)' 자료형
# 리스트나 딕셔너리를 함수에 전달할 때는 원본이 변경될 수 있다
def change_list(my_list):
    my_list.append(4) # 리스트에 값을 추가

a = [1, 2, 3]
change_list(a)
print(a) # [1, 2, 3, 4]

