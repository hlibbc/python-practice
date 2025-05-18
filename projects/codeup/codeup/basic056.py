# 참/거짓이 서로 다를 때에만 참 출력하기 (xor)
def main():
    a, b = input().split()
    print(bool(int(a)) ^ bool(int(b))) # xor

if __name__ == "__main__":
    main()