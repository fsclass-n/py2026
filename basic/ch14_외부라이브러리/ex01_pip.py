# pip
# 파이썬 모듈이나 패키지를 쉽게 설치할 수 있도록 도와주는 도구이다.
# 의존성 있는 모듈이나 패키지를 자동으로 함께 설치
# 설치 확인:
# 터미널에서
# pip --version

# pip install
# PyPI(Python Package Index)는 파이썬 소프트웨어가 모인 저장 공간이다.
# window: python -m pip install SomePackage
# mac: python3 -m pip install SomePackage 또는
# mac: python -m pip install SomePackage

# pip uninstall
# 설치한 패키지를 삭제
# python -m pip uninstall SomePackage

# 특정 버전으로 설치하기
# python -m pip install SomePackage==1.0.4
# 버전을 생략하면 최신 버전으로 자동 설치된다.
# python -m pip install SomePackge

# 최신 버전으로 업그레이드하기
# 패키지를 최신 버전으로 업그레이드하려면 --upgrade 옵션을 사용한다.
# python -m pip install --upgrage SomePackage

# 설치된 패키지 확인하기
# python -m pip list
