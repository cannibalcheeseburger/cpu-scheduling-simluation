import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')


processes = []  
tat = []
twt = []


def priority_p():
    processes_data =[]
     
    with open('./inputs/PRIORITY_P.txt', 'r') as f:
        f.readline()
        for line in f.readlines():
            temporary = []
            process, burst, arrival, prior = (line.split(" "))
            processes.append(process)
            temporary.extend([process, int(arrival), int(burst), int(prior), 0, int(burst)])
            processes_data.append(temporary)
    
    twt, tat,w_time,t_time = schedulingProcess(processes_data) 
    printData(processes_data, t_time, w_time, tat, twt)

def schedulingProcess(process_data):
    start_time = []
    exit_time = []
    s_time = 0
    sequence_of_process = []
    process_data.sort(key=lambda x: x[1])
        
    while 1:
        ready_queue = []
        normal_queue = []
        temp = []
        for i in range(len(process_data)):
            if int(process_data[i][1]) <= s_time and process_data[i][4] == 0:
                temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][3], process_data[i][5]])
                ready_queue.append(temp)
                temp = []
            elif process_data[i][4] == 0:
                temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4], process_data[i][5]])
                normal_queue.append(temp)
                temp = []
        if len(ready_queue) == 0 and len(normal_queue) == 0:
            break
        if len(ready_queue) != 0:
            ready_queue.sort(key=lambda x: x[3], reverse=True)
            start_time.append(s_time)
            s_time = s_time + 1
            e_time = s_time
            exit_time.append(e_time)
            sequence_of_process.append(ready_queue[0][0])
            for k in range(len(process_data)):
                if process_data[k][0] == ready_queue[0][0]:
                    break
            process_data[k][2] = process_data[k][2] - 1
            if process_data[k][2] == 0:       #if burst time is zero, it means process is completed
                process_data[k][4] = 1
                process_data[k].append(e_time)
        if len(ready_queue) == 0:
            normal_queue.sort(key=lambda x: x[1])
            if s_time < normal_queue[0][1]:
                s_time = normal_queue[0][1]
            start_time.append(s_time)
            s_time = s_time + 1
            e_time = s_time
            exit_time.append(e_time)
            sequence_of_process.append(normal_queue[0][0])
            for k in range(len(process_data)):
                if process_data[k][0] == normal_queue[0][0]:
                    break
            process_data[k][2] = process_data[k][2] - 1
            if process_data[k][2] == 0:        #if burst time is zero, it means process is completed
                process_data[k][4] = 1
                process_data[k].append(e_time)
    t_time, tat = calculateTurnaroundTime(process_data)
    w_time, twt = calculateWaitingTime(process_data)
    return twt , tat , w_time ,t_time


def calculateTurnaroundTime(process_data):
    total_turnaround_time = 0
    
    for i in range(len(process_data)):
        turnaround_time = process_data[i][6] - process_data[i][5]
            
        total_turnaround_time = total_turnaround_time + turnaround_time
        process_data[i].append(turnaround_time)

        tat.append(total_turnaround_time)
    
    average_turnaround_time = total_turnaround_time / len(process_data)
       
    return average_turnaround_time, tat

def calculateWaitingTime(process_data):
    total_waiting_time = 0
    for i in range(len(process_data)):
        waiting_time = process_data[i][6] - process_data[i][2]
            
        total_waiting_time = total_waiting_time + waiting_time
        process_data[i].append(waiting_time)
        twt.append(total_waiting_time)
    average_waiting_time = total_waiting_time / len(process_data)
       
    return average_waiting_time, twt

def printData(process_data, average_turnaround_time, average_waiting_time,  tat, twt):
    process_data.sort(key=lambda x: x[0])
        
    print("Process_ID  Arrival_Time  Rem_Burst_Time   Priority  Completed  Orig_Burst_Time Completion_Time  Turnaround_Time  Waiting_Time")
    for i in range(len(process_data)):
        for j in range(len(process_data[i])):

            print(process_data[i][j], end="              ")
        print()

    print(f'Average Turnaround Time: {average_turnaround_time}')

    print(f'Average Waiting Time: {average_waiting_time}')

    print("Throughput  =  ",len(process_data)/max([p[6] for p in process_data]))
    #   print(f'Sequence of Process: {sequence_of_process}')

    plt.plot(processes, twt, '-', label='Waiting Time')
    plt.plot(processes, tat, '--', label='TurnAround Time')
    plt.legend(loc='best')
    plt.savefig('./output/PRIORITY_P_output.png')
    plt.show()
    plt.close(fig='all')


if __name__ == "__main__":
    priority_p()  