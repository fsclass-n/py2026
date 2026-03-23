# 프로그램 입출력
# sys 모듈 사용하기
# sys 모듈을 사용하여 프로그램에 인수를 전달할 수 있다.
# sys 모듈을 사용하려면 import sys처럼 import 문을 사용해야 한다.
# 자동 임포트: ctrl+.
import sys

args = sys.argv[1:]
for i in args:
    print(i)

# 문자열 관련 함수인 upper()를 사용하여
# 전달된 인수를 모두 대문자로 바꾸어 주는 프로그램
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')

