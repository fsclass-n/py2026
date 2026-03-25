# pickle
# 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
import pickle

# 문제
# pickle 모듈의 dump 함수를 사용하여
# 딕셔너리 객체인 data를 그대로 파일에 저장하는 방법
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'java', 3: 'ruby', 4: 'c#'}
pickle.dump(data, f)
f.close()

# pickle.dump로 저장한 파일을 pickle.load를 사용해서
# 원래 있던 딕셔너리 객체(data) 상태 그대로 불러오는 예
f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)
# {1: 'python', 2: 'java', 3: 'ruby', 4: 'c#'}