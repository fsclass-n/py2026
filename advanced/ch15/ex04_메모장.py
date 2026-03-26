# 간단한 메모장 만들기
# 1. 필요한 기능? 메모 추가하기, 메모 조회하기
# 2. 입력 값? 메모 내용, 프로그램 실행 옵션
# 3. 출력 값? memo.txt
import sys

# 가장 먼저 해야 할 일은? 메모를 추가하는 것
# python momo.py -a "Life is too short"
# 입력으로 받은 옵션과 메모를 출력
# sys.argv는 프로그램 실행 시
# 입력된 값을 읽어 들이는 파이썬 라이브러리이다.
option = sys.argv[1]
memo = sys.argv[2]

print(option)
print(memo)