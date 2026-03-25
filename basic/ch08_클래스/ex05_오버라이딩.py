# 메서드 오버라이딩(method overriding)
# 부모 클래스(상속한 클래스)에 있는 메서드를
# 동일한 이름으로 다시 만드는 것
# 이렇게 메서드를 오버라이딩하면
# 부모 클래스의 메서드 대신 오버라이딩한 메서드가 호출된다.
from basic.ch08_클래스.ex03_생성자 import FourCal

a = FourCal(4, 0)
# ZeroDivisionError: division by zero
# a.div() # error

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0: # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
print(a.div()) # 0
