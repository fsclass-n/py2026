# 대응 관계를 나타내는 자료형을 딕셔너리라고 하고,
# '연관 배열(associative array)'또는 '해시(hash)'라고도 한다.
# 딕셔너리는 Key와 Value를 한 쌍으로 가지는 자료형이다.
# 딕셔너리는 리스트나 튜플처럼 순차적으로(sequential) 해당 요솟값을 구하지 않고
# Key를 통해 Value를 얻는다.
# 파이썬 3.7 이후 딕셔너리 순서 보장
# {Key1: Value1, Key2: Value2, Key3: Value3, ...}
# Key와 Value의 쌍 여러 개가 {}로 둘러싸여 있다.
# 각각의 요소는 Key: Value 형태로 이루어져 있고 쉼표(,)로 구분되어 있다.
dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
a = {1: 'hi'}
a = {'a': [1, 2, 3]}

# 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
print(a) # {1: 'a', 2: 'b'}

a['name'] = 'pey'
print(a) # {1: 'a', 2: 'b', 'name': 'pey'}

a[3] = [1, 2, 3]
print(a) # {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# 딕셔너리 요소 삭제하기
# del은 파이썬의 예약어로,
# del a[key]처럼 사용하면 지정한 Key에 해당하는 {Key: Value} 쌍이 삭제된다.
del a[1]
print(a) # {2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# 사람 이름과 특기를 한 쌍으로 묶은 딕셔너리
# {"김연아": "피겨스케이팅", "류현진": "야구", "손흥민": "축구", "귀도": "파이썬"}

# 딕셔너리에서 Key를 사용해 Value 얻기
# 딕셔너리는 단 1가지 방법뿐이다. 바로 Key를 사용해서 Value를 구하는 방법이다.
# 어떤 Key의 Value를 얻으려면 '딕셔너리_변수_이름[Key]'를 사용해야 한다.
grade = {'pey': 10, 'julliet': 99}
print(grade['pey']) # 10
print(grade['julliet']) # 99

a = {1: 'a', 2: 'b'}
# 딕셔너리 변수에서 [] 안의 숫자 1은 두 번째 요소를 나타내는 것이 아니라
# Key에 해당하는 1을 나타낸다.
print(a[1]) # a
print(a[2]) # b

a = {'a': 1, 'b': 2}
print(a['a']) # 1
print(a['b']) # 2

dic = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
print(dic['name']) # pey
print(dic['phone']) # 010-9999-1234
print(dic['birth']) # 1118

# 딕셔너리 만들 때 주의할 사항
# 딕셔너리에서 Key는 고유한 값이므로
# 중복되는 Key 값을 설정하면 하나를 제외한 나머지 것들이 모두 무시된다.
# KeyError: 'a'
a = {1: 'a', 1: 'b'} # error
print(a) # {1: 'b'}

# Key에 리스트는 쓸 수 없다는 것이다. 하지만 튜플은 Key로 쓸 수 있다.
# 딕셔너리의 Key로 쓸 수 있느냐, 없느냐는
# Key가 변하는(mutable) 값인지, 변하지 않는(immutable) 값인지에 달려 있다.
# 단, Value에는 변하는 값이든, 변하지 않는 값이든 아무 값이나 넣을 수 있다.
# TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
# a = {[1, 2]: 'hi'} -> error

# 딕셔너리 관련 함수
# key 리스트 만들기 - keys
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
# a.keys()는 딕셔너리 a의 Key만을 모아 dict_keys 객체를 반환한다.
print(a.keys()) # dict_keys(['name', 'phone', 'birth'])
# 파이썬 2.7 버전까지는 a.keys() 함수를 호출하면 dict_keys가 아닌 리스트를 반환했다.
# 파이썬 3.0 이후 버전에서는 keys, values, items 함수가
# 리스트 대신 view 객체(dict_keys, dict_values, dict_items)를 반환한다.
# 3.0 이후 버전에서 반환값으로 리스트가 필요한 경우에는
# list(a.keys())를 사용하면 된다.
print(list(a.keys())) # ['name', 'phone', 'birth']

# Value 리스트 만들기 - values
print(a.values()) # dict_values(['pey', '010-9999-1234', '1118'])

# key, value 쌍 얻기 - items
print(a.items()) # dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1118')])

# key:value 쌍 모두 지우기 - clear
# clear 함수는 딕셔너리 안의 모든 요소를 삭제한다.
a.clear()
print(a) # {}

# key로 value 얻기 - get
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
# get(x) 함수는 x라는 Key에 대응되는 Value를 반환한다.
# a.get('name')은 a['name']을 사용했을 때와 동일한 결괏값을 반환한다.
print(a.get('name')) # pey
print(a['name'])
print(a.get('phone')) # 010-9999-1234

# 딕셔너리에 존재하지 않는 키로 값을 가져오려고 할 경우,
# a['nokey'] 방식은 오류를 발생시키고 a.get('nokey') 방식은 None을 반환한다
a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
print(a.get('nokey')) # none
# print(a['nokey']) -> error

# 딕셔너리 안에 찾으려는 Key가 없을 경우,
# 디폴트 값을 대신 가져오게 하고 싶을 때는 get(x, '디폴트 값')을 사용
print(a.get('nokey', '정보없음')) # '정보없음'

# 해당 key가 딕셔너리 안에 있는지 조사하기 - in
a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
print('name' in a) # True
print('email' in a) # False

# key로 value 얻기 - pop
a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
phone = a.pop('phone')
print(phone) # 010-9999-1234
print(a) # {'name': 'pey', 'birth': '1118'}

# pop(x) 함수는 딕셔너리에서 key가 x인 항목을 삭제한 후 그 value를 반환한다.
email = a.pop('email', '정보없음')
print(email) # 정보없음

