# 정수 1개 입력받아 분류하기 (양수,음수,홀,짝)
'''
A: 음수이면서 짝수
B: 음수이면서 홀수
C: 양수이면서 짝수
D: 양수이면서 홀수
'''
def main():
    a = int(input())
    print((('C') if not (a % 2) else ('D')) if a > 0 else (('A') if not (a % 2) else ('B')))

if __name__ == "__main__":
    main()