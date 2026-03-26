# json
# 인터넷으로 얻은 myinfo.json 파일을 읽어
# 파이썬에서 처리할 수 있도록 딕셔너리 자료형으로 만들려면?
import json

# JSON 파일을 읽을 때는 json.load(파일_객체)를 사용한다.
# load() 함수는 읽은 데이터를 딕셔너리 자료형으로 반환한다.
with open('myinfo.json') as f:
    data = json.load(f)

type(data)
print(data)

# 딕셔너리 자료형을 JSON 파일로 생성할 때는
# json.dump(딕셔너리, 파일_객체)를 사용한다.
data = {'name': '홍길동', 'birth': '0525', 'age': 30}
with open('myinfo.json', 'w') as f:
    json.dump(data, f)

# 파이썬 자료형을 JSON 문자열로 만드는 방법
# 딕셔너리 자료형을 JSON 문자열로 만들려면
# json.dumps() 함수를 사용하면 된다.
d = {"name": "홍길동", "birth": "0525", "age": 30}
json.data = json.dumps(d)
print(json_data)

# JSON 문자열을 딕셔너리로 변환
print(json.loads(json_data))

# 한글 문자열이 아스키 형태의 문자열로 변경되는 것을 방지
# ensure_ascii=False 옵션을 사용하면 된다.
# 이 옵션은 데이터를 저장할 때 아스키 형태로 변환하지 않겠다는 뜻이다.
d = {"name": "홍길동", "birth": "0525", "age": 30}
json_data = json.dumps(d, ensure_ascii=False)
print(json_data)
json.loads(json_data)

# JSON 문자열을 정렬
d = {"name": "홍길동", "birth": "0525", "age": 30}
print(json.dumps(d, indent=2, ensure_ascii=False))

# 리스트나 튜플처럼 다른 자료형도 JSON 문자열로 바꿀 수 있다.
print(json.dumps([1, 2, 3]))
print(json.dumps((4, 5, 6)))



