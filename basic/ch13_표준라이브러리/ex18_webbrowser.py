# webbrowser는
# 파이썬 프로그램에서 시스템 브라우저를 호출할 때 사용하는 모듈이다.
# 파이썬으로 웹 페이지를 새 창으로 열려면
# webbrowser 모듈의 open_new() 함수를 사용해야 한다.
import webbrowser

webbrowser.open_new('http://python.org')

# 이미 열린 브라우저로 원하는 사이트를 열고 싶다면
# open_new() 대신 open()을 사용하면 된다.
webbrowser.open('http://python.org')