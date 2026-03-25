# 예외 만들기
# 예외는 파이썬 내장 클래스인 Exception 클래스를 상속하여 만들 수 있다.
class MyError(Exception):
    pass

# 별명을 출력하는 함수
def say_nick(nick):
    if nick == '하하':
        raise MyError()
    print(nick)

# say_nick("나나")
# say_nick("하하")

try:
    say_nick("나나")
    say_nick("하하")
except MyError:
    print("허용되지 않는 별명입니다.")

# print(e)로 오류 메시지가 출력되지 않는 것을 확인할 수 있다.
try:
    say_nick("쵸코")
    say_nick("하하")
except MyError as e:
    print(e)

# 오류 메시지가 보이게 하려면
# 오류 클래스에 __str__ 메서드를 구현해야 한다.
# __str__ 메서드는 print(e)처럼
# 오류 메시지를 print 문으로 출력할 경우에 호출되는 메서드이다.
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

try:
    say_nick("딸기")
    say_nick("하하")
except MyError as e:
    print(e)