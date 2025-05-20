# 정수 1개 입력받아 그 수까지 출력하기 (for문 사용)
def main():
    n = int(input())
    for i in range(0, n+1, 1):
        print(i)

if __name__ == "__main__":
    main()