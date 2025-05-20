# 점수 입력받아 평가 출력하기
'''
90 ~ 100 : A
70 ~  89 : B
40 ~  69 : C
 0 ~  39 : D
'''
def main():
    a = int(input())
    if   a >= 90:
        print('A')
    elif a >= 70:
        print('B')
    elif a >= 40:
        print('C')
    else:
        print('D')

if __name__ == "__main__":
    main()