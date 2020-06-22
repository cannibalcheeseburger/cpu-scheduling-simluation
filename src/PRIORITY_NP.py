import matplotlib.pyplot as plt;

plt.style.use('fivethirtyeight')


def get_wt_time( wt, proc, totalprocess):  
  
    service = [0] * 5
  
    service[0] = 0
    wt[0] = 0
  
    for i in range(1, totalprocess):  
        service[i] = proc[i - 1][1] + service[i - 1]  
        wt[i] = service[i] - proc[i][0] + 1
  
        if(wt[i] < 0) :      
            wt[i] = 0
          
def get_tat_time(tat, wt, proc, totalprocess):  
  
    for i in range(totalprocess): 
        tat[i] = proc[i][1] + wt[i]  
  
def findgc(proc, totalprocess): 
      
    wt = [0] * 5
    tat = [0] * 5
  
    wavg = 0
    tavg = 0
  
    get_wt_time(wt,proc, totalprocess)  
      
    get_tat_time(tat, wt, proc, totalprocess)  
  
    stime = [0] * 5
    ctime = [0] * 5
    stime[0] = 1
    ctime[0] = stime[0] + tat[0] 
      
    for i in range(1, totalprocess):  
        stime[i] = ctime[i - 1]  
        ctime[i] = stime[i] + tat[i] - wt[i]  

    for i in range(totalprocess): 
        wavg += wt[i]  
        tavg += tat[i]  
          
    return wt, tat,ctime

def print_details(processes,proc,arrival_time,ctime,tat,wt):
     
    print("Process_no\tStart_time\tComplete_time", 
               "\tTurn_Around_Time\tWaiting_Time") 
  
    for i in range(len(processes)):
        print(proc[i][3], "\t\t", arrival_time[i],  
                         "\t\t", end = " ") 
        print(ctime[i], "\t\t", tat[i], "\t\t\t", wt[i])  
  
    print("Average waiting time is : ", end = " ") 
    print(sum(wt) / len(processes)) 
    print("average turnaround time : " , end = " ") 
    print(sum(tat) / len(processes)) 
  
    return wt , tat 


def plot_graph(processes,wt,tat):

    plt.plot(processes, wt, '-',label='Waiting Time')
    plt.plot(processes, tat, '--',label = 'TurnAround Time')
    plt.legend(loc='best')
    plt.savefig('./output/PRIORITY_NP_output.png')
    plt.show()
    plt.close(fig='all')


# Driver code  
def priority_np():

    processes = []
    burst_time = []
    arrival_time = []
    priority = []
    with open('./inputs/PRIORITY_NP.txt', 'r') as f:
        f.readline()
        for line in f.readlines():
            process, burst, arrival, prior = (line.split())
            processes.append(process)
            burst_time.append(int(burst))
            arrival_time.append(int(arrival))
            priority.append(int(prior)) 
    

    totalprocess = 5
    proc = []
    for i in range(5): 
        l = [] 
        for j in range(4): 
            l.append(0) 
        proc.append(l) 
    
    
    for i in range(5):
        proc[i][0] = arrival_time[i]
        proc[i][1] = burst_time[i]
        proc[i][2] = priority[i]
        proc[i][3] = [i+1]

    proc = sorted (proc, key = lambda x:x[2]) 
    proc = sorted (proc) 
      
    wt, tat,ctime = findgc(proc,totalprocess) 
    print_details(processes,proc,arrival_time,ctime,tat,wt)

    plot_graph(processes,wt,tat)
    


if __name__ =="__main__": 
    priority_np()
