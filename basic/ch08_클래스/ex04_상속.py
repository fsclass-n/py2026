# 클래스의 상속
# 상속(Inheritance)이란 '물려받다'라는 뜻
# 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것이다.
# class 클래스_이름(상속할_클래스_이름)
# MoreFourCal 클래스는 FourCal 클래스를 상속했으므로
# FourCal 클래스의 모든 기능을 사용할 수 있다.
from basic.ch08_클래스.ex03_생성자 import FourCal


class MoreFourCal(FourCal):
    pass

a = MoreFourCal(4, 2)
print(a.add()) # 6
print(a.mul()) # 8
print(a.sub()) # 2
print(a.div()) # 2.0

# 상속 기능은 왜 쓰는 걸까?
# 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용한다.

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
print(a.pow()) # 16
print(a.add()) # 6