# json
# 인터넷으로 얻은 myinfo.json 파일을 읽어
# 파이썬에서 처리할 수 있도록 딕셔너리 자료형으로 만들려면?
import json

with open('myinfo.json') as f:
    data = json.load(f)

type(data)
print(data)
