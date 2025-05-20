# 단어 1개 입력받아 나누어 출력하기
def main():
    input_str = input()
    # for char in input_str:
    #     print(char)
    # 위 주석과 같이 해도 되고, 아래와 같이 배열처리 형식으로 해도 된다.
    '''
    range: 연속된 정수의 시퀀스(범위)를 생성하는 내장함수
    range(start, stop, step)
    - start (생략 가능): 범위의 시작값 (기본값은 0)
    - stop (필수): 범위의 끝값 (이 값은 포함되지 않음)
    - step (생략 가능): 증가 또는 감소 간격 (기본값은 1)
    '''
    for i in range(len(input_str)):
        print(input_str[i])

if __name__ == "__main__":
    main()
