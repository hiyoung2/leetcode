# --url--
# https://www.acmicpc.net/problem/10797

# --title--
# 10797번: 10부제

# --problem_description--
# 서울시는 6월 1일부터 교통 혼잡을 막기 위해서 자동차 10부제를 시행한다. 자동차 10부제는 자동차 번호의 일의 자리 숫자와 날짜의 일의 자리 숫자가 일치하면 해당 자동차의 운행을 금지하는 것이다. 예를 들어, 자동차 번호의 일의 자리 숫자가 7이면 7일, 17일, 27일에 운행하지 못한다. 또한, 자동차 번호의 일의 자리 숫자가 0이면 10일, 20일, 30일에 운행하지 못한다.

# 여러분들은 일일 경찰관이 되어 10부제를 위반하는 자동차의 대수를 세는 봉사활동을 하려고 한다. 날짜의 일의 자리 숫자가 주어지고 5대의 자동차 번호의 일의 자리 숫자가 주어졌을 때 위반하는 자동차의 대수를 출력하면 된다. 

# --problem_input--
# 첫 줄에는 날짜의 일의 자리 숫자가 주어지고 두 번째 줄에는 5대의 자동차 번호의 일의 자리 숫자가 주어진다. 날짜와 자동차의 일의 자리 숫자는 모두 0에서 9까지의 정수 중 하나이다. 

# --problem_output--
# 주어진 날짜와 자동차의 일의 자리 숫자를 보고 10부제를 위반하는 차량의 대수를 출력한다.

# 1. 날짜의 일의 자리 숫자 입력 받기, 5대의 자동차 번호의 일의 자리 숫자 입력 받기 (input(), sys.stdin.readlin() 사용 가능)
# 2. 입력받은 자동차 일의 자리 숫자들 중 날짜의 일의 자리 숫자와 동일한 숫자가 몇 개인지 출력해내면 된다

# 리스트에서 같은 이름(?)을 가진 게 몇 개 있는지 추출해내는 기능을 봤던 것 같아서 정리해 둔 거 찾아보고 count()함수 적용
# count("강아지") 라고 하면 어떤 리스트에 "강아지" 요소가 몇 개인지 추출해내줌
# 자동차 번호를 입력 받을 때 list형태로 받기(input() or sys.stdin.readline() 앞에 list로 감싸주면 list 형태로 받아진다!)

import sys

day = input()
car = list(sys.stdin.readline().split())

print(car.count(day))
