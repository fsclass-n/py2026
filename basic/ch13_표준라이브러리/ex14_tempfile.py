# tempfile
# 파일을 임시로 만들어서 사용
# tempfile.mkstemp()는 중복되지 않는 임시 파일을 만들고
# (파일 디스크립터, 파일 경로) 형태의 튜플을 반환한다.
import tempfile

fd, path = tempfile.mkstemp()
print(path)

# tempfile.TemporaryFile()은 임시 저장 공간으로 사용할 파일 객체를 반환한다.
# 이 파일은 기본적으로 바이너리 쓰기 모드(wb)를 갖는다.
# f.close()가 호출되면 이 파일은 자동으로 삭제된다.
f = tempfile.TemporaryFile()
f.close()