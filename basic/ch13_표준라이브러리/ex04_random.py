# random
# random은 난수(규칙이 없는 임의의 수)를 발생시키는 모듈이다.
# 0.0에서 1.0 사이의 실수 중에서 난수 값을 반환
import random
print(random.random()) # 0.5291041929571102

# 1에서 10 사이의 정수 중에서 난수 값을 반환
print(random.randint(1, 10)) # 3

# 1에서 55 사이의 정수 중에서 난수 값을 반환
print(random.randint(1, 55)) # 35

# 리스트의 요소 중에서 무작위로 하나를 선택하여 꺼낸 다음 그 값을 반환
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__=="__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))

# random.choice 함수는
# 입력으로 받은 리스트에서 무작위로 하나를 선택하여 반환
def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

# 리스트의 항목을 무작위로 섞고 싶을 때는 random.sample 함수를 사용
data = [1, 2, 3, 4, 5]
print(random.sample(data, len(data))) # [2, 1, 3, 4, 5]
# len(data)는 무작위로 추출할 원소의 개수
print(random.sample(data, 3)) # [5, 4, 2]