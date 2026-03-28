# 선형 회귀(Linear Regression)
# 공부 시간에 따른 시험 점수?
import matplotlib.pyplot as plt
import pandas as pd

# .csv 파일(데이터) 가져오기
dataset = pd.read_csv('LinearRegressionData.csv')
print(dataset.head())
'''
   hour  score
0   0.5     10
1   1.2      8
2   1.8     14
3   2.4     26
4   2.6     22
'''

# 독립 변수와 종속 변수 분리
# 처음부터 마지막 컬럼 직전까지의 데이터(독립 변수, 원인)
X = dataset.iloc[:, :-1].values
# 마지막 컬럼 데이터(종속 변수, 결과)
y = dataset.iloc[:, -1].values
print(X, y)
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
 [10. ]] [ 10   8  14  26  22  30  42  48  38  58  60  72  62  68  72  58  76  86
  90 100]
'''

from sklearn.linear_model import LinearRegression
reg = LinearRegression() # 객체 생성
reg.fit(X, y) # 학습(모델 생성)

y_pred = reg.predict(X) # X에 대한 예측(predict) 값
print(y_pred)
'''
[  7.67033317  14.72278017  20.76773474  26.8126893   28.82767416
  34.87262873  41.92507572  46.96253786  47.97003029  53.00749243
  56.02996971  40.91758329  63.08241671  64.08990913  65.09740156
  72.14984856  75.17232584  87.26223498  89.27721983 103.38211382]
'''

plt.scatter(X, y, color='blue') # 산정도
plt.plot(X,  y_pred, color='green') # 선 그래프
plt.title('Score by hours') # 제목
plt.xlabel('hours') # x축 이름
plt.ylabel('score') # Y축 이름
plt.show()

print('9시간 공부했을 때 예상 점수: ', reg.predict([[9]])) # [93.30718954]

print('기울기(m): ', reg.coef_) # [10.07492428]
print('y 절편(b): ', reg.intercept_) # 2.6328710345926893

# y = mX + b -> y = 10.0749X + 2.6328