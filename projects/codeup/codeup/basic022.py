# 6자리의 연월일 (YYMMDD) 입력받아 나누어 출력하기
def main():
    date = input()
    result = ''
    for i in range(0, len(date), 2):
        result += date[i:i+2] + ' '
    print(result)

if __name__ == "__main__":
    main()
