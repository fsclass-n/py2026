# 1. 파일 생성하기
# open() 함수는 '파일 이름'과 '파일 열기 모드'를 입력값으로 받고
# 결괏값으로 파일 객체를 반환한다.
# 파일_객체 = open(파일_이름, 파일_열기_모드)
# 파일 열기 모드: r(읽기), w(쓰기), a(추가)
# 파일을 쓰기 모드로 열면
# 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 사라지고,
# 해당 파일이 존재하지 않으면 새로운 파일이 생성된다.
# f.close()는 열려 있는 파일 객체를 닫아 주는 역할을 한다.
# 쓰기 모드로 열었던 파일을 닫지 않고 다시 사용하려고 하면 오류가 발생하기 때문이다.
f = open("새파일.txt","w")
f.close()

# '새파일.txt' 파일을 D:/temp 디렉터리에 생성
f = open("D:/temp/새파일.txt","w")
f.close()
f = open("D:\\temp\\새파일.txt","w")
f.close()
# r 문자(raw string)
f = open(r"D:\temp\새파일.txt","w")
f.close()

# 2. 파일을 쓰기 모드로 열어 내용 쓰기
# 인코딩을 명시하지 않으면
# 운영체제마다 다른 기본 인코딩을 사용하여 한글이 깨질 수 있다.
# 어떤 문자를 어떤 숫자로 변환할지 정하는 규칙이 인코딩(Encoding)이다.
# 예를 들어 'A'는 65, 'B'는 66으로 저장하는 식이다.
f = open("새파일.txt","w")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 파일을 읽는 여러 가지 방법
# 1. readline 함수 이용하기
# readline()을 사용해서 파일의 첫 번째 줄을 읽어 출력
f = open("새파일.txt","r")
line = f.readline()
print(line)
f.close()

# 한 줄씩 읽어 출력할 때 줄 끝에 \n 문자가 있으므로 빈 줄도 같이 출력된다.
# 더 이상 읽을 줄이 없으면 break를 수행한다.
# readline()은 더 이상 읽을 줄이 없을 경우 빈 문자열('')을 반환한다.
f = open("새파일.txt","r")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# 2. readlines 함수 사용하기
# readlines 함수는 파일의 모든 줄을 읽어서
# 각각의 줄을 요소로 가지는 리스트를 반환한다.
# lines는 리스트 ["1번째 줄입니다.\n", "2번째 줄입니다.\n", ..., "10번째 줄입니다.\n"]가 된다.
f = open("새파일.txt","r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# 줄 바꿈(\n) 문자 제거하기
# strip() 함수를 사용하면 줄 바꿈 문자를 제거할 수 있다.
f = open("새파일.txt","r")
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)
f.close()

# 3. read 함수 사용하기
# read()는 파일의 내용 전체를 문자열로 반환한다.
f = open("새파일.txt","r")
data = f.read()
print(data)
f.close()

# 파일 객체를 for 문과 함께 사용하기
# 파일 객체(f)는 for 문과 함께 사용하여 파일을 줄 단위로 읽을 수 있다.
f = open("새파일.txt","r")
for line in f:
    print(line)
f.close()

# 파일에 새로운 내용 추가하기
# 쓰기 모드('w')로 파일을 열 때
# 이미 존재하는 파일을 열면 그 파일의 내용이 모두 사라진다.
# 원래 있던 값을 유지하면서 새로운 값만 추가해야 할 경우
# 파일을 추가 모드('a')로 열면 된다.
f = open("새파일.txt","a")
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 파일 처리 시 주의사항
# 어떤 문자를 어떤 숫자로 변환할지 정하는 규칙이 인코딩(Encoding)이다.
# 예를 들어 'A'는 65, 'B'는 66으로 저장하는 식이다.
# 한글 파일 쓰기
with open("한글파일.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요. 파이썬!")

# 한글 파일 읽기
with open("한글파일.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)