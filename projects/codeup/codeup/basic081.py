# 16진수 구구단 출력하기
'''
입력된 16진수에 1~F까지 순서대로 곱한, 16진수 구구단을 줄을 바꿔 출력한다.
계산 결과도 16진수로 출력해야 한다.

try-catch 문을 써서 정확한 입력 제어도 직접 해보자
'''
def main():
    inputs = input()
    hex_input = ord(inputs)
    if not ((hex_input >= ord('A')) and (hex_input <= ord('F'))):
        raise ValueError(f"Invalid input: [{inputs}] Only (A-F) can be entered!")
    hex_input = hex_input - ord('A') + 10
    for i in range(1, 16, 1):
        print('%X'%hex_input, '*%X'%i, '=%X'%(hex_input*i), sep='')

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(e) # poetry로 실행하면 traceback까지 같이 찍힘. python3로 해당파일만 실행하면 딱 이 에러만 출력됨