def factorial(n):
    if n == 0:          #입력값이 0이라면 1반환
        return 1
    else:
        return n * factorial(n-1)

# 사용자가 입력하는 수의 factorial 계산
def calculate_factorial():
    try:
        num = int(input("팩토리얼을 계산할 정수를 입력하세요: ")) #정수입력
        if num < 0:
            print("음수의 팩토리얼은 계산할 수 없습니다..") # 팩토리얼은 입력값이 0보다 작다면 불가능
            return
        result = factorial(num)                     # 팩토리얼 함수 호출
        print(f"{num}의 팩토리얼은 {result}입니다.") # 팩토리얼 출력
    except ValueError:              #값 문제가 있다면 재귀호출
        print("정수를 입력해주세요.")

calculate_factorial()       #재귀호출
