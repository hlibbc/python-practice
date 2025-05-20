# 둘 다 참일 경우만 참 출력 (and)
def main():
    a, b = input().split()
    print(bool(int(a)) and bool(int(b))) # and: && 효과

if __name__ == "__main__":
    main()