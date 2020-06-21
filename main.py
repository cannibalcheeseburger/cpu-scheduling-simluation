import os
import src

if os.sys.platform[0]=='l':
    clear  = 'clear'
else:
    clear = 'cls'

def main():
    while True:
        os.system(clear)
        print("=============== MAIN MENU ===============")
        print("\nAnalyse Performance Of Scheduling Algorithms:")
        print("\n1.First Come First Serve (FCFS)")
        print("2.Shortest Job First (SJF) -- PREEMPTIVE")
        print("3.Shortest Job First (SJF) -- NON PREEMPTIVE")
        print("4.Priority Scheduling -- PREEMPTIVE")
        print("5.Priority Scheduling -- NON PREEMPTIVE")
        print("6.Round Robin")
        print("7.ALL OF THE ABOVE AND COMPARE")
        print("0.Exit\n")
        try:
            choice = int(input("\nENTER YOUR OPTION:"))
        except ValueError:
            os.system(clear)
            print("=========== Enter Valid Choice ==========")
            input("\n press any button to continue.....")
            continue
        os.system(clear)
        if choice<8 and choice >= 0:
            pass
        else:
            print("=========== Enter Valid Choice ==========")
            input("\n press any button to continue.....")
        src.fcfs()
        input()
        
if __name__ == "__main__":
    main()