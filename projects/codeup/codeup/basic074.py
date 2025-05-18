# 문자 1개 입력받아 알파벳 출력하기
'''
영문 소문자(a ~ z) 1개가 입력되었을 때,
a부터 그 문자까지의 알파벳을 순서대로 출력해보자.
'''
# def main():
#     char_idx = ord(input())
#     index = ord('a')
#     result = ''
#     while index <= char_idx:
#         result += chr(index)
#         result += ' '
#         index += 1
#     print(result)
## 아래 코드가 더 깔끔하다. print 함수의 end 옵션 주목
def main():
    char_idx = ord(input())
    index = ord('a')
    while index <= char_idx:
        print(chr(index), end=' ') # end문자를 명시한다. end=을 생략하면 디폴트로 '\n'이 들어간다. 여기선 개행대신 공백(' ')을 end문자로 명시함
        index += 1
    print('')

if __name__ == "__main__":
    main()