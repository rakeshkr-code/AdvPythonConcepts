from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    print(f"executing info() in function f() ---")
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    print(f"executing info() in main line with mainline_process_id {os.getpid()} ---")
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()