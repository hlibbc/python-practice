# 정수 1개 입력받아 그 수까지 출력하기
def main():
    n = int(input())
    index = 0
    while index <= n:
        print(index)
        index += 1

if __name__ == "__main__":
    main()