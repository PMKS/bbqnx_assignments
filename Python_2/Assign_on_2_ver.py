import time
import math


def fact(val):
    if val == 0:
        return 1
    return val * fact(val - 1)


def getProd(var):
    start_time = time.time()
    try:
        if var < 0:
            raise Exception("InvalidNumberException")

        for i in xrange(1, var):
            j = 1
            while (j <= 10):
                print
                "{0}*{1}= {2},{3},{4}".format(i, j, i * j, i / j, fact(i * j))
                j += 1
                time.sleep(0.1)

    except NameError, err:
        print "Exception Occured, {0}".format(err)
    finally:
        end_time = time.time()
        print("total execution time is {0}".format(math.floor(end_time - start_time)))


getProd(input('enter a number: '))