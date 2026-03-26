# 다른 사람들이 만든 프로그램을 자세히 들여다보고
# 분석하는 것부터 시작
# -> 수준에 맞는 소스를 찾는 일
# 가장 먼저 '입력'과 '출력'을 생각

# 구구단
# 2를 입력값으로 주었을 때
# 어떻게 출력되어야 할지 먼저 생각
# 1. 함수 이름은? gugu
# 2. 입력받는 값은? 2
# 3. 출력하는 값은? 2단(2,4,6,8,10,...,18)
# 4. 결과는 어떤 형태로 저장하지? 연속된 자료형 -> 리스트
# result = gugu(2)
# result = [2,4,6,8,...,18]
def gugu(n):
    print(n)

gugu(2)

def gugu(n):
    result = []
    result.append(n*1)
    result.append(n*2)
    result.append(n*3)
    result.append(n*4)
    result.append(n*5)
    result.append(n*6)
    result.append(n*7)
    result.append(n*8)
    result.append(n*9)
    return result

print(gugu(2)) # [2, 4, 6, 8, 10, 12, 14, 16, 18]

i = 1
while i < 10:
    print(i)
    i += 1

def gugu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i += 1
    return result

print(gugu(2)) # [2, 4, 6, 8, 10, 12, 14, 16, 18]

# 프로그래밍을 할 때는
# 매우 구체적으로 접근해야 머리가 덜 아프다는 것을 기억하자.
