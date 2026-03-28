# 다중 선형 회귀
# 원-핫 인코딩
import pandas as pd
dataset = pd.read_csv('MultipleLinearRegressionData.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
X

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(drop='first'), [2])], remainder='passthrough')
X = ct.fit_transform(X)
X

# 데이터 세트 분리
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 학습(다중 선형  회귀)
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train, y_train)

# 예측 값과 실제 값 비교(테스트 세트)
y_pred = reg.predict(X_test)
y_pred # array([ 92.15457859,  10.23753043, 108.36245302,  38.14675204])
# 실제 값
y_test # array([ 90,   8, 100,  38])

# 기울기
reg.coef_
# array([-5.82712824, -1.04450647, 10.40419528, -1.64200104])
# 절편
reg.intercept_
# np.float64(5.3650067065447615)

# 모델 평가
# 훈련 세트
reg.score(X_train, y_train) # 0.9623352565265527
# 테스트 세트
reg.score(X_test, y_test) # 0.9859956178877446