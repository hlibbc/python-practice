# 주민등록번호 123456-1234567 를 입력받아 1234561234567 로 표현
def main():
    first_sn, second_sn = input().split('-')
    print(first_sn + second_sn)

if __name__ == "__main__":
    main()