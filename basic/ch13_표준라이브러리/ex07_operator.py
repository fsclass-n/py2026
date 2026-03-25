# operator.itemgetter
# operator.itemgetter는
# 주로 sorted와 같은 함수의 key 매개변수에 적용하여
# 다양한 기준으로 정렬할 수 있도록 도와주는 모듈이다.
from operator import itemgetter, attrgetter

# 학생의 이름, 나이, 성적 등의 정보
# 문제: 이 리스트를 나이순으로 정렬하려면?
students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B')
]
# sorted 함수의 key 매개변수에 itemgetter()를 적용
# itemgetter(1)은 students의 아이템인 튜플의 두 번째 요소를 기준으로 정렬하겠다는 의미이다.
# itemgetter(2)와 같이 사용하면 성적순으로 정렬한다.
result = sorted(students, key=itemgetter(1))
print(result)
# [('sally', 17, 'B'), ('jane', 22, 'A'), ('dave', 32, 'B')]

students = [
    {"name": "jane", "age": 22, "grade": "A"},
    {"name": "dave", "age": 32, "grade": "B"},
    {"name": "sally", "age": 17, "grade": "B"}
]
result = sorted(students, key=itemgetter('age'))
print(result)
# [{'name': 'sally', 'age': 17, 'grade': 'B'}, {'name': 'jane', 'age': 22, 'grade': 'A'}, {'name': 'dave', 'age': 32, 'grade': 'B'}]

# operator.attrgetter()
# students 리스트의 요소가 튜플이 아닌 Student 클래스의 객체라면?
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

students = [
    Student("jane", 22, "A"),
    Student("dave", 32, "B"),
    Student("sally", 17, "B")
]

result = sorted(students, key=attrgetter('age'))
print([vars(s) for s in result])
# for s in result:
#     print(s.name, s.age, s.grade)