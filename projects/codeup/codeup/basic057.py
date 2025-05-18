# 참/거짓이 서로 같을 때에만 참 출력하기 (xnor: ^와 not의 조합)
def main():
    a, b = input().split()
    print(not (bool(int(a)) ^ bool(int(b)))) # xnor

if __name__ == "__main__":
    main()