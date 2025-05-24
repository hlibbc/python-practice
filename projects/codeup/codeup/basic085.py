# 그림 파일 저장용량 계산하기
'''
입력:
w, h, b 가 공백을 두고 입력된다.
단, w, h는 모두 정수이고 1~1024 이다. b는 40이하의 4의 배수이다.

w: 가로해상도
h: 세로해상도
b: 하나의 픽셀을 저장하기 위한 비트
ex. 1024 width, 768 height, 24 bit
-> 1024 * 768 * 24 / 8 / 1024 / 1024


출력:
필요한 저장 공간을 MB 단위로 바꾸어 출력한다.
단, 소수점 셋째 자리에서 반올림하여 둘째 자리까지 출력한다.
'''
def main():
    try:
        w, h, b = map(int, input().split())
        if not ((0 < w <= 1024) and (0 < h <= 1024) and ((0 < b <= 40) and (b % 4 == 0))):
            raise ValueError(f"Invalid input")
        size = w * h * b / 8 / 1024 / 1024 # / 하면 자동으로 float으로 타입 변경됨
        print(f"{size:.2f} MB")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()