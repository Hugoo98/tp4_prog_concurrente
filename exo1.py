# coding:utf-8
import threading
import time

my_lock = threading.RLock()

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        i=0
        list = {2, 3, 8, 9, 12}
        while i<1:
            with my_lock:
                for n in list:
                    print("square de ",n,"est : ",n ** 2 )
                    print("cube du ", n, "est : ",n ** 3 )
                    time.sleep(0.2)
            i+=1

if __name__ == "__main__":

    # creating thread
    t1 = MyThread()
    t2 = MyThread()

    # starting thread 1
    # starting thread 2
    t1.start()
    t2.start()

    # wait until thread 1 is completely executed
    # wait until thread 2 is completely executed
    t1.join()
    t2.join()

    # both threads completely executed
    print("Done!")
