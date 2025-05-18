# 정수 3개 입력받아 가장 작은 값 출력 (3항 연산자 사용)
def main():
    a, b, c = map(int, input().split())
    print((c if b > c else b) if a > b else (c if a > c else a))

if __name__ == "__main__":
    main()