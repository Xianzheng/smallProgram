from threading import Thread,Lock
import os,time
def work(threadName):
    global n
    lock.acquire()

    temp=n
    print(threadName)
    print(n)
    time.sleep(0.1)
    n=temp-1
    lock.release()
if __name__ == '__main__':
    lock=Lock()
    n=100
    l=[]
    print(time.time())
    for i in range(50):
        p1=Thread(target=work,args= ('thread-1',))
        p2=Thread(target=work,args = ('thread-2',))
        l.append(p1)
        l.append(p2)
        p1.start()
        p2.start()
    
    for p in l:
        p.join()