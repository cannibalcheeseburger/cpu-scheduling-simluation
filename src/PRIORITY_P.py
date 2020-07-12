import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')


def schedulingProcess( process_data):
    start_time = []
    exit_time = []
    s_time = 0
    sequence_of_process = []
    process_data.sort(key=lambda x: x[1])
    '''
    Sort processes according to the Arrival Time
    '''
    while 1:
        ready_queue = []
        normal_queue = []
        temp = []
        for i in range(len(process_data)):
            if process_data[i][1] <= s_time and process_data[i][4] == 0:
                temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][3],
                                process_data[i][5]])
                ready_queue.append(temp)
                temp = []
            elif process_data[i][4] == 0:
                temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4],
                                process_data[i][5]])
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
    calculateTurnaroundTime( process_data)
    calculateWaitingTime( process_data)
    twt = [p[8] for p in process_data]
    tat = [p[7] for p in process_data]
    ctime = [p[6] for p in process_data]
    return twt,tat,ctime,sequence_of_process

def calculateTurnaroundTime( process_data):
    total_turnaround_time = 0
    for i in range(len(process_data)):
        turnaround_time = process_data[i][6] - process_data[i][5]

        total_turnaround_time = total_turnaround_time + turnaround_time
        process_data[i].append(turnaround_time)



def calculateWaitingTime( process_data):
    total_waiting_time = 0
    for i in range(len(process_data)):
        waiting_time = process_data[i][6] - process_data[i][1]
        '''
        waiting_time = turnaround_time - burst_time
        '''
        total_waiting_time = total_waiting_time + waiting_time
        process_data[i].append(waiting_time)


def plot_graph(process_data):
    processes = [p[0] for p in process_data]
    twt = [p[8] for p in process_data]
    tat = [p[7] for p in process_data]
    ctime = [p[6] for p in process_data]

    plt.plot(processes,twt,label='Waiting Time')
    plt.plot(processes, tat, label = 'TurnAround Time')
    plt.plot(processes, ctime, label = 'Completion Time')

    plt.legend(loc='best')
    plt.savefig('./output/PRIORITY_NP_output.png')
    plt.show()
    plt.close(fig='all')

def printData( process_data,sequence_of_process):
    process_data.sort(key=lambda x: x[0])
    '''
    Sort processes according to the Process ID
    '''
    print("Process_ID  Arrival_Time  Rem_Burst_Time   Priority        Completed  Orig_Burst_Time Completion_Time  Turnaround_Time  Waiting_Time")
    for i in range(len(process_data)):
        for j in range(len(process_data[i])):
            print(process_data[i][j], end='\t\t')
        print()
    print('\nAverage Turnaround Time:',sum(p[7] for p in process_data)/len(process_data))
    print('Average Waiting Time:',sum(p[8] for p in process_data)/len(process_data))
    print("Throughput: ",len(process_data)/max([p[6] for p in process_data]))
    print(f'Sequence of Process: {sequence_of_process}')



def priority_p():
    process_data = []
    with open('./inputs/PRIORITY_P.txt', 'r') as f:
        f.readline()
        for line in f.readlines():
            temporary = []
            process , burst , arrival,priority = (line.split(" "))
            temporary.extend([process, int(arrival), int(burst),int(priority), 0,int(burst)])
            process_data.append(temporary)

    sequence_of_process =  schedulingProcess( process_data)
    printData(process_data,sequence_of_process)
    plot_graph(process_data)

if __name__ == "__main__":
    priority_p()