# 정수 2개 입력받아 나눈 몫 계산
def main():
    a, b = input().split()
    print(int(a) // int(b)) # 나눈 몫 계산
    # print(int(a) / int(b)) # 나누기 연산만 쓰면 나누어 떨어지지 않을 경우, 몫만 구하는게 아니라, 소수점 아래 수들까지 다 나오게 됨

if __name__ == "__main__":
    main()