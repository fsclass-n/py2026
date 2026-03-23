# 파일을 열면(open) 항상 닫아(close) 주어야 한다.
f = open("foo.txt", "w")
f.write("Life is too short, you need python")
f.close()

# with 문과 함께 사용하기
# with 문을 사용하면 with 블록(with 문에 속해 있는 문장)을 벗어나는 순간
# 열린 파일 객체 f가 자동으로 닫힌다.
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")

# 파일이 닫혔는지 확인하기
# f.closed는 파일이 닫혔으면 True, 열려 있으면 False를 반환한다.
with open("foo.txt", "w") as f:
    f.write("Hello")
    print(f.closed) # False (아직 열려 있음)
print(f.closed) # True (with 블록을 벗어나 자동으로 닫힘)
