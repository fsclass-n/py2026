# 패키지 내 모듈을 미리 import
# __init__.py 파일에 패키지 내의 다른 모듈을 미리 import하면
# 패키지 사용 시 간편하게 접근할 수 있다.
# from .graphic.render import render_test 문장에서
# .graphic.render의 맨 앞 .은 현재 디렉터리를 의미한다.
from .graphic.render import render_test

VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}.")

# 여기에 패키지 초기화 코드를 작성한다.
print("Initializing game...")
