# traceback
# 프로그램 실행 중 발생한 오류를 추적
def a():
    return 1/0

def b():
    a()

def main():
    try:
        b()
    except:
        print("오류가 발생했습니다.")

main()


# traceback 모듈의 format_exc()는 오류 추적 결과를 문자열로 반환
import traceback

def a():
    return 1/0

def b():
    a()

def main():
    try:
        b()
    except:
        print("오류가 발생했습니다.")
        print(traceback.format_exc())

main()