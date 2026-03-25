# os
# 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어
# 내 시스템의 환경 변숫값을 알고 싶을 때 - os.environ
import os

print(os.environ)
# os.environ은 환경 변수에 대한 정보를
# 딕셔너리 형태로 구성된 environ 객체로 반환한다.

# 시스템의 PATH 환경 변수 내용
print(os.environ['PATH'])

# 디렉터리 위치 변경하기 - os.chdir
# 현재 디렉터리의 위치를 변경할 수 있다.
#os.chdir("d:/temp")
# 디렉터리 위치 돌려받기 - os.getcwd
# 현재 자신의 디렉터리 위치를 반환한다.
print(os.getcwd())
# 시스템 명령어 호출하기 - os.system
os.system("dir")
# 실행한 시스템 명령어의 결괏값 돌려받기 - os.popen
# os.popen은 시스템 명령어를 실행한 결괏값을 읽기 모드 형태의 파일 객체로 반환
f = os.popen("dir")
# 읽어 들인 파일 객체의 내용을 보려면
print(f.read())
# 디렉터리 생성
os.mkdir("d:/temp/디렉터리")
# 디렉터리 삭제
os.rmdir("d:/temp/디렉터리")
# 파일 지우기
# os.remove("d:/temp/a.txt")
# 파일 이름바꾸기
# os.rename("d:/temp/mod.py", "d:/temp/a.txt")

