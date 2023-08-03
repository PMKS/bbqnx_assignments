import os

# os.system("netperf -H192.168.0.2 -l360 -p 12236 -- -m 90000 -M 90000 -S 90000 -s 90000")
import subprocess
buffer =[]

def getBuferAverage():
    """Return the average value of buffer content."""
    global buffer
    sum =0
    for value in buffer:
        sum+=value
    return sum/len(buffer)

def getPerformance(run_count=100):
    """run netpref test for given count and return false when
     any of iteration threshould value is greater than the average with threshold of 50."""
    counter = 0
    while(counter < run_count):
        result = subprocess.run(['netperf -H192.168.0.2 -l360 -p 12236 -- -m 90000 -M 90000 -S 90000 -s 90000'], stdout=subprocess.PIPE)
        value = result.stdout.decode('utf-8')
        throughput = value.split(" ")[-1]
        if abs(throughput,getBuferAverage()) > 50:
            return False # exit from iteration
        counter += 1
        buffer[counter % 5] = throughput
    return True

getPerformance(100)