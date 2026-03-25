# glob
# 특정 디렉터리에 있는 파일 이름 모두를 알아야 할 때
# 디렉터리에 있는 파일들을 리스트로 만들기 - glob(pathname)
import glob

print(glob.glob("d:/temp/*.*"))
# ?는 1자리 문자열, *은 임의의 길이의 문자열을 의미한다.
