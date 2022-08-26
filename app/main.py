import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.calculator import CalculatorService
from app.services.user import UserService
from app.services.score import ScoreService


def print_menu():
    print('0. 전체프로그램 종료')
    print('1. 계산기 프로그램')
    print('2. 로그인 프로그램') # 입력받은 아이디와 비번 콘솔에 출력하기
    menu = input('메뉴 선택')
    return menu
    
def main():
    while 1:
        menu = print_menu()
        if menu == '0':
            print('전체프로그램 종료')
            break
        elif menu == '1':
            calculatorService = CalculatorService()             
            first = int(input('첫번째 수 입력')) 
            second = int(input('두번째 수 입력'))
            calculatorService.calculate(first, second)
        elif menu == '2':
            userService = UserService()
            id = input('아이디 입력')
            password = input('비밀번호 입력')
            userService.login(id, password)
        elif menu == '3':
            scoreService = ScoreService()
            name = input('이름 입력')
            scoreService.Score2(name)
            if ave >= 90:
                
               grade = "A"
            elif 80 <= ave < 90:
               grade = "B"
            elif 70 <= ave < 80:
               grade = "C"
            else:
               grade = "D"
            print(f"당신의 평균 점수는 {Average}점으로 {grade}학점 입니다.")

if __name__ == '__main__':
    main()
    