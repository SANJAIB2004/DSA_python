import threading
import time
from threading import Thread

t = Thread(target = "sanjai")
print(t)



def Printing():
    print('the thread is running')
    time.sleep(1)

t1 = threading.Thread(target=Printing)
t2 = threading.Thread(target=Printing)
# t3 = threading.Thread(t)
print(t1.start())
t2.start()

t1.join(5)
# print(help())
print(type(t1))

