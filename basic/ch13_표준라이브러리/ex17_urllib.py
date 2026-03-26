# urllib
# urllib은 URL을 읽고 분석할 때 사용
# 브라우저로 위키독스의 특정 페이지를 읽으려면 다음과 같이 요청하면 된다.
# https://wikidocs.net/페이지_번호 (예: https://wikidocs.net/12)
import ssl
import urllib


# 문제
# 오프라인으로도 읽을 수 있도록 페이지 번호를 입력받아
# 위키독스의 특정 페이지를 wikidocs_페이지_번호.html 파일로
# 저장하는 함수는 어떻게 만들어야 할까?
# get_wikidocs(page)는 위키독스의 페이지 번호를 입력받아
# 해당 페이지의 리소스 내용을 파일로 저장
def get_wikidocs(page):
    resource = 'https://wikidocs.net/{}'.format(page)
    with urllib.request.urlopen(resource) as s:
        with open('wikidocs_%s.html' % page, 'wb') as f:
            f.write(s.read())
# urllib.request.urlopen(resource)로 s 객체를 생성하고
# s.read()로 리소스 내용 전체를 읽어 이를 저장할 수 있다
# 예를 들어 get_wikidocs(12)라고 호출하면
# https://wikidocs.net/12 웹 페이지를
# wikidocs_12.html라는 파일로 저장한다.

# SSL 오류가 발생하면?
context = ssl._create_unverified_context()

def get_wikidocs(page):
    resource = f'https://wikidocs.net/{page}'
    with urllib.request.urlopen(resource, context=context) as s:
        with open(f'wikidocs_{page}.html', 'wb') as f:
            f.write(s.read())

get_wikidocs(12)
