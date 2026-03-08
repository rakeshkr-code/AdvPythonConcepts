import os

# def f(x):
#     return x*x

# # def f2(name):
# #     print('hello', name)

# # ----------------------------------------------------------

def f(name):
    print(f"Hello, {name}!")

# # ---
def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)
