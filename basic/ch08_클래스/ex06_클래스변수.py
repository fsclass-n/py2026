# 클래스 변수
# 클래스 안에 변수를 선언하여 생성한다.
from traceback import print_tb


class Family:
    lastname = "김"

# 클래스변수는 클래스_이름.클래스변수로 사용할 수 있다.
print(Family.lastname) # 김


# Family 클래스로 만든 객체를 이용해도
# 클래스변수를 사용할 수 있다.
a = Family()
b = Family()
print(a.lastname) # 김
print(b.lastname) # 김

# 클래스변수의 값을 변경했더니
# 클래스로 만든 객체의 lastname 값도 모두 변경됨을 확인할 수 있다.
# 클래스변수는 객체변수와 달리
# 클래스로 만든 모든 객체에 공유된다는 특징이 있다.
Family.lastname = "박"
print(a.lastname) # 박
print(b.lastname) # 박

# 클래스변수와 동일한 이름의 객체변수를 생성하면?
# 객체변수는 클래스변수와 동일한 이름으로 생성할 수 있다.
a.lastname = "최"
print(a.lastname) # 최
# a.lastname 객체변수를 생성하더라도 
# Family 클래스의 lastname과는 상관없다
print(Family.lastname) # 박
print(b.lastname) # 박
