# 함수의 Docstring
# 함수에 대한 설명을 문서화
# 함수의 첫 번째 줄에 삼중 따옴표로 둘러싼 문자열을 작성하면 된다.
def add(a, b):
    """
    두 숫자를 더하는 함수
    Parameter:
    a (int, float): 첫 번째 숫자
    b (int, float): 두 번째 숫자

    Returns:
    int, float: 두 숫자의 합
    """
    return a + b

# Docstring 확인하기
print(add.__doc__)