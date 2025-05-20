# 평가 입력받아 다르게 출력하기 (dictionary 사용)
'''
dictionary: 키-값 (Key-Value) 쌍으로 데이터를 저장하는 변경 가능한 (mutable) 자료형
평가 : 내용
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what?

기본 dictionary 타입으로 what?을 처리할 수 없어, defaultdict를 import 한다.
'''
from collections import defaultdict

def main():
    grades = defaultdict(lambda: "what?")
    grades.update({
        "A": "best!!!",
        "B": "good!!",
        "C": "run!",
        "D": "slowly~"
    })
    print(grades[input()])

if __name__ == "__main__":
    main()