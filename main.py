import os
import src

if os.sys.platform[0]=='l':
    clear  = 'clear'
else:
    clear = 'cls'

def choose(choice):
    os.system(clear)

    if choice == 0:
        os.sys.exit()
    elif choice == 1:
        src.fcfs()
    elif choice == 2:
        pass
    elif choice == 3:
        pass        
    elif choice == 4:
        src.priority_p()
    elif choice == 5:
        src.priority_np()
    elif choice == 6:
        src.round_robin()
    elif choice == 7:
        src.compare()
    else:
        print("=========== Enter Valid Choice ==========")
        input("\n press any button to continue.....")

def main():
    while True:
        os.system(clear)
        print("=============== MAIN MENU ===============")
        print("\nAnalyse Performance Of Scheduling Algorithms:")
        print("\n1.First Come First Serve (FCFS)")
        print("\n2.Shortest Job First (SJF) -- PREEMPTIVE")
        print("\n3.Shortest Job First (SJF) -- NON PREEMPTIVE")
        print("\n4.Priority Scheduling -- PREEMPTIVE")
        print("\n5.Priority Scheduling -- NON PREEMPTIVE")
        print("\n6.Round Robin")
        print("\n7.ALL OF THE ABOVE AND COMPARE")
        print("\n0.Exit\n")
        try:
            choice = int(input("\nENTER YOUR OPTION:"))
        except ValueError:
            os.system(clear)
            print("=========== Enter Valid Choice ==========")
            input("\n press any button to continue.....")
            continue
        choose(choice)
        input("press any button to continue.....")
        os.system(clear)
if __name__ == "__main__":
    main()