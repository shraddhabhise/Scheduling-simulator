# Entry point for starting the Simulator
from Jobs import Job
from Fcfs import Fcfs as fcfs
from Priority import Priority as  priority
from CFS import CFS as cfs
import argparse
import Jobs


def main():
    print("Starting Simulator")
    parser = argparse.ArgumentParser()
    requiredArgs = parser.add_argument_group('required arguments')
    requiredArgs.add_argument("-n","--jobs",metavar="",help="Number of Jobs to be run on a scheduling Algorithm", type=int, required=True,action="store")
    requiredArgs.add_argument("-t", "--cputime",metavar="",help="CPU Time", required=True,action="store", type=int)
    njobs=parser.parse_args().jobs
    cpuTime=parser.parse_args().cputime

    # njobs = 4
    # cpuTime = 4
    cfs_Job_List=[]
    priority_Job_List = []

    if njobs > 0 and cpuTime > 0:
        # call the create jobs methods from the Jobs file
        job_List = Jobs.create_Jobs(njobs)
        # print("Started Jobs execution through FCFS Scheduling")
        # fcfs_Job_List=fcfs().execute_fcfs(njobs,cpuTime,job_List)
        # print("Finished Jobs execution through FCFS Scheduling")

        # print("Started Jobs execution through Priority Scheduling")
        # priority_Job_List=priority().execute_priority(njobs,cpuTime,job_List)
        # print("Finished Jobs execution through Priority Scheduling")

        print("Started Jobs execution through CFS Scheduling")
        cfs_Job_List = cfs().execute_priority(njobs, cpuTime, job_List)
        print("Finished Jobs execution through CFS Scheduling")
        priority_Job_List = priority().execute_priority(njobs, cpuTime, job_List)
        for x in range(0, len(cfs_Job_List)):
            print("job id, arrival time, execution time", int(cfs_Job_List[x].JobId),
                  int(cfs_Job_List[x].priority), int(cfs_Job_List[x].execution_time))


    print("Simulator Exiting")


if __name__ == "__main__":
    main()


