# 정수 1개 입력받아 카운트다운 출력하기
def main():
    n = int(input())
    while n != 0:
        print(n)
        n -= 1

if __name__ == "__main__":
    main()