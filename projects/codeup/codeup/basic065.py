# 정수 3개 입력받아 짝수만 출력하기
def main():
    a, b, c = map(int, input().split())
    if not (a % 2):
        print(a)
    if not (b % 2):
        print(b)
    if not (c % 2):
        print(c)

if __name__ == "__main__":
    main()