import matplotlib.pyplot as plt


def findWaitingTime(processes, n, bt,  
                         wt, quantum):  
    rem_bt = [0] * n 

    for i in range(n):  
        rem_bt[i] = bt[i] 
    t = 0
    while(1): 
        done = True
        for i in range(n): 
            if (rem_bt[i] > 0) : 
                done = False 
                  
                if (rem_bt[i] > quantum) : 
                    t += quantum  
                    rem_bt[i] -= quantum  
                else: 
                    t = t + rem_bt[i]  
                    wt[i] = t - bt[i]  
                    rem_bt[i] = 0
        if (done == True): 
            break
              

def findTurnAroundTime(processes, n, bt, wt, tat): 
    for i in range(n): 
        tat[i] = bt[i] + wt[i]  
  
  

def findavgTime(processes, n, bt,arrival_time, quantum):  
    wt = [0] * n 
    tat = [0] * n  
    compl_time = [0]*len(processes)

    findWaitingTime(processes, n, bt,  wt, quantum)  

    findTurnAroundTime(processes, n, bt, wt, tat)  
  
    print("Processes    Burst Time     Waiting",  "Time    Turn-Around Time    Completion Time") 
    total_wt = 0
    total_tat = 0
    for i in range(n): 
  
        total_wt = total_wt + wt[i]  
        total_tat = total_tat + tat[i]  
        compl_time[i] = arrival_time[i] + tat[i]
        print(" ", processes[i] , "\t\t", bt[i], "\t\t", wt[i], "\t\t", tat[i],"\t\t",compl_time[i]) 
  
    print("\nAverage waiting time = %.5f "%(total_wt /n) ) 
    print("Average turn around time = %.5f "% (total_tat / n))  
    print('Throughput = ', len(processes)/ compl_time[len(processes)-1])
    print('Average Job elapsed time = ',total_tat/len(processes))
    return wt, tat ,compl_time
      

def plot_graph_normal(processes,waiting_time,compl_time,turn_around_time):
    
    plt.plot(processes,waiting_time,label = "Waiting time")
    plt.plot(processes,compl_time,label = "Completion time")
    plt.plot(processes,turn_around_time,label = "Turnaround Time")
    plt.text(4,4,'Throughput = %.5f'  % (len(processes)/ compl_time[len(processes)-1]))
    plt.title("Round Robin Algo")
    plt.xlabel("Processes")
    plt.ylabel("Time Units")
    plt.legend()
    plt.savefig('./output/ROUND_ROBIN_output.png')
    plt.show()


def round_robin():
    processes = []
    burst_time = []
    arrival_time = []
    #breakpoint
    with open('./inputs/ROUND_ROBIN.txt','r') as  f:
        f.readline()
        for line in f.readlines():
            process , burst , arrival = (line.split(" "))
            processes.append(process)
            burst_time.append(int(burst))
            arrival_time.append(int(arrival))


    # Time quantum  
    quantum = 6;  
    waiting_time,turn_around_time,compl_time =  findavgTime(processes, len(processes), burst_time, arrival_time, quantum) 
    plot_graph_normal(processes,waiting_time,compl_time,turn_around_time)
    input()

# Driver code  
if __name__ =="__main__": 
      round_robin()

  