# 369게임
'''
만약 3, 6, 9 가 들어간 수를 자신이 불러야 하는 상황이라면, 수를 부르는 대신 "박수(X)" 를 쳐야 한다.
33과 같이 3,6,9가 두 번 들어간 수 일때, "짝짝"과 같이 박수를 두 번 치는 형태도 있다. 
입력
----
30 보다 작은 정수 1개가 입력된다. (1 ~ 29)

출력
----
1 부터 그 수까지 순서대로 공백을 두고 수를 출력하는데,
3 또는 6 또는 9가 포함 되어있는 수인 경우, 그 수 대신 영문 대문자 X 를 출력한다.
'''
# def main():
#     input_str = input()
#     n = int(input_str)
#     if not (1 <= n < 30):
#         raise ValueError(f"Invalid input: [{n}] Only (1 ~ 29) can be entered!")
#     for i in range(1, n + 1):
#         check_str = str(i)
#         check_flag = False
#         for j in range(len(check_str)):
#             if int(check_str[j]) != 0 and int(check_str[j]) % 3 == 0:
#                 print('X', end='')
#                 check_flag = True
#         if check_flag == False:
#             print(check_str, end='')
#         print(' ', end='')
#     print('')

## 좀 더 우아한 표현방법
'''
각 숫자별로 '369' 포함개수를 카운팅하여, 0이 아닐경우, 그 개수만큼 X를 출력하고, 0일 경우, 숫자 자체를 출력
루프과정에서의 print()는 end를 공백(' ')으로 설정하여 한줄에 출력되도록 한 후, 루프종료시 개행

clap_cnt 생성은 제너레이터 표현식으로 한줄로 깔끔하게 표현
    1 for c in str(i) if c in '369'
    - 문자열 str(i)의 각 문자 c에 대해, '3', '6', '9' 중 하나일 경우 1을 생성하라.
    clap_cnt = sum(1 for c in str(i) if c in '369')
    - 위 제너레이터 표현식에 의해 1이 생성될 때마다 더해서, 최종 합산값을 clap_cnt에 넣어라.
    - 즉, clap_cnt는 str(i)가 '3','6','9'를 몇개나 가지고 있는지 카운팅한 값이 됨

    위 코드는 아래와 같이 풀어 쓸 수 있음
    count = 0
    for c in str(i):
        if c in '369':
            count += 1
    clap_cnt = count
'''
# def main():
#     n = int(input())
#     if not (1 <= n < 30):
#         raise ValueError(f"Invalid input: [{n}] Only (1 ~ 29) can be entered!")
#     for i in range(1, n +1):
#         clap_cnt = sum(1 for c in str(i) if c in '369')
#         print('X' * clap_cnt if clap_cnt else i, end=' ')
#     print('')

## 좀 더 우아한 표현방법
'''
최종 출력 문자열을 담을 리스트를 생성하고, 여기에 계속 append 시킨 후
출력은 최종 한번만 수행함
result는 리스트 타입이며, for 루프 안에서 append 함수를 통해 문자열들이 element로 추가됨
최종적으로 ' '.join(result) 을 통해 하나의 문자열로 병합된 후 출력됨
    ' '.join(result)의 의미
    - 각 element들을 ' ' 로 구분하여 하나의 문자열로 병합시킴.
'''
# def main():
#     n = int(input())
#     if not (1 <= n < 30):
#         raise ValueError(f"Invalid input: [{n}] Only (1 ~ 29) can be entered!")
#     result = []  # 최종 출력 문자열을 담을 리스트
#     for i in range(1, n + 1):
#         count = sum(1 for c in str(i) if c in '369')  # 3, 6, 9의 개수 세기
#         if count > 0:
#             result.append('X' * count)
#         else:
#             result.append(str(i))
#     print(' '.join(result))


## 좀 더 축약해서 아래와 같이도 표현 가능
'''
print(' '.join('X' * sum(1 for c in str(i) if c in '369') or str(i) for i in range(1, n + 1)))
.... for i in range(1, n + 1) -> 1 부터 n 까지 루핑돌면서
.... 'X' * sum(1 for c in str(i) if c in '369') or str(i) -> 'X' * sum(1 for c in str(i) if c in '369') 이놈 혹은 str(i) 이놈이 선택되는데
........ 'X' * sum(1 for c in str(i) if c in '369')가 '참같은 값'이면 이 값이 선택되고
........ '거짓같은 값 ('' 혹은 null) 이면 str(i)가 선택된다.
............ 1 for c in str(i) if c in '369' -> 문자열 str(i)의 각 문자 c에 대해, '3', '6', '9' 중 하나일 경우 1을 생성
............ sum(1 for c in str(i) if c in '369') -> 1이 생성될 때마다 sum 더해짐
............ 'X' * sum(1 for c in str(i) if c in '369') 최종 sum 값만큼 X가 append 됨
................ print(' '.join(...) -> 최종적으로 생성된 제너레이터 (XX.., str(i) 중 하나를 element들로 가지는 리스트) 들을 ' '으로 구분하여 하나의 문자열로 병합
'''
def main():
    n = int(input())
    if not (1 <= n < 30):
        raise ValueError(f"Invalid input: [{n}] Only (1 ~ 29) can be entered!")
    # print(' '.join('X' * sum(c in '369' for c in str(i)) or str(i) for i in range(1, n + 1))) # 이렇게해도 되긴된다. 이는 True와 1이 1로 똑같이 처리되기 때문
    print(' '.join('X' * sum(1 for c in str(i) if c in '369') or str(i) for i in range(1, n + 1))) # but 문맥상으론 이게 더 맞는 표현
    
if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(e)