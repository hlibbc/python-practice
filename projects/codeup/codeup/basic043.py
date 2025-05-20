# 실수 2개 입력받아 나눈 결과 계산 (소수점 3째자리까지 출력)
def main():
    a, b = input().split()
    result = float(a) / float(b)
    print(f"{result:.3f}") # 파이썬에서는 기본적으로 반올림이다. (버림이나 올림하려면 인위적으로 코드작업 해야 함)

if __name__ == "__main__":
    main()