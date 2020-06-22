from src import PRIORITY_NP
from src import FCFS
from src import PRIORITY_P
from src import ROUND_ROBIN
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')

def compare():
    processes =[]
    arrival_time = []
    burst_time = []
    priorities = []
    quantum = 5
    with open('./inputs/Compare.txt','r') as  f:
        f.readline()

        for line in f.readlines():
            process , burst , arrival, priority = (line.strip()).split(" ")
            
            processes.append(process)
            burst_time.append(int(burst))
            arrival_time.append(int(arrival))
            priorities.append(int(priority))
            
    x = np.arange(len(processes)) 
    f_waiting, f_turn_around ,f_compl_time = FCFS.findavgTime(processes,burst_time,arrival_time)
      # n changes
    r_waiting,r_turn_around,r_compl_time = ROUND_ROBIN.findavgTime(processes, len(processes), burst_time,arrival_time, quantum) 
    
    totalprocess = len(processes)
    proc = []
    for i in range(len(processes)): 
        l = [] 
        for j in range(4): 
            l.append(0) 
        proc.append(l) 


    for i in range(len(processes)):
        proc[i][0] = arrival_time[i]
        proc[i][1] = burst_time[i]
        proc[i][2] = int(priorities[i])
        proc[i][3] = [i+1]

    proc = sorted (proc, key = lambda x:x[2]) 
    proc = sorted (proc) 
      
    np_waiting,np_turn_around,np_compl_time= PRIORITY_NP.findgc(proc,totalprocess) 

    plt.bar(x, f_waiting, width = 0.25,label = "FCFS")
    plt.bar(x + 0.25, r_waiting, width = 0.25,label = "Round Robin" )
    plt.bar(x+0.5,np_waiting,width=0.25,label = "Priority Non Preemptive")
    plt.xticks(x,processes)
    plt.ylabel("Waiting Time")
    plt.legend()
    plt.savefig("./output/Compare.png")
    plt.show()