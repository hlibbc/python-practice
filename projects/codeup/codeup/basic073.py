# 정수 1개 입력받아 카운트다운 출력하기
def main():
    n = int(input())
    while n != 0:
        n -= 1
        print(n)

if __name__ == "__main__":
    main()