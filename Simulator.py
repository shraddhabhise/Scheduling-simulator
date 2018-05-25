#Entry point for starting the Simulator.

import Timer
from Jobs import Job
from Fcfs import Fcfs as fcfs
from Priority import Priority as  priority


def simulator(algorithm, num_of_jobs, cpu_slice):
    algorithm_to_execute = algorithm.capitalize()
    job_List = Job.create_Jobs(200)

    if(algorithm_to_execute == "Fcfs"):
        sorted_job_list = fcfs.sort_job(job_List)

        fcfs.calculate_completion_time(sorted_job_list, cpu_slice)

        #Check if the arrival time is same or different, calculate wait time accordingly
        for x in range(len(fcfs.completed_job_list) - 1, 0, -1):
            if fcfs.completed_job_list[x].get_arrival_time() == fcfs.completed_job_list[x - 1].get_arrival_time():
                is_arrival_same = True
        if is_arrival_same:
            print("Calling -------> calculate_wait_time_same_arrival")
            fcfs.calculate_wait_time_same_arrival(fcfs.completed_job_list)
        else:
            print("Calling -------> calculate_wait_time_different_arrival")
            fcfs.calculate_wait_time_different_arrival(fcfs.completed_job_list)

        fcfs.calculate_turn_around_time(sorted_job_list)

        #Call for throughput

    elif algorithm_to_execute == "Priority":

        sorted_job_list = priority.sort_job(job_List)

        queue = priority.convert_to_queue(sorted_job_list)
        priority.calculate_times(queue, num_of_jobs)


def main():
    print("Starting Simulator")
    cpuTimer = Timer.Timer(count=50, step=1)
    #cpuTimer.start_Timer()
    #cpuTimer.stop()

    #Create required number of Jobs for scheduling using Jobs.Creat_Jobs
    job_List=Job.create_Jobs(200)



if __name__== "__main__":
  main()


