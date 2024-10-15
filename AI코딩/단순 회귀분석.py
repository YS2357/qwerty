import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 샘플 데이터 생성 (독립 변수 X, 종속 변수 y)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1.5, 1.8, 3.2, 4.5, 5.0])

# 단순 회귀 모델 생성 및 학습
model = LinearRegression()
model.fit(X, y)

# 예측 값
y_pred = model.predict(X)

# 회귀 계수 (기울기와 절편)
print(f'기울기 (Slope): {model.coef_[0]}')
print(f'절편 (Intercept): {model.intercept_}')

# 모델 평가 지표
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(f'Mean Squared Error (MSE): {mse}')
print(f'R² Score: {r2}')

# 시각화 (데이터와 회귀선)
plt.scatter(X, y, color='blue')  # 실제 데이터
plt.plot(X, y_pred, color='red')  # 회귀선
plt.xlabel('X')
plt.ylabel('y')
plt.title('Simple Linear Regression')
plt.show()

from sklearn.metrics import mean_absolute_error

# MSE와 R² Score는 앞에서 구했습니다.
mae = mean_absolute_error(y, y_pred)

print(f'Mean Absolute Error (MAE): {mae}')

# 샘플 데이터 생성 (다중 변수)
X_multi = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]])
y_multi = np.array([1.5, 1.8, 3.2, 4.5, 5.0])

# 다중 회귀 모델 생성 및 학습
model_multi = LinearRegression()
model_multi.fit(X_multi, y_multi)

# 예측 값
y_pred_multi = model_multi.predict(X_multi)

# 회귀 계수
print(f'회귀 계수 (Coefficients): {model_multi.coef_}')
print(f'절편 (Intercept): {model_multi.intercept_}')

from sklearn.model_selection import cross_val_score

# 교차 검증을 통한 모델 평가 (5-fold)
scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')

print(f'교차 검증 MSE 점수: {-scores.mean()}')

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
