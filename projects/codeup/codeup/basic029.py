# 10진 정수 입력받아 16진수로 출력하기
def main():
    n = int(input(), 16) # 입력받은 문자열을 16진수로 변수 n에 저장 -> ex. 255가 입력되었다면 16진수 255로 저장된다.
    # n = int(input())   # 입력받은 문자열을 10진수로 변수 n에 저장 -> ex. 255가 입력되었다면 10진수 255로 저장된다.
    print(f"{n:o}")

if __name__ == "__main__":
    main()