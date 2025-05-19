# 원하는 문자(q) 가 입력될 때까지 입력된 문자를 계속 출력하기
# walrus 연산자, 파이썬의 변수 스코프
'''
파이썬의 변수 스코프는 function 내부에서는 다 접근 가능 (조건문 안에서 선언되었더라도 외부에서 접근 가능)
--------------
정상적인 케이스
def func():
    ....
    if x > 10:
        n = 'test'
    else:
        n = 'real'
    print(n) # n은 if / else 문 안에서 선언되었으나, 외부에서 참조 가능

--------------
아래의 경우는 오류
def func():
    ....
    if x > 10:
        n = 'test'
    print(n) # 오류 원인은 scope 문제가 아니라 if에 걸리지 않는 경우 n 변수 초기화 자체가 안되기 때문에 에러나는 것임
'''
def main():
    while True:
        char = input()
        print(char)
        if  char == 'q': # Walrus 연산자: 선언과 동시에 값 대입도 됨. (파이썬에서는 조건문에서 = 연산자를 허용하지 않는다. walrus는 이 대용으로 생각하면 됨)
            break
        
if __name__ == "__main__":
    main()