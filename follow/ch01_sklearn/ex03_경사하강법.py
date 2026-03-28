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
sr = SGDRegressor()
sr.fit(X_train, y_train)

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