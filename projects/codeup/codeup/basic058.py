# 둘 다 거짓일 경우만 참 출력 (nor: not 과 or의 조합)
def main():
    a, b = input().split()
    print(not (bool(int(a)) or bool(int(b)))) # nor

if __name__ == "__main__":
    main()