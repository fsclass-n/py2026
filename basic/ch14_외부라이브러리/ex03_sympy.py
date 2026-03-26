# sympy
# sympy는 방정식 기호(symbol)를 사용하게 해 주는 외부 라이브러리
from fractions import Fraction
import sympy

# 문제
# 시윤이는 가진 돈의 2/5로 학용품을 샀다고 한다.
# 학용품을 사는 데 쓴 돈이 1,760원이라면
# 남은 돈은 어떻게 구하면 될까?
# sympy.symbols()는
# x처럼 방정식에 사용하는 미지수를 나타내는 기호를 생성할 때 사용한다.
# 가지고 있던 돈을 x라고 하자.
x = sympy.symbols("x")

# x, y 2개의 미지수가 필요하다면?
x, y = sympy.symbols("x y")

# 시윤이가 가진 돈의 2/5는 1,760원,
# 즉 일차방정식 ㅌ * (2/5) = 1750이므로
# sympy.Eq(a, b)는 a와 b가 같다는 방정식이다.
# Fraction은 유리수를 표현할 때 사용하는 표준 라이브러리로,
# 2/5를 정확하게 계산하려고 사용했다.
# 가지고 있던 돈의 2/5가 1760원이므로
# 방정식은 x * (2/5) = 1760 이다.
f = sympy.Eq(x*Fraction('2/5'), 1760)

# fractions.Fraction으로 유리수 연산하기
a = Fraction(1, 5)
print(a) # 1/5
a = Fraction('1/5')
print(a) # 1/5

# 방정식을 만족하는 값(result)을 구한다.
result = sympy.solve(f) # 결괏값은 리스트
print(result) # [4400]

# 남은 돈은 가지고 있던 돈에서 1760원을 빼면 된다.
remains = result[0] - 1760
print('남은 돈은 {}원 입니다.'.format(remains))
# 남은 돈은 2640원입니다.

# x의제곱 = 1과 같은 2차 방정식의 해
x = sympy.Symbol('x')
f = sympy.Eq(x**2, 1)
print(sympy.solve(f)) # [-1, 1]

# 연립방정식의 해
# x + y = 10
# x - y = 4
x, y = sympy.symbols('x y')
f1 = sympy.Eq(x+y, 10)
f2 = sympy.Eq(x-y, 4)
print(sympy.solve([f1, f2])) # {x: 7, y: 3}
# 미지수가 2개 이상이면
# 결괏값이 리스트가 아닌 딕셔너리라는 점에 주의하자.