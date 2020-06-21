#include<iostream>
#include<fstream>
#include<stdlib.h>
#include"cpu-algo.h"

using namespace std;

int main(){
    while(true){
        int n;
        cout<<"=============== MAIN MENU ===============\n";
        cout<<"\nAnalyse Performance Of Scheduling Algorithms:\n";
        cout<<"\n1.First Come First Serve (FCFS)";
        cout<<"\n2.Shortest Job First (SJF) -- PREEMPTIVE";
        cout<<"\n3.Shortest Job First (SJF) -- NON PREEMPTIVE";
        cout<<"\n4.Priority Scheduling -- PREEMPTIVE";
        cout<<"\n5.Priority Scheduling -- NON PREEMPTIVE";
        cout<<"\n6.Round Robin";
        cout<<"\n0.Exit\n";
        cout<<"\n\nChoose an alogrithm for analysis ";
        cin>>n;
        
        switch(n){
            case 1: break;
            case 2: break;
            case 3: break;
            case 4: break;
            case 5: break;
            case 6: break;
            case 7: break;
            case 0: return 0;
            default:{     
                    system("CLS") ;
                    cout<<"\n=============== ENTER VALID VALUE ==========\n\n\n";
                    system("PAUSE");
                    }
        }

        cout<<"\nDo you want to compare this algorithm with some other algorithm:\n [Y] or [N]\n";
        char ans; cin>>ans;
        if(ans=='N') return 0;
        
        
    system("CLS") ;
    }
    return 0;

}