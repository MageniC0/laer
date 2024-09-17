import os

def cla(i):
    if not os.path.exists(i):
        os.makedirs(i)
        print(f"创建文件夹\033[94m{i}\033[0m.")
    else:
        print(f"文件夹\033[94m{i}\033[0m已存在.")

def clb(i):
    a_=[]
    a0=os.path.abspath(i)
    for a1,_,a2 in os.walk(a0):
        a3 = a1.replace(a0,'').count(os.sep)
        a_.append("|   "*a3+f"[{os.path.basename(a1)}]\n")
        a_.extend("|   "*(a3+1)+f"{a6}\n" for a6 in a2)
    print("\033[90m"+"".join(a_))

def lu(i):
    cla(i)
    clb(i)

lu("input/")
lu("output/")