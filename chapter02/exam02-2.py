#매개변수를 총해서 하나의 문자열을 전달받아 그 문자열을 총 3회 출력하는 함수를 만들어보자
def exam(str):
    print(str)
    print(str)
    print(str)

#매개변수를 통해서 하나의 정수를 전달 받아서 전달받은 수와 부호가 반대인 정수를 출력하는 함수를 만들어보자
def exam02(num):
    print(num * -1)

#매개변수를 통해서 두 개의 정수를 전달받아서 이 둘의 평균값을 계산해서 출력하는 함수를 만들어보자
def Avg(num1, num2):
    print((num1 + num2) / 2)

def main():
    exam("Hello")
    exam02(3)
    Avg(3, 5)

main()
