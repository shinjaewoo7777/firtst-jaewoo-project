import numpy as np
import matplotlib.pyplot as plt

# 함수 정의
def f(x):
    return x * np.sqrt(4 - x)

# x 값의 범위 설정
x_values = np.linspace(0, 4, 400)

# 함수값 계산
y_values = f(x_values)

# 그래프 그리기
plt.plot(x_values, y_values, label='f(x) = x(4-x)^{1/2}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x) = x(4-x)^{1/2}')
plt.grid(True)
plt.legend()
plt.show()