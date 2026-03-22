# while 문
# 조건문이 참인 동안 while 문에 속한 문장들을 반복해서 수행한다.
# 기본 구조:
# while 조건문:
#     수행할_문장1
#     수행할_문장2
#     수행할_문장3

treeHit = 0
while treeHit < 10:
    # treeHit = treeHit + 1
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0
while number != 4:
    print(prompt)
    # number = int(input())는 사용자의 숫자 입력을 받아들이는 것
    # int나 input은 내장 함수이다.
    number = int(input())

# while 문 강제로 빠져나가기
# break 문
# 커피 자판기
coffee = 10
money = 300
# money는 0이 아니기 때문에 항상 참이다.
# 따라서 무한히 반복되는 무한 루프를 돌게 된다.
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# 실제 자판기
coffee = 1
while True:
    # 사용자로부터 값을 입력받아 money 변수에 대입하는 것
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee -= 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee -= 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break

# while 문을 빠져나가지 않고
# while 문의 맨 처음(조건문)으로 다시 돌아가게 만들고 싶은 경우
# continue
# 상황: 1부터 10까지의 숫자 중에서 홀수만 출력
a = 0
while a < 10:
    a += 1
    if a % 2 == 0: continue
    print(a)

# 무한 루프
# 무한 루프(endless loop)는 무한히 반복한다는 의미이다.
# 서버, 이벤트 처리, 입력 대기 같은 상황에서 무한 루프는 자주 사용된다.
# while True:
#     print("ctrl+c를 눌러야 while문을 빠져나갈 수 있습니다.")

# while-else 문
# while 문이 정상적으로 종료되었을 때(break로 빠져나가지 않았을 때)
# else 절이 실행된다.
count = 0
while count < 3:
    print(f"카운트: {count}")
    count += 1
else:
    print("while 문이 정상 종료되었습니다.")

# break 문으로 while 문을 빠져나가면 else 절은 실행되지 않는다.
count = 0
while count < 5:
    if count == 2:
        break
    print(f"카운트: {count}")
    count += 1
else:
    print("while 문이 정상 종료되었습니다.")

# 중첩된 while 문
# 중첩된 while 문에서 break나 continue를 사용할 때는
# 가장 가까운 while 문에만 영향을 준다
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1