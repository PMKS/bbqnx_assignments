import time
import math


def getFactorial(val):
    if val == 0:
        return 1
    return val*getFactorial(val-1)



def getTables(n):
    start_time = time.time()
    try:
        if n < 0:
            raise Exception("InvalidNumberException")
        for i in range (1,n):
            j=1
            while(j < 10):
                print(f"{i}*{j}={i*j},{getFactorial(i*j)}")
                j+=1
                time.sleep(0.1)
    except :
        print ("Invalid range Exception")
    finally:
        end_time = time.time()
        print(f"Total execution time is :{math.floor(end_time-start_time)}")



getTables(int(input("enter a number: ")))