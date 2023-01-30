#하나의 정수를 전달받아서 전달받은 수와 부호가 반대인 정수를 반환하는 함수를 정의해보자
def fun(num):
    return num * -1

#두 새의 정수를 전달받아서 그 두수의 평균값을 계산해서 반환하는 함수를 정의해보자
def fun2(num1, num2):
    return (num1 + num2) / 2

def main():
    print(fun(3))
    print(fun2(3, 5))

main()