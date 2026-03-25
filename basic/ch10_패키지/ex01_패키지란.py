# 패키지(packages)란 관련 있는 모듈의 집합이다.
# 파이썬에서 모듈은 하나의 .py 파일이다.
# 파이썬 패키지는 디렉터리와 파이썬 모듈로 이루어진다.
# 패키지 만들기

# \> set PYTHONPATH=D:/temp
# \> python

# 패키지 안의 함수 실행하기
# 첫 번째는 echo 모듈을 import하여 실행하는 방법
# >>> import game.sound.echo
# >>> game.sound.echo.echo_test()
# >>> exit()

# 두 번째는 echo 모듈이 있는 디렉터리까지를
# from ... import하여 실행하는 방법
# :\> python
# >>> from game.sound import echo
# >>> echo.echo_test()

# 세 번째는 echo 모듈의 echo_test 함수를 직접 import하여 실행하는 방법
# >>> from game.sound.echo import echo_test
# >>> echo_test()

# __init__.py의 용도
# __init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다.
# 만약 game, sound, graphic 등 패키지에 포함된 디렉터리에
# __init__.py 파일이 없다면 패키지로 인식되지 않는다.
# python 3.3 버전부터는 __init__.py 파일이 없어도 패키지로 인식한다.
# 하지만 하위 버전 호환을 위해 __init__.py 파일을 생성하는 것이 안전하다.

# 패키지 변수 및 함수 정의
# __init__.py 파일에 공통 변수나 함수를 정의할 수 있다.
# >>> import game
# print(game.VERSION) # 3.5
# game.print_version_info()

# 패키지 내 모듈을 미리 import
# __init__.py 파일에 패키지 내의 다른 모듈을 미리 import하면
# 패키지 사용 시 간편하게 접근할 수 있다.

# 패키지 초기화
# __init__.py 파일에 패키지를 처음 불러올 때 실행할 코드를 작성할 수 있다.
# 데이터베이스 연결이나 설정 파일 로드 같은 작업을 수행할 수 있다.
# game 패키지의 초기화 코드는 하위 모듈의 함수를 import할 경우에도 실행된다.
# 단, 초기화 코드는 한 번 실행된 후에는 다시 import해도 실행되지 않는다.

# __all__ 변수
# 특정 디렉터리의 모듈을 *로 import할 때는
# 해당 디렉터리의 __init__.py 파일에
# __all__ 변수를 설정하고 import할 모듈을 정의해야 한다.

# 상대경로 패키지
