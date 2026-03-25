# from game.sound.echo import echo_test로
# 전체 경로를 사용하여 import할 수도 있지만,
# 상대경로로 import할 수도 있다.
# ..은 부모 디렉터리, .은 현재 디렉터리
# from game.sound.echo import echo_test
from ..sound.echo import echo_test
def render_test():
    print("render")
    echo_test()