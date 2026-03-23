# 1. 클래스를 어떻게 만들지 먼저 구상하기
# 1) 사칙 연산 클래스: FourCal
# 2) 사칙 연산을 위해 두 숫자를 입력받는다: setdata 메서드
# 3) 더하기 기능은? add 메서드
# 4) 빼기 기능은? sub 메서드
# 5) 곱하기 기능은? mul 메서드
# 6) 나누기 기능은? div 메서드

# a = FourCal()
# a.setdata(4, 2)
# a.add()
# a.mul()
# a.sub()
# a.div()

# 2. 클래스 구조 만들기
# pass는 아무것도 수행하지 않는 문법으로,
# 임시로 코드를 작성할 때 주로 사용한다.
class FourCal:
    pass
a = FourCal()
# type()은 파이썬 내장 함수로, 객체의 타입을 출력한다.
print(type(a)) # <class '__main__.FourCal'>

# 객체에 연산할 숫자 지정하기
# a.setdata(4, 2)

# 클래스 안에 구현된 함수는 다른 말로 메서드(method)라고 부른다.
# 파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다.
# 객체의 메서드를 호출할 때 호출한 객체 자신이 전달되기 때문에
# self라는 이름을 사용한 것이다.
# 물론 self 말고 다른 이름을 사용해도 상관없다.
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

a = FourCal()
# 객체를 이용해 클래스의 메서드를 호출하려면
# a.setdata(4, 2)와 같이 도트(.) 연산자를 사용하면 된다.
#  setdata 메서드의 첫 번째 매개변수 self에는
#  setdata 메서드를 호출한 객체 a가 자동으로 전달
a.setdata(4, 2)

# 메서드를 호출하는 또 다른 방법
#  '클래스명.메서드' 형태로 호출할 때는
#  객체 a를 첫 번째 매개변수 self에 꼭 전달해야 한다.
a = FourCal()
FourCal.setdata(a, 4, 2)

# '객체.메서드' 형태로 호출할 때는
# self를 반드시 생략해서 호출해야 한다.
a = FourCal()
a.setdata(4, 2)

# a.first = 4라는 문장이 수행되면
# a 객체에 객체변수 first가 생성되고 4라는 값이 저장된다.
# 객체에 생성되는 객체변수를 '인스턴스 변수' 또는 '속성'이라고도 부른다.
a = FourCal()
a.setdata(4, 2)
print(a.first) # 4
print(a.second) # 2

# 클래스로 만든 객체의 객체변수는
# 다른 객체의 객체변수에 상관없이 독립적인 값을 유지한다.
a = FourCal()
b = FourCal()
a.setdata(4, 2)
print(a.first) # 4
b.setdata(3, 7)
print(b.first) # 3
print(a.first) # 4

# 더하기 기능 만들기
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 8)
print(a.add()) # 6
print(a.sub()) # 2
print(a.mul()) # 8
print(a.div()) # 2.0
print(b.add()) # 11
print(b.sub()) # -5
print(b.mul()) # 24
print(b.div()) # 0.375