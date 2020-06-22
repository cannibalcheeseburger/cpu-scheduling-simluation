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

    np_waiting , np_turn_around, np_compl_time = PRIORITY_NP.findgc(proc,len(processes))

    plt.bar(x, f_waiting, width = 0.25,label = "FCFS")
    plt.bar(x + 0.25, r_waiting, width = 0.25,label = "RR" )
    plt.bar(x+0.5,np_waiting,width=0.25,label="NP")
    plt.xticks(x,processes)

   # ax.bar(X + 0.50, data[2], color = 'r', width = 0.25)
    plt.legend()
    plt.show()