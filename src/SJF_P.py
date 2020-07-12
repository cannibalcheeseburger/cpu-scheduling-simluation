import matplotlib.pyplot as plt;

plt.style.use('fivethirtyeight')
 
def findWaitingTime(processes, n, wt):  
    rt = [0] * n 
    for i in range(n):  
        rt[i] = processes[i][1] 
    complete = 0
    t = 0
    minm = 999999999
    short = 0
    check = False
  
    while (complete != n): 
        for j in range(n): 
            if ((processes[j][2] <= t) and 
                (rt[j] < minm) and rt[j] > 0): 
                minm = rt[j] 
                short = j 
                check = True
        if (check == False): 
            t += 1
            continue
              
        rt[short] -= 1
        minm = rt[short]  
        if (minm == 0):  
            minm = 999999999
        if (rt[short] == 0):  
  
            complete += 1
            check = False
            fint = t + 1
            wt[short] = (fint - processes[short][1] -processes[short][2]) 
  
            if (wt[short] < 0): 
                wt[short] = 0
        t += 1


def findTurnAroundTime(processes, n, wt, tat):  
    
    for i in range(n): 
        tat[i] = processes[i][1] + wt[i]  


  
def findavgTime(processes, n):  
    wt = [0] * n 
    tat = [0] * n  
    findWaitingTime(processes, n, wt)  
    findTurnAroundTime(processes, n, wt, tat)  
    compl_time = []
    for i in range(n):
         compl_time.append(tat[i]+processes[i][2])
    return wt, tat,compl_time


def print_data(processes,w_time,tat_time,compl_time,n):
    
    print("Processes\t\tBurst Time\t\tWaiting",  
                    "Time\t\tTurn-Around Time\t\tArrival Time\t\tCompletion Time" )
    for i in range(n): 
 
        print(" ", processes[i][0], "\t\t\t",  
                   processes[i][1], "\t\t\t",  
                   w_time[i], "\t\t\t", tat_time[i],'\t\t\t\t',processes[i][2],'\t\t\t',compl_time[i]) 
  
    print("\nAverage waiting time = %.5f "%(sum(w_time) /n) ) 
    print("Average turn around time = ", sum(tat_time) / n)  
    print("Throughput  =  ",n/max(compl_time))


def  plot_graph(processes,waiting_time,compl_time,turn_around_time):

    plt.plot(processes,waiting_time,label = "Waiting time")
    plt.plot(processes,compl_time,label = "Completion time")
    plt.plot(processes,turn_around_time,label = "Turnaround Time")
    plt.text(4,2,'Throughput = %.5f'  % (len(processes)/ compl_time[len(processes)-1]))
    plt.title("SJF PREEMPTIVE")
    plt.xlabel("Processes")
    plt.ylabel("Time Units")
    plt.legend()
    plt.savefig('./output/SJF_P_output.png')
    plt.show()



def sjf_p():
    process_data = []
    #change dis
    with open('./inputs/SJF_P.txt','r') as  f:
        f.readline()
        for line in f.readlines():
            temporary = []
            process , burst , arrival = (line.split(" "))
            temporary.extend([process, int(burst), int(arrival)])
            process_data.append(temporary)
    n = len(process_data)
    w_time,tat_time,compl_time =  findavgTime(process_data, n) 
    print_data(process_data, w_time, tat_time,compl_time,n)
    plot_graph([p[0] for p in process_data],w_time,compl_time,tat_time)
    plt.close(fig='all')

# Driver code  
if __name__ =="__main__": 
    sjf_p()

