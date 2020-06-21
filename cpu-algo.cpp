#include"cpu-algo.h"
#include<bits/stdc++.h>

using namespace std;
class fcfs{

void fcfs::findWaitingTime(int processes[], int n,
                     int bt[], int wt[])
{
    // waiting time for first process is 0
    wt[0] = 0;

    // calculating waiting time
    for (int i = 1; i < n; i++)
        wt[i] = bt[i - 1] + wt[i - 1];
}

// Function to calculate turn around time
void fcfs::findTurnAroundTime(int processes[], int n,
                        int bt[], int wt[], int tat[])
{
    // calculating turnaround time by adding
    // bt[i] + wt[i]
    for (int i = 0; i < n; i++)
        tat[i] = bt[i] + wt[i];
}

//Function to calculate average time
void fcfs::findavgTime()
{
    int n;
    cout << "Enter the no. processes:";
    cin >> n;
    int pid[n], bt[n];
    
    cout<<"\nProcess Id\tBurst Time\n";

    for(int i=0;i<n;i++)
    {
        cin>>pid[i]>>bt[i];
    }

    int wt[n], tat[n], total_wt = 0, total_tat = 0;

    //Function to find waiting time of all processes
    fcfs::findWaitingTime(pid, n, bt, wt);

    //Function to find turn around time for all processes
    fcfs::findTurnAroundTime(pid, n, bt, wt, tat);

    //Display processes along with all details
    cout << "Processes  "
         << " Burst time  "
         << " Waiting time  "
         << " Turn around time\n";

    // Calculate total waiting time and total turn
    // around time
    for (int i = 0; i < n; i++)
    {
        total_wt = total_wt + wt[i];
        total_tat = total_tat + tat[i];
        cout << "   " << i + 1 << "\t\t" << bt[i] << "\t    "
             << wt[i] << "\t\t  " << tat[i] << endl;
    }

    cout << "Average waiting time = "
         << (float)total_wt / (float)n<<endl;
    cout<<(float)total_tat / (float)n;     
    
         
}

};
/////////////////////////////////////////////////////////////////////////////////////////////////
                                /*FCFS  till    here*/
/////////////////////////////////////////////////////////////////////////////////////////////////

class sjfp
{
void sjfp::findWaitingTime(int pid[], int n, int bt[], int at[], int wt[])
{
    int rt[n];

    // Copy the burst time into rt[]
    for (int i = 0; i < n; i++)
        rt[i] = bt[i];

    int complete = 0, t = 0, minm = INT_MAX;
    int shortest = 0, finish_time;
    bool check = false;

    // Process until all processes gets
    // completed
    while (complete != n)
    {

        // Find process with minimum
        // remaining time among the
        // processes that arrives till the
        // current time`
        for (int j = 0; j < n; j++)
        {
            if ((at[j] <= t) &&
                (rt[j] < minm) && rt[j] > 0)
            {
                minm = rt[j];
                shortest = j;
                check = true;
            }
        }

        if (check == false)
        {
            t++;
            continue;
        }

        // Reduce remaining time by one
        rt[shortest]--;

        // Update minimum
        minm = rt[shortest];
        if (minm == 0)
            minm = INT_MAX;

        // If a process gets completely
        // executed
        if (rt[shortest] == 0)
        {

            // Increment complete
            complete++;
            check = false;

            // Find finish time of current
            // process
            finish_time = t + 1;

            // Calculate waiting time
            wt[shortest] = finish_time -
                           bt[shortest] -
                           at[shortest];

            if (wt[shortest] < 0)
                wt[shortest] = 0;
        }
        // Increment time
        t++;
    }
}

// Function to calculate turn around time
void sjfp::findTurnAroundTime(int n, int bt[], int wt[], int tat[])
{
    int total_tat=0;
    // calculating turnaround time by adding
    // bt[i] + wt[i]
    for (int i = 0; i < n; i++)
        tat[i] = bt[i] + wt[i];

   
}

// Function to calculate average time
void sjfp::findavgTime()
{

    cout<<"\nEnter the no. of processes: ";
    int n; cin>>n;
    int pid[n], bt[n], at[n];
    cout << "\nProcess ID\tBurst Time\tArrival Time\n";

    for(int i=0;i<n;i++)
    {
        cin>>pid[i]>>bt[i]>>at[i];
    }

    int wt[n], tat[n], total_wt = 0, total_tat = 0;

    // Function to find waiting time of all
    // processes

    sjfp::findWaitingTime(pid, n, bt, at, wt);

    // Function to find turn around time for
    // all processes
    sjfp::findTurnAroundTime( n, bt, wt, tat);

    // Display processes along with all
    // details
    cout << "Processes "
         << " Burst time "
         << " Waiting time "
         << " Turn around time\n";

    // Calculate total waiting time and
    // total turnaround time
    for (int i = 0; i < n; i++)
    {
        total_wt = total_wt + wt[i];
        total_tat = total_tat + tat[i];
        cout << " " << pid[i] << "\t\t"<< bt[i] << "\t\t " << wt[i] << "\t\t " << tat[i] << endl;
    }


    
    cout << "\nAverage waiting time = "
         << (float)total_wt / (float)n;

    cout<<"\nAvergae TurnAround time ="
        << (float)total_tat/(float)n;    

    cout<<"GG";
    
}

};
            /* ///////////////////////////////////////////////////////////////

                                 SJF PREMPTIVE till here

           /////////////////////////////////////////////////////////////////*/

class sjfnp{

void sjfnp::swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void sjfnp::arrangeArrival(int num, int mat[][6])
{
    for (int i = 0; i < num; i++)
    {
        for (int j = 0; j < num - i - 1; j++)
        {
            if (mat[j][1] > mat[j + 1][1])
            {
                for (int k = 0; k < 5; k++)
                {
                    swap(&mat[j][k], &mat[j + 1][k]);
                }
            }
        }
    }
}

void sjfnp::completionTime(int num, int mat[][6])
{
    int temp, val;
    mat[0][3] = mat[0][1] + mat[0][2];
    mat[0][5] = mat[0][3] - mat[0][1];
    mat[0][4] = mat[0][5] - mat[0][2];

    for (int i = 1; i < num; i++)
    {
        temp = mat[i - 1][3];
        int low = mat[i][2];
        for (int j = i; j < num; j++)
        {
            if (temp >= mat[j][1] && low >= mat[j][2])
            {
                low = mat[j][2];
                val = j;
            }
        }
        mat[val][3] = temp + mat[val][2];
        mat[val][5] = mat[val][3] - mat[val][1];
        mat[val][4] = mat[val][5] - mat[val][2];
        for (int k = 0; k < 6; k++)
        {
            swap(&mat[val][k], &mat[i][k]);
        }
    }
}

void sjfnp::findAvgTime(){
    
    int n;
    int mat[n][6];
    cout<<"\nEnter the no. of processes:"; cin>>n;

    cout<<"\nProcess Id\tBurst Time\tArrival Time\n";
    for(int i=0;i<n;i++)
    {
        cin>>mat[i][0]>>mat[i][2]>>mat[i][1];
    }

    sjfnp::arrangeArrival(n, mat);
    sjfnp::completionTime(n, mat);

    cout<<"\nProcess Id\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time\n";
    for(int i=0;i<n;i++)
    cout<<mat[i][0]<<"\t\t"<<mat[i][2]<<"\t\t"<<mat[i][1]<<"\t\t"<<mat[i][4]<<"\t\t"<<mat[i][5]<<"\n";

   
}
};
/*//////////////////////////////////////////////////////////////////////////////////////////////////////

                        SJF Non_preemptive till here

/////////////////////////////////////////////////////////////////////////////////////////////////////*/


