# functools.reduce
# functools.reduce(function, iterable)은
# 함수(function)를 반복 가능한 객체(iterable)의 요소에
# 차례대로(왼쪽에서 오른쪽으로) 누적 적용하여
# 이 객체를 하나의 값으로 줄이는 함수이다.
import functools


# 문제
# 입력 인수 data의 요소를 모두 더하여 반환하는 add 함수
def add(data):
    result = 0
    for i in data:
        result += i
    return result

data = [1, 2, 3, 4, 5]
result = add(data)
print(result) # 15

data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x + y, data)
print(result) # 15

# reduce()에 선언한 람다 함수를
# data 요소에 차례대로 누적 적용하여 다음과 같이 계산한다.
# ((((1+2)+3)+4)+5)

# 퀴즈
# 최댓값 구하기
num_list = [3, 2, 8, 1, 6, 7]
max_num = functools.reduce(lambda x, y: x if x > y else y, num_list)
print(max_num) # 8

# 최솟값 구하기
min_num = functools.reduce(lambda x, y: x if x < y else y, num_list)
print(min_num) # 1