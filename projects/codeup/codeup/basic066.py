# 정수 3개 입력받아 짝/홀 출력하기
def main():
    a, b, c = map(int, input().split())
    print("even" if not (a % 2) else "odd")
    print("even" if not (b % 2) else "odd")
    print("even" if not (c % 2) else "odd")

if __name__ == "__main__":
    main()