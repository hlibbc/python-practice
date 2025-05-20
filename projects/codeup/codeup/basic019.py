# 연도.월.일 을 입력받아 일-월-연도 로 출력하기
def main():
    year, month, day = input().split('.')
    print(day, month, year, sep='-')

if __name__ == "__main__":
    main()