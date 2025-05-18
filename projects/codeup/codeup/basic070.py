# 월 입력받아 계절 출력하기
'''
월 : 계절 이름
 12, 1, 2   : winter
  3, 4, 5   : spring
  6, 7, 8   : summer
  9, 10, 11 : fall
'''
def main():
    season = ["winter", "spring", "summer", "fall"]
    a = int(input())
    print(season[(a // 3) % 4])

if __name__ == "__main__":
    main()