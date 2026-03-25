# 생성자
from basic.ch08_클래스.ex01_클래스란 import add
from basic.ch08_클래스.ex02_사칙연산클래스 import FourCal

a = FourCal()
# AttributeError: 'FourCal' object has no attribute 'first'
# a.add() # error
# 객체에 first, second와 같은 초깃값을 설정해야 할 필요가 있을 때는
# setdata와 같은 메서드를 호출하여 초깃값을 설정하기보다
# 생성자를 구현하는 것이 안전한 방법이다.

# 생성자(constructor)란 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다.
# 파이썬 메서드명으로 __init__를 사용하면 이 메서드는 생성자가 된다.
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

# a = FourCal()
a = FourCal(4, 2)
print(a.first) # 4
print(a.second) # 2
print(a.add()) # 6
print(a.div()) # 2.0