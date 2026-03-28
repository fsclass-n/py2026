# 1. 데이터 세트 분리
import matplotlib.pyplot as plt
import pandas as pd

# .csv 파일(데이터) 가져오기
dataset = pd.read_csv('LinearRegressionData.csv')

# 독립 변수와 종속 변수 분리
# 처음부터 마지막 컬럼 직전까지의 데이터(독립 변수, 원인)
X = dataset.iloc[:, :-1].values
# 마지막 컬럼 데이터(종속 변수, 결과)
y = dataset.iloc[:, -1].values


from sklearn.model_selection import train_test_split
# 훈련 세트 : 테스트 세트를 80:20 으로 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 데이터 세트: 전체 데이터 X, 개수
print(X, len(X))
'''
[[ 0.5]
 [ 1.2]
 [ 1.8]
 [ 2.4]
 [ 2.6]
 [ 3.2]
 [ 3.9]
 [ 4.4]
 [ 4.5]
 [ 5. ]
 [ 5.3]
 [ 3.8]
 [ 6. ]
 [ 6.1]
 [ 6.2]
 [ 6.9]
 [ 7.2]
 [ 8.4]
 [ 8.6]
 [10. ]] 20
'''
# 훈련 세트 X, 개수
print(X_train, len(X_train))
'''
[[5.3]
 [8.4]
 [3.9]
 [6.1]
 [2.6]
 [1.8]
 [3.2]
 [6.2]
 [5. ]
 [4.4]
 [7.2]
 [3.8]
 [2.4]
 [0.5]
 [6.9]
 [6. ]] 16
'''
# 테스트 세트 X, 개수
print(X_test, len(X_test))
'''
[[ 8.6]
 [ 1.2]
 [10. ]
 [ 4.5]] 4
'''
# 전체 데이터 y, 개수
print(y, len(y))
'''
[ 10   8  14  26  22  30  42  48  38  58  60  72  62  68  72  58  76  86
  90 100] 20
'''
# 훈련 세트 y, 개수
print(y_train, len(y_train))
# [60 86 42 68 22 14 30 72 58 48 76 72 26 10 58 62] 16
# 테스트 세트 y, 개수
print(y_test, len(y_test))
# [ 90   8 100  38] 4


# 2. 분리된 데이터를 통한 모델링
from sklearn.linear_model import LinearRegression
reg = LinearRegression()

# 훈련 세트로 학습
reg.fit(X_train, y_train)

# 3. 데이터 시각화(훈련 세트)
plt.scatter(X_train, y_train, color='blue') # 산정도
plt.plot(X_train,  reg.predict(X_train), color='green') # 선 그래프
plt.title('Score by hours (train data)') # 제목
plt.xlabel('hours') # x축 이름
plt.ylabel('score') # Y축 이름
plt.show()

# 4. 데이터 시각화(테스트 세트)
plt.scatter(X_test, y_test, color='blue') # 산정도
plt.plot(X_train,  reg.predict(X_train), color='green') # 선 그래프
plt.title('Score by hours (test data)') # 제목
plt.xlabel('hours') # x축 이름
plt.ylabel('score') # Y축 이름
plt.show() 

print('기울기(m): ', reg.coef_) # [9.95294514]
print('y 절편(b): ', reg.intercept_) # 4.404246457593025


# 모델 평가
# 테스트 세트를 통한 모델 평가
reg.score(X_test, y_test) # 0.9629782781439863
# 훈련 세트를 통한 모델 평가
reg.score(X_train, y_train) # 0.8358318774163065