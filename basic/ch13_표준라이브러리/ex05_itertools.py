# itertools.zip_longest
#  유치원생 5명에게 간식을 나누어 주고자

students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초콜릿', '젤리']

# 간식의 개수가 유치원생보다 적으므로
# 다음과 같은 결과가 나온다.
# 더 적은 snacks의 개수만큼만 zip()으로 묶게 된다.
result = zip(students, snacks)
print(list(result))

# itertools.zip_longest(*iterables, fillvalue=None) 함수는
# 같은 개수의 자료형을 묶는 파이썬 내장 함수인 zip 함수와 똑같이 동작한다.
# 하지만 itertools.zip_longest() 함수는
# 전달한 반복 가능 객체(*iterables)의 길이가 서로 다르면
# 긴 객체의 길이에 맞춰 fillvalue에 설정한 값을 짧은 객체에 채울 수 있다.

# students의 요소 개수가 snacks보다 많을 때
# 그만큼을 '새우깡'으로 채우려면 어떻게 해야 할까?
# 요소 개수가 많은 것을 기준으로
# 자료형을 묶는 itertools.zip_longest()를 사용하면 된다.
# 부족한 항목은 None으로 채우는데,
# fillvalue로 값을 지정하면 None 대신 다른 값으로 채울 수 있다.
import itertools
result = itertools.zip_longest(students, snacks, fillvalue='새우깡')
print(list(result))
# [('한민서', '사탕'), ('황지민', '초콜릿'), ('이영철', '젤리'), ('이광수', '새우깡'), ('김승민', '새우깡')]

# 순열(permutations)
# itertools.permutations
# itertools.permutations(iterable, r)은
# 반복 가능 객체 중에서 r개를 선택한 순열을 이터레이터로 반환하는 함수이다.
# 상황:
# 1, 2, 3이라는 숫자가 적힌 3장의 카드에서
# 2장의 카드를 꺼내 만들 수 있는 2자리 숫자를 모두 구하려면 어떻게 해야 할까?
print(list(itertools.permutations(['1', '2', '3'], 2)))
# [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
for a, b in itertools.permutations(['1', '2', '3'], 2):
    print(a, b)

# 조합(combinations)
# itertools.combinations(iterable, r)은
# 반복 가능 객체 중에서 r개를 선택한 조합을 이터레이터로 반환하는 함수이다.

# 3장의 카드에서 순서에 상관없이 2장을 고르는 조합은
# 다음처럼 itertools.combinations()를 사용하면 된다.
print(list(itertools.combinations(['1', '2', '3'], 2)))
# [('1', '2'), ('1', '3'), ('2', '3')]

# 퀴즈
# 1~45 중 서로 다른 숫자 6개를 뽑는 로또 번호의 모든 경우의 수(조합)를 구하고
# 그 개수를 출력하려면 어떻게 해야 할까?
# 이터레이터 객체를 루프를 이용하여 출력하면 아마 끝도 없이 출력될 것이다.
it = itertools.combinations(range(1, 46), 6)
# for num in it:
#     print(num)

# 순환하여 출력하지 않고 이터레이터의 개수만 세려면
print(len(list(itertools.combinations(range(1, 46), 6)))) # 8145060

# 중복 조합을 사용하는 함수
# 퀴즈
# 로또 복권이 숫자 중복을 허용하도록 규칙이 변경된다면 경우의 수는 몇 개가 될까?
# 같은 숫자를 허용하는 중복 조합은
# itertools.combinations_with_replacement()를 사용하면 된다.
print(len(list(itertools.combinations_with_replacement(range(1, 46), 6)))) # 15890700