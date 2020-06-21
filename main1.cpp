#include<bits/stdc++.h>
#include"cpu-algo.h"
using namespace std;

int main(){
    
        int algo_num,proc_num;            
        int array[2];
        //burst time, arrival time, priority, quantum
        string options[7] = {"\n1.First Come First Serve(FCFS) ",
                             "\n2.Shortest Job First (SJF) -- PREEMPTIVE",
                             "\n3.Shortest Job First (SJF) -- NON PREEMPTIVE",
                             "\n4.Priority Scheduling -- PREEMPTIVE",
                             "\n5.Priority Scheduling -- NON PREEMPTIVE",
                             "\n6.Round Robin",
                             "\n0. Exit"};

        cout << "=============== MAIN MENU ===============\n";
        cout << "\nAnalyse Performance Of Scheduling Algorithms:\n";
        for(int i=0;i<7;i++) cout<<options[i];
        cout<<"\n\nSelect an algorithm:";
        cin>>algo_num;

                /* Showing the menu and selection of algorithms. */

                /* Next is no. of process and different variables required for the algorithm choosen. */

//////////////////////////////////////////////////////////////////////////////////////////////////////////////

        switch (algo_num)
        {
        case 1: 
           fcfs obj1;
           obj1.findavgTime();

        case 2: 
           sjfp obj2;
           obj2.findavgTime();

        case 3: 
            sjfnp obj3;
            obj3.findAvgTime();

        case 4: 
            break;

        case 5: break;
        case 6: break;
        case 0: return 0;
        default:
        {
            
            cout << "\n=============== ENTER VALID VALUE ==========\n\n\n";
            
        }

        }

        
        return 0;
        }
        
