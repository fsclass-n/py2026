# 클래스는 왜 필요한가?
# 계산기 프로그램
# 이전에 계산한 결괏값을 유지하기 위해서
# result 전역 변수(global)를 사용했다.
result = 0
def add(num):
    global result
    result += num # 결괏값(result)에 입력값(num) 더하기
    return result # 결괏값 리턴

print(add(3)) # 3
print(add(4)) # 7

# 한 프로그램에서 2대의 계산기가 필요한 상황이 발생
result1 = 0
result2 = 0

def add1(num): # 계산기1
    global result1
    result1 += num
    return result1

def add2(num): # 계산기2
    global result2
    result2 += num
    return result2

print(add1(3)) # 3
print(add1(4)) # 7
print(add2(3)) # 3
print(add2(7)) # 10

# 클래스 사용
# Calculator 클래스로 만든 별개의 계산기
# cal1, cal2(파이썬에서는 이것을 '객체'라고 부른다)
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3)) # 3
print(cal1.add(4)) # 7
print(cal2.add(3)) # 3
print(cal2.add(7)) # 10

# 클래스(class)와 객체
# 과자를 만드는 과자 틀과 이를 사용해 만든 과자이다.
# 과자틀 = 클래스
# 과자 틀로 찍어 낸 과자 = 객체
# 클래스(class)란 똑같은 무언가를 계속 만들어 낼 수 있는 설계 도면(과자 틀)이고,
# 객체(object)란 클래스로 만든 피조물(과자 틀로 찍어 낸 과자)을 뜻한다.
class Cookie:
    pass

# Cookie 클래스의 객체를 만드는 방법
# Cookie()의 결괏값을 리턴받은 a와 b가 바로 객체이다.
a = Cookie()
b = Cookie()

# 객체와 인스턴스의 차이
# 클래스로 만든 객체를 '인스턴스'라고도 한다.
# a = Cookie()로 만든 a는 객체이다.
# a 객체는 Cookie의 인스턴스이다.
# 인스턴스는 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용한다.
# 'a는 인스턴스'보다 'a는 객체'라는 표현이 어울리며
# 'a는 Cookie의 객체'보다 'a는 Cookie의 인스턴스'라는 표현이 훨씬 잘 어울린다.
