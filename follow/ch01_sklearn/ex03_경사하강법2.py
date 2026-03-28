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

# 경사 하강법(Gradient Descent)
# SGD: Stochastic Gradient Descent(확률적 경사 하강법)
from sklearn.linear_model import SGDRegressor
# max_iter: 훈련 세트 반복 횟수(Epoch 횟수)
# eta0: 학습률(learning rate)
# 지수 표기법
# 0.001 -> 1e-3
# 0.0001 -> 1e-4
# 1000 -> 1e+3
# 10000 -> 1e+4
#sr = SGDRegressor(max_iter=1000, eta0=0.001, random_state=0, verbose=1)
sr = SGDRegressor(max_iter=200, eta0=1e-4, random_state=0, verbose=1)
sr.fit(X_train, y_train)
'''
-- Epoch 1
Norm: 2.35, NNZs: 1, Bias: 0.444851, T: 16, Avg. loss: 1198.292022, Objective: 1198.292100
Total training time: 0.00 seconds.
-- Epoch 2
Norm: 3.76, NNZs: 1, Bias: 0.704722, T: 32, Avg. loss: 788.857742, Objective: 788.858202
Total training time: 0.00 seconds.
-- Epoch 3
Norm: 4.81, NNZs: 1, Bias: 0.894567, T: 48, Avg. loss: 561.339336, Objective: 561.340294
Total training time: 0.00 seconds.
-- Epoch 4
Norm: 5.61, NNZs: 1, Bias: 1.042767, T: 64, Avg. loss: 416.295947, Objective: 416.297293
Total training time: 0.00 seconds.
-- Epoch 5
Norm: 6.26, NNZs: 1, Bias: 1.162648, T: 80, Avg. loss: 319.035774, Objective: 319.037520
Total training time: 0.00 seconds.
-- Epoch 6
Norm: 6.80, NNZs: 1, Bias: 1.262173, T: 96, Avg. loss: 250.737568, Objective: 250.739704
Total training time: 0.00 seconds.
-- Epoch 7
Norm: 7.25, NNZs: 1, Bias: 1.345727, T: 112, Avg. loss: 201.084636, Objective: 201.087108
Total training time: 0.00 seconds.
-- Epoch 8
Norm: 7.63, NNZs: 1, Bias: 1.416259, T: 128, Avg. loss: 164.594667, Objective: 164.597448
Total training time: 0.00 seconds.
-- Epoch 9
...
-- Epoch 88
Norm: 10.38, NNZs: 1, Bias: 2.021400, T: 1408, Avg. loss: 43.527633, Objective: 43.533023
Total training time: 0.01 seconds.
Convergence after 88 epochs took 0.01 seconds
'''

# 데이터 시각화(훈련 세트)
plt.scatter(X_train, y_train, color='blue') # 산정도
plt.plot(X_train,  sr.predict(X_train), color='green') # 선 그래프
plt.title('Score by hours (train data SGD)') # 제목
plt.xlabel('hours') # x축 이름
plt.ylabel('score') # Y축 이름
plt.show()

# print('기울기(m): ', reg.coef_) # [9.95294514]
# print('y 절편(b): ', reg.intercept_) # 4.404246457593025
print('기울기(m): ', sr.coef_) # [10.40150099]
print('y 절편(b): ', sr.intercept_) # 2.43608493

# 모델 평가
# 테스트 세트를 통한 모델 평가
# reg.score(X_test, y_test) # 0.9629782781439863
sr.score(X_test, y_test) # 0.9613927681584246
# 훈련 세트를 통한 모델 평가
# reg.score(X_train, y_train) # 0.8358318774163065
sr.score(X_train, y_train) # 0.8341158424419166