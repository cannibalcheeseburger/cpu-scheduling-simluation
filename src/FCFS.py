import matplotlib.pyplot as plt

## Finds waiting time for each process
def findWaitingTime(processes,  burst_time, waiting_time, arrival_time):  
    service_time = [0] *len(processes) 
    service_time[0] = 0
    waiting_time[0] = 0
    for i in range(1, len(processes)):  
           
        service_time[i] = (service_time[i - 1] +  burst_time[i - 1])  
  
        waiting_time[i] = service_time[i] - arrival_time[i]  
        if (waiting_time[i] < 0): 
            waiting_time[i] = 0
      

#Finds Turn Around Time for All processes
def findTurnAroundTime(processes, burst_time, waiting_time, turn_around_time):  
    for i in range(len(processes)): 
        turn_around_time[i] = burst_time[i] + waiting_time[i]  
  
  
#Returns waiting,turn around, completion time for each process
def findavgTime(processes,  burst_time, arrival_time):  

    waiting_time = [0] *len(processes)
    turn_around_time = [0] *len(processes) 
    findWaitingTime(processes,  burst_time, waiting_time, arrival_time)  
    findTurnAroundTime(processes,  burst_time, waiting_time, turn_around_time)  
  
    print("Processes   Burst Time   Arrival Time     Waiting",  
          "Time   Turn-Around Time  Completion Time \n") 
    total_wt = 0
    total_turn_around_time = 0
    compl_time = [0]*len(processes)
    for i in range(len(processes)): 
  
        total_wt = total_wt + waiting_time[i]  
        total_turn_around_time = total_turn_around_time + turn_around_time[i]  
        # Calculate completion time

        compl_time[i] = turn_around_time[i] + arrival_time[i] 
        print(" ", i + 1, "\t\t", burst_time[i], "\t\t", arrival_time[i],  
              "\t\t", waiting_time[i], "\t\t ", turn_around_time[i], "\t\t ", compl_time[i])  
  
    print("Average waiting time = %.5f "%(total_wt /len(processes))) 
    print("\nAverage turn around time = ", total_turn_around_time / len(processes))  
    print('\nThroughput = ', len(processes)/ compl_time[len(processes)-1])
    print('\nAverage Job elapsed time = ',total_turn_around_time/len(processes))
    return waiting_time , turn_around_time ,compl_time


# driver function
def fcfs():
 
    processes = []
    burst_time = []
    arrival_time = []
    #breakpoint
    with open('./inputs/FCFS.txt','r') as  f:
        f.readline()
        for line in f.readlines():
            process , burst , arrival = (line.split(" "))
            processes.append(process)
            burst_time.append(int(burst))
            arrival_time.append(int(arrival))

    #returned waiting time and turn around time
    waiting_time , turn_around_time, compl_time = findavgTime(processes,  burst_time, arrival_time)
    #plotting 
    plt.plot(processes,waiting_time,label = "Waiting time")
    plt.plot(processes,compl_time,label = "Completion time")
    plt.plot(processes,turn_around_time,label = "Turnaround Time")
    plt.text(4,2,'Throughput = %.5f'  % (len(processes)/ compl_time[len(processes)-1]))
    plt.title("First Come First Serve Algo")
    plt.xlabel("Processes")
    plt.ylabel("Time Units")
    plt.legend()
    plt.savefig('./output/FCFS_output.png')
    plt.show()
    input()

if __name__ =="__main__": 
    fcfs()