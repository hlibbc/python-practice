# 정수 2개 입력받아 큰 값 출력 (3항 연산자 사용)
def main():
    a, b = input().split()
    print(a if int(a) > int(b) else b)

if __name__ == "__main__":
    main()