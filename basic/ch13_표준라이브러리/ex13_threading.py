# threading
# 컴퓨터에서 동작하고 있는 프로그램을 프로세스(process)라고 한다.
# 보통 1개의 프로세스는 1가지 일만 하지만,
# 스레드(thread)를 사용하면 한 프로세스 안에서 2가지 또는 그 이상의 일을 동시에 수행할 수 있다.
import threading
import time


def long_task(): # 5초의 시간이 걸리는 함수
    for i in range(2):
        time.sleep(1) # 1초간 대기한다.
        print("working:%d\n" % i)

print("Start")

for i in range(2): # long_task를 5회 수행한다.
    long_task()

print("End")


#  threading.Thread를 사용하여 만든 스레드 객체가 동시 작업을 가능하게 해 주기 때문이다.
def long_task():
    for i in range(2):
        time.sleep(1)
        print("working:%d\n" % i)

print("Start")

threads = []
for i in range(2):
    t = threading.Thread(target=long_task) # 스레드를 생성한다.
    threads.append(t)

for t in threads:
    t.start() # 스레드를 실행한다.

for t in threads:
    t.join() # join으로 스레드가 종료될때까지 기다린다.

print("End")