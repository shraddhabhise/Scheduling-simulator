#Entry point for starting the Simulator.

import Timer
import Jobs


def main():
    print("Starting Simulator")
    cpuTimer = Timer.Timer(count=50, step=1)
    #cpuTimer.start_Timer()
    #cpuTimer.stop()

    #Create required number of Jobs for scheduling using Jobs.Creat_Jobs
    job_List=Jobs.create_Jobs(200)



if __name__== "__main__":
  main()


