import matplotlib.pyplot as plt

# 2차 1차 상수의 계수를 입력받음
a = float(input("2차항의 계수를 입력하세요: "))
b = float(input("1차항의 계수를 입력하세요: "))
c = float(input("상수항의 계수를 입력하세요: "))

def fn():
    xlist = []      #범위를 -100부터 101까지 줌
    ylist = []

    for x in range(-100, 101):
        x = x / 10.0
        y = a * x ** 2 + b * x + c  #함수
        xlist.append(x)
        ylist.append(y)

    plt.plot(xlist, ylist)  #plt.plot을 사용해 그래프 그림
    plt.show()

fn()