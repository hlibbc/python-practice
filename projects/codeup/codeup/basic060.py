# 비트단위로 AND 하여 출력
def main():
    a, b = input().split()
    print(int(a) & int(b)) # bitwise and

if __name__ == "__main__":
    main()