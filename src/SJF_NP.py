import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')



def schedulingProcess(  process_data):
    start_time = []
    exit_time = []
    s_time = 0
    process_data.sort(key=lambda x: x[1])
    '''
    Sort processes according to the Arrival Time
    '''
    for i in range(len(process_data)):
        ready_queue = []
        temp = []
        normal_queue = []

        for j in range(len(process_data)):
            if (process_data[j][1] <= s_time) and (process_data[j][3] == 0):
                temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                ready_queue.append(temp)
                temp = []
            elif process_data[j][3] == 0:
                temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                normal_queue.append(temp)
                temp = []

        if len(ready_queue) != 0:
            ready_queue.sort(key=lambda x: x[2])
            '''
            Sort the processes according to the Burst Time
            '''
            start_time.append(s_time)
            s_time = s_time + ready_queue[0][2]
            e_time = s_time
            exit_time.append(e_time)
            for k in range(len(process_data)):
                if process_data[k][0] == ready_queue[0][0]:
                    break
            process_data[k][3] = 1
            process_data[k].append(e_time)

        elif len(ready_queue) == 0:
            if s_time < normal_queue[0][1]:
                s_time = normal_queue[0][1]
            start_time.append(s_time)
            s_time = s_time + normal_queue[0][2]
            e_time = s_time
            exit_time.append(e_time)
            for k in range(len(process_data)):
                if process_data[k][0] == normal_queue[0][0]:
                    break
            process_data[k][3] = 1
            process_data[k].append(e_time)

    calculateTurnaroundTime(  process_data)
    calculateWaitingTime(  process_data)

    waiting_time = [p[6] for p in process_data]
    turn_around_time = [p[5] for p in process_data]
    compl_time = [p[4] for p in process_data]
    return waiting_time,turn_around_time,compl_time


def calculateTurnaroundTime(  process_data):
    total_turnaround_time = 0
    for i in range(len(process_data)):
        turnaround_time = process_data[i][4] - process_data[i][1]
        '''
        turnaround_time = completion_time - arrival_time
        '''
        total_turnaround_time = total_turnaround_time + turnaround_time
        process_data[i].append(turnaround_time)
 

def calculateWaitingTime(  process_data):
    total_waiting_time = 0
    for i in range(len(process_data)):
        waiting_time = process_data[i][5] - process_data[i][2]
        '''
        waiting_time = turnaround_time - burst_time
        '''
        total_waiting_time = total_waiting_time + waiting_time
        process_data[i].append(waiting_time)
 



def printData(  process_data):
    average_turnaround_time  = sum(p[5] for p in process_data)/len(process_data)
    average_waiting_time = sum(p[6] for p in process_data)/len(process_data)
    process_data.sort(key=lambda x: x[0])
    '''
    Sort processes according to the Process ID
    '''
    print("\nProcess_ID\t\t\tArrival_Time\t\t\tBurst_Time\t\t\tCompleted\t\t\tCompletion_Time\t\t\tTurnaround_Time\t\t\tWaiting_Time")

    for i in range(len(process_data)):
        for j in range(len(process_data[i])):

            print(process_data[i][j], end="				")
        print()

    print(f'Average Turnaround Time: {average_turnaround_time}')

    print(f'Average Waiting Time: {average_waiting_time}')

    print("Throughput  =  ",len(process_data)/max([p[4] for p in process_data]))




def plot_graph( process_data):
    plt.plot([p[0] for p in process_data],[po[4] for po in process_data],label = 'Completion Time')
    plt.plot([p[0] for p in process_data],[po[5] for po in process_data],label = 'Turnaround Time')
    plt.plot([p[0] for p in process_data],[po[6] for po in process_data],label = 'Waiting TIme')
    plt.title("Shortest Job First Algo - Non Preemptive")
    plt.xlabel("Processes")
    plt.ylabel("Time Units")
    plt.legend()
    plt.savefig('./output/SJF_NP_output.png')
    plt.show()



def sjf_np():
 
    process_data = []
    #change dis
    with open('./inputs/SJF_NP.txt','r') as  f:
        f.readline()
        for line in f.readlines():
            temporary = []
            process , burst , arrival = (line.split(" "))
            temporary.extend([process, int(arrival), int(burst), 0])
            process_data.append(temporary)
    schedulingProcess(process_data)

    printData( process_data)

    plot_graph(process_data)
    plt.close(fig='all')


if __name__ == '__main__':
    sjf_np()
