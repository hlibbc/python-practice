# 하나라도 참이면 참 출력 (or)
def main():
    a, b = input().split()
    print(bool(int(a)) or bool(int(b))) # or: || 효과

if __name__ == "__main__":
    main()