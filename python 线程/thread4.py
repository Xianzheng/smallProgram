from threading import Thread,Lock
import os,time
def work(threadName):
    
    lock.acquire()

    # print(threadName)
    if n:
        print(n.pop())
    
    
    lock.release()
if __name__ == '__main__':
    
    
    lock=Lock()
    n=[i for i in range(50000)]
    total = []
    for i in range(5):
        total.append('thread' + str(i))
    
    start =time.time()
    while n:
        
        p = Thread(target=work,args= ('t1',))
        p.start()
        p.join()
        # p1 = Thread(target=work,args= ('p1',))
        # p1.start()
        # p1.join()
        # p2 = Thread(target=work,args= ('p2',))
        # p2.start()
        # p2.join()
        

    
    end = time.time()
    
    print('Running time: %s Seconds'%(end-start))

#0.237
#0.239

#2.383 1
#2.349 2
#2.333 3
#2.300 4
