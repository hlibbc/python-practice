# 짝수 합 구하기 
# 정수 1개 (1 ~ 100)를 입력받아 1부터 그 수까지 짝수의 합을 구한다.
def main():
    n = int(input())
    result = 0
    if not (n % 2):
        n += 1
    for i in range(0, n, 2):
        result += i
    print(result)

if __name__ == "__main__":
    main()