# shutil
# 파일을 복사(copy)하거나 이동(move)할 때 사용하는 모듈
# 문제:
# 작업 중인 파일을 자동으로 백업하는 기능을 구현
# 단, a.txt는 temp 폴더에 만들어 있다.
import shutil

shutil.copy("d:/temp/a.txt", "d:/temp/b.txt")
shutil.copy("d:/temp/a.txt", "d:/temp/c.txt")

# 문제 : 휴지통으로 삭제하는 기능
# shutil.move로 삭제 기능 만들기
# shutil.move("d:/temp/a.txt.bak", "d:/temp/휴지통/a.txt.bak")
