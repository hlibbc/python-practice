# 언제까지 더해야 할까?
# 즉, 1부터 n까지 정수를 계속 더해 나간다고 할 때, 어디까지 더해야 입력한 수보다 같거나 커지는 지를 알아보자

## 그냥 일반적인 방법
# def main():
#     n = int(input())
#     sum = 0
#     for i in range(0, n, 1):
#         sum += i
#         if sum >= n:
#             break
#     print(i)

# sum() 함수를 통한 while 루프 제어
# def main():
#     n = int(input())
#     i = 0
#     while sum(range(0, i+1)) < n:
#         i += 1
#     print(i)

# takewhile과 accumulate를 사용한 더 효율적인 방법
from itertools import takewhile, accumulate

def main():
    n = int(input())
    i = len(list(takewhile(lambda x: x < n, accumulate(range(0, n + 1)))))
    print(i)


if __name__ == "__main__":
    main()