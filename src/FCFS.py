import matplotlib.pyplot as plt


def findWaitingTime(processes,  bt, wt, at):  
    service_time = [0] *len(processes) 
    service_time[0] = 0
    wt[0] = 0
    for i in range(1, len(processes)):  
           
        service_time[i] = (service_time[i - 1] +  bt[i - 1])  
  
        wt[i] = service_time[i] - at[i]  
        if (wt[i] < 0): 
            wt[i] = 0
      

def findTurnAroundTime(processes, bt, wt, tat):  
    for i in range(len(processes)): 
        tat[i] = bt[i] + wt[i]  
  
  

def findavgTime(processes,  bt, at):  
    wt = [0] *len(processes)
    tat = [0] *len(processes) 
    findWaitingTime(processes,  bt, wt, at)  
    findTurnAroundTime(processes,  bt, wt, tat)  
  
    print("Processes   Burst Time   Arrival Time     Waiting",  
          "Time   Turn-Around Time  Completion Time \n") 
    total_wt = 0
    total_tat = 0
    for i in range(len(processes)): 
  
        total_wt = total_wt + wt[i]  
        total_tat = total_tat + tat[i]  
        compl_time = tat[i] + at[i]  
        print(" ", i + 1, "\t\t", bt[i], "\t\t", at[i],  
              "\t\t", wt[i], "\t\t ", tat[i], "\t\t ", compl_time)  
  
    print("Average waiting time = %.5f "%(total_wt /len(processes))) 
    print("\nAverage turn around time = ", total_tat / len(processes))  
    return wt


def fcfs():
    #change dis
    processes = []
    burst_time = []
    arrival_time = []
    with open('./inputs/FCFS.txt','r') as  f:
        f.readline()
        for line in f.readlines():
            process , burst , arrival = (line.split(" "))
            processes.append(process)
            burst_time.append(int(burst))
            arrival_time.append(int(arrival))

    print(processes,burst_time,arrival_time)
    wt = findavgTime(processes,  burst_time, arrival_time)

    plt.plot(processes,wt)
    plt.title("First Come First Serve Algo")
    plt.show()
#    findavgTime(processes, len(processes), burst_time,  arrival_time)

if __name__ =="__main__": 
     fcfs()