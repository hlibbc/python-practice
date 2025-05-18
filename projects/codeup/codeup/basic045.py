# 정수 3개 입력받아 합과 평균 출력 (소수점 2째자리까지 출력)
def main():
    a, b, c = input().split()
    sum = int(a) + int(b) + int(c)
    avg = sum / 3
    print(sum, f"{avg:.2f}")

if __name__ == "__main__":
    main()