# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값 계산하기
'''
첫 번째 줄에 합
두 번째 줄에 차,
세 번째 줄에 곱,
네 번째 줄에 몫,
다섯 번째 줄에 나머지,
여섯 번째 줄에 나눈 값을 순서대로 출력한다.
(실수, 소수점 이하 둘째 자리까지의 정확도로 출력)
'''
def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    divided = a / b
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
    print(f"{divided:.2f}")

if __name__ == "__main__":
    main()