import matplotlib.pyplot as plt
from statistics import mean

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)


def findWaitingTime(processes, n, burst_time, waiting_time, quantum):  
    rem_burst_time = [0] * n 

    for i in range(n):  
        rem_burst_time[i] = burst_time[i] 
    t = 0
    while(1): 
        done = True
        for i in range(n): 
            if (rem_burst_time[i] > 0) : 
                done = False 
                  
                if (rem_burst_time[i] > quantum) : 
                    t += quantum  
                    rem_burst_time[i] -= quantum  
                else: 
                    t = t + rem_burst_time[i]  
                    waiting_time[i] = t - burst_time[i]  
                    rem_burst_time[i] = 0
        if (done == True): 
            break
              

def findTurnAroundTime(processes, n, burst_time, waiting_time, tat): 
    for i in range(n): 
        tat[i] = burst_time[i] + waiting_time[i]  
  
  

def findavgTime(processes, n, burst_time,arrival_time, quantum):  
    waiting_time = [0] * n 
    tat = [0] * n  
    compl_time = [0]*len(processes)

    findWaitingTime(processes, n, burst_time,  waiting_time, quantum)  

    findTurnAroundTime(processes, n, burst_time, waiting_time, tat)    
    total_waiting_time = 0
    total_tat = 0
    for i in range(n): 
        total_waiting_time = total_waiting_time + waiting_time[i]  
        total_tat = total_tat + tat[i]  
        compl_time[i] = arrival_time[i] + tat[i]
    return waiting_time, tat ,compl_time
      


def plot_graph_normal(processes,waiting_time,compl_time,turn_around_time):
    
    ax1.plot(processes,waiting_time,label = "waiting_time")
    ax1.plot(processes,compl_time,label = "Completion time")
    ax1.plot(processes,turn_around_time,label = "Turnaround Time")

    ax1.legend()
   # plt.savefig('../output/ROUND_ROBIN_output.png')


def plot_graph_quantum(processes, burst_time, arrival_time):
    throughput_quantum = []
    avg_waiting_quantum = []
    avg_turnaround_quantum = []
    avg_completion_quantum =[]
    for n in range(1,10):
        waiting_time,turn_around_time,compl_time =  findavgTime(processes, len(processes), burst_time, arrival_time, n) 
        throughput_quantum.append(len(processes)/ compl_time[len(processes)-1])
        avg_turnaround_quantum.append(mean(turn_around_time))
        avg_completion_quantum.append(mean(compl_time))
        avg_waiting_quantum.append(mean(waiting_time))

    rang = list(range(1,10))
    ax2.plot(rang,throughput_quantum,label="Throughput")
    ax2.plot(rang,avg_waiting_quantum,label="Average waiting_time")
    ax2.plot(rang,avg_completion_quantum,label="Average Completion Time")
    ax2.plot(rang,avg_turnaround_quantum,label="Average Turn Around Time")

    ax2.legend()



def print_details(processes,burst_time,waiting_time,compl_time,tat):
    print("Processes    Burst Time     Waiting  Time    Turn-Around Time    Completion Time") 
    for i in range(len(processes)):
           print(" ", processes[i] , "\t\t", burst_time[i], "\t\t", waiting_time[i], "\t\t", tat[i],"\t\t",compl_time[i]) 
    print("\nAverage waiting_time = %.5f "%(sum(waiting_time) /len(processes)) ) 
    print("Average turn around time = %.5f "% (sum(tat) / len(processes)))  
    print('Throughput = ', len(processes)/ compl_time[len(processes)-1])
    print('Average Job elapsed time = ',sum(tat)/len(processes))



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
    quantum = 2;  
    waiting_time,turn_around_time,compl_time =  findavgTime(processes, len(processes), burst_time, arrival_time, quantum) 
    print_details(processes,burst_time,waiting_time,compl_time,turn_around_time)
    plot_graph_normal(processes,waiting_time,compl_time,turn_around_time)
    plot_graph_quantum(processes, burst_time, arrival_time)
    plt.savefig("./output/ROUND_ROBIN.png")
    plt.show()
    input()

# Driver code  
if __name__ =="__main__": 
      round_robin()

  