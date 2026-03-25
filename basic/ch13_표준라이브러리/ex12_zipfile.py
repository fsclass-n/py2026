# zipfile
# 여러 개의 파일을 zip 형식으로 합치거나 이를 해제
import zipfile

# 파일 합치기
# ZipFile 객체의 write() 함수로 개별 파일을 추가할 수 있고
# extractall() 함수를 사용하면 모든 파일을 해제할 수 있다.
with zipfile.ZipFile("mytext.zip", 'w') as myzip:
    myzip.write("d:/temp/a.txt")
    myzip.write("d:/temp/b.txt")
    myzip.write("d:/temp/c.txt")

# 해제하기
# with zipfile.ZipFile("mytext.zip") as myzip:
#     myzip.extractall()

# 합친 파일에서 특정 파일만 해제 - extract() 함수를 사용
# 특정 파일만 해제하기
with zipfile.ZipFile('mytext.zip') as myzip:
    myzip.extract('temp/a.txt')

# 파일을 압축하여 묶고 싶은 경우에는
# compression, compresslevel 옵션을 사용할 수 있다.
# 압축하여 묶기
with zipfile.ZipFile('mytext1.zip', 'w', compression=zipfile.ZIP_LZMA, compresslevel=9) as myzip:
    myzip.write("d:/temp/a.txt")
    myzip.write("d:/temp/b.txt")
    myzip.write("d:/temp/c.txt")

# compression에는 4가지 종류가 있다.
# ZIP_STORED: 압축하지 않고 파일을 zip으로만 묶는다. 속도가 빠르다.
# ZIP_DEFLATED: 일반적인 zip 압축으로 속도가 빠르고 압축률은 낮다(호환성이 좋다).
# ZIP_BZIP2: bzip2 압축으로 압축률이 높고 속도가 느리다.
# ZIP_LZMA: lzma 압축으로 압축률이 높고 속도가 느리다(7zip과 동일한 알고리즘으로 알려져 있다).

# compresslevel은 압축 수준을 의미하는 숫자값으로, 1~9를 사용한다.
# 1은 속도가 가장 빠르지만 압축률이 낮고, 9는 속도는 가장 느리지만 압축률이 높다.