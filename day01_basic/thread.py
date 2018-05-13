import threading
import logging


def thread_func(x):
    logging.debug('logging test')
    print('%d\n' % (x * 100))


threads = []
for i in range(5):
    threads.append(threading.Thread(target=thread_func, args=(100,)))

for thread in threads:
    thread.start()

# 防止执行的线程未结束，进程就已经结束了
for thread in threads:
    thread.join()
