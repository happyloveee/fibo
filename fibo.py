# fibonacci sequence

def fibo(num):
    if num < 3:
        num =1
    else:
        return ibo(num-1) + fibo(num-2) 

if __name=='__main__':
    print(fibo(5))
