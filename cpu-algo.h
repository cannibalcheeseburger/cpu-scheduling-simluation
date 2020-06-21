#pragma once

class fcfs
{   public:
    void findWaitingTime(int processes[], int n, int bt[], int wt[]);
    void findTurnAroundTime(int processes[], int n,int bt[], int wt[], int tat[]);
    void findavgTime();

};

class sjfp{
    public:
        void findWaitingTime(int pid[], int n, int bt[], int at[], int wt[]);
        void findTurnAroundTime( int n, int bt[], int wt[], int tat[]);
        void findavgTime();
};

class sjfnp{
    public:
        void swap(int *a, int *b);
        void arrangeArrival(int num, int mat[][6]);
        void completionTime(int num, int mat[][6]);
        void findAvgTime();
};

