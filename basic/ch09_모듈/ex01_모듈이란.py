# 모듈이란 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일이다.
# 다른 파이썬 프로그램에서 불러와 사용할 수 있게 만든 파이썬 파일이라고도 할 수 있다.
# 모듈 불러오기(ctrl+.)
# import는 이미 만들어 놓은 파이썬 모듈을 사용할 수 있게 해 준다.
# import는 현재 디렉터리에 있는 파일이나
# 파이썬 라이브러리가 저장된 디렉터리에 있는 모듈만 불러올 수 있다.
# 파이썬 라이브러리는 파이썬을 설치할 때 자동으로 설치되는 파이썬 모듈을 말한다.
# import 모듈_이름
import mod1

# mod1.py 파일에 있는 add 함수를 사용하려면
# mod1.add처럼 모듈 이름 뒤에 도트 연산자(.)를 붙이고 함수 이름을 쓰면 된다.
print(mod1.add(3, 4)) # 7
print(mod1.sub(4, 2)) # 2

# from 모듈_이름 import 모듈_함수
from mod1 import add
print(add(3, 4)) # 7

# from 모듈_이름 import 모듈_함수1, 모듈_함수2
from mod1 import add, sub
# * 문자는 '모든 것'이라는 의미로
# mod1 모듈의 모든 함수를 불러와 사용하겠다는 뜻이다.
from mod1 import *

# if __name__ == "__main__": 의 의미
import mod2
import mod3
# __name__ 변수란?
print(mod1.__name__) # mod1
# 직접 mod1.py 파일을 실행할 경우,
# mod1.py의 __name__ 변수에는 __main__ 값이 저장된다.
# 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import할 경우에는
# mod1.py의 __name__ 변수에 mod1.py의 모듈 이름인 mod1이 저장된다.

# 클래스나 변수 등을 포함한 모듈
import mod4
print(mod4.PI) # 3.141592
a = mod4.Math()
print(a.solv(2)) # 12.566368
print(mod4.add(mod4.PI, 4.4)) # 7.5415920000000005

# 다른 파일에서 모듈 불러오기
import mod4
result = mod4.add(3, 4)
print(result) # 7

# 다른 디렉터리에 있는 모듈을 불러오는 방법
# sys.path.append 사용하기
# sys 모듈은 파이썬을 설치할 때 함께 설치되는 라이브러리 모듈이다.
# sys 모듈을 사용하면 파이썬 라이브러리가 설치되어 있는 디렉터리를 확인할 수 있다.
import sys
# sys.path는 파이썬 라이브러리가 설치되어 있는 디렉터리 목록을 보여 준다.
# 이 디렉터리 안에 저장된 파이썬 모듈은
# 모듈이 저장된 디렉터리로 이동할 필요 없이 바로 불러 사용할 수 있다.
print(sys.path)
# sys.path.append를 사용해서
# D:/temp 디렉터리를 sys.path에 추가했다.
sys.path.append("d:/temp")
print(sys.path)
# 디렉터리 이동 없이 바로 모듈을 불러와서 사용할 수 있다.
import mod5
print(mod5.mul(3, 4)) # 12