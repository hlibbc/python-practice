# 정수 입력받아 0이 아니면 True를, 0이면 False를 출력하기
def main():
    print(bool(int(input())))

# 입력받은 값이 정수형인지 아닌지 판별하려면? 아래와 같이 해야..
# def main():
#     try:
#         n = int(input())
#         print(True)
#     except ValueError:
#         print(False)

if __name__ == "__main__":
    main()