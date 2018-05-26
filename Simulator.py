#Entry point for starting the Simulator.

import Timer
from Jobs import Job
from Fcfs import Fcfs as fcfs
from Priority import Priority as  priority


class Simulator:

    fcfs_job_list = []
    priority_job_list = []
    linux_job_list = []

    def simulator(algorithm, num_of_jobs, cpu_slice):
        algorithm_to_execute = algorithm.capitalize()
        job_List = Job.create_Jobs(num_of_jobs)

        if(algorithm_to_execute == "Fcfs"):
            Simulator.fcfs_job_list = fcfs.execute_fcfs(num_of_jobs,cpu_slice,job_List )

        elif algorithm_to_execute == "Priority":
            priority.execute_priority(num_of_jobs,cpu_slice,job_List)

    def main():
        print("Starting Simulator")
        cpuTimer = Timer.Timer(count=50, step=1)
        #cpuTimer.start_Timer()
        #cpuTimer.stop()

        #Create required number of Jobs for scheduling using Jobs.Creat_Jobs
        #job_List=Job.create_Jobs(200)
        Simulator.simulator("fcfs", 4, 5)



if __name__== "__main__":
    Simulator.main()


