# 오류 회피하기
# 코드를 작성하다 보면 특정 오류가 발생해도 그냥 통과시켜야 할 때
# 여러 파일을 처리하는 중에 일부 파일이 없더라도 프로그램을 계속 실행하고 싶을 때
students = ["김철수", "이영자", "박민수", "최유진"]
for student in students:
    try:
        with open(f"{student}_성적.txt", 'r') as f:
            score = f.read()
            print(f"{student}의 성적: {score}")
    except FileNotFoundError:
        print(f"{student}의 성적 파일이 없습니다. 건너뜁니다.")
        continue # 다음 학생으로 넘어감

# 때로는 오류를 완전히 무시하고 싶을 때도 있다.
# 이럴 때 pass를 사용한다.
try:
    # 설정 파일을 읽으려 시도
    with open("설정파일.txt", 'r') as f:
        config = f.read()
except FileNotFoundError:
    pass # 설정 파일이 없어도 계속 진행

# 프로그램의 주요 기능은 계속 수행
print("프로그램이 정상적으로 실행됩니다.")

# 오류 일부러 발생시키기
# 파이썬은 raise 문을 사용해 오류를 강제로 발생시킬 수 있다.
# 상황:
# Bird 클래스를 상속받는 자식 클래스는
# 반드시 fly라는 함수를 구현하도록 만들고 싶은 경우
class Bird:
    def fly(self):
        raise NotImplementedError

#  Eagle 클래스는 fly 메서드를 오버라이딩하여 구현하지 않았다.
class Eagle(Bird):
    pass

eagle = Eagle()
# 따라서 eagle 객체의 fly 메서드를 수행하는 순간
# Bird 클래스의 fly 메서드가 수행되어 NotImplementedError가 발생한다.
# 상속받는 클래스에서 메서드를 재구현하는 것을 '메서드 오버라이딩'이라고 한다.
# eagle.fly()

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()