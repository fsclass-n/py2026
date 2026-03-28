# 다중 선형 회귀
# 원-핫 인코딩
import pandas as pd
dataset = pd.read_csv('MultipleLinearRegressionData.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(drop='first'), [2])], remainder='passthrough')
X = ct.fit_transform(X)

# 데이터 세트 분리
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 학습(다중 선형  회귀)
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train, y_train)

# 예측 값과 실제 값 비교(테스트 세트)
y_pred = reg.predict(X_test)

# 1. MAE(Mean Absolute Error): 실제 값과 예측 값 차이의 절대값
# 2. MSE(Mean Squared Error): 실제 값과 예측 값 차이의 제곱
# 3. RMSE(Root Mean Squared Error): 실제 값고 예측 값 차이의 제곱에 루트
# 4. R2: 결정 계수
# R2는 1에 가까울수록, 나머지는 0에 가까울수록 좋다.

# MAE(실제값, 예측값)
from sklearn.metrics import mean_absolute_error
print(mean_absolute_error(y_test, y_pred)) # 3.225328518828796
# MSE
from sklearn.metrics import mean_squared_error
print(mean_squared_error(y_test, y_pred)) # 19.900226981514965
# RMSE
from sklearn.metrics import root_mean_squared_error
print(root_mean_squared_error(y_test, y_pred)) # 4.460967045553572
# R2
from sklearn.metrics import r2_score
print(r2_score(y_test, y_pred)) # 0.9859956178877446

