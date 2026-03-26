# Faker
# Faker는 테스트용 가짜 데이터를 생성할 때 사용하는 라이브러리
from faker.proxy import Faker

# pip을 이용하여 설치
# C:\> python -m pip install Faker

# 이름
fake = Faker()
print(fake.name())

# 한글 이름
fake = Faker('ko-KR')
print(fake.name())

# 주소
print(fake.address())

# 문제
# 테스트 데이터 30건이 필요하다
# [(이름1, 주소1), (이름2, 주소2), ..., (이름30, 주소30)]
test_data = [(fake.name(), fake.address()) for i in range(30)]
print(test_data)

# fake.name()           이름
# fake.address()        주소
# fake.postcode()       우편번호
# fake.country()        국가명
# fake.company()        회사명
# fake.job()            직업명
# fake.phone_number()   전화번호
# fake.email()          이메일 주소
# fake.user_name()      사용자명
# fake.pyint(min_value=0, max_value=100)    0부터 100 사이의 임의의 숫자
# fake.ipv4_private()   IP주소
# fake.text()           임의의 문장
# fake.catch_phrase()   한글 임의의 문장
# fake.color_name()     색상명