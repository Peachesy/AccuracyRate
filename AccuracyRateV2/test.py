import threading

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self) -> None:
        print("开始" + self.name)
        print("结束" + self.name)

thread1=myThread(1,"1111111",1)
thread2=myThread(2,"22222222",2)

thread1.start()
thread2.start()
thread1.join()
thread2.join()