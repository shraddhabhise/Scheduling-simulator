from Jobs import Job
import random
from collections import deque

"""
This class is used to calculate waiting time,
completion time and turn around time per job and their total averages.
"""


class Fcfs:
    cpu_free = False
    queue = deque()
    remaining_slice = 0
    ready_job_list = []
    wait_time = 0
    completed_job_list = []
    completion_time = 0

    @staticmethod
    def sort_job(job_list):
        """ Sort the job list based on arrival time
        :param job_list:Job
        :return: sorted_job_list
        """
        sorted_job_list = sorted(job_list, key=lambda x: x.arrival_time, reverse=False)
        print("Sorted List: ")
        for x in range(0, len(sorted_job_list)):
            print("job id, arrival time, execution time", int(sorted_job_list[x].JobId),
                  int(sorted_job_list[x].arrival_time), int(sorted_job_list[x].execution_time))
        return sorted_job_list

    def calculate_wait_time_different_arrival(self):
        """Calculate wait time when arrival times are different
        This method calculates the waiting time
        of each job and stores it in
        waiting_time attribute of the job object
        :return:
        """
        Fcfs.completed_job_list[0].set_waiting_time(0)

        print("job id, arrival time, execution time, waiting time", int(Fcfs.completed_job_list[0].JobId),
              int(Fcfs.completed_job_list[0].arrival_time),
              int(Fcfs.completed_job_list[0].execution_time), int(Fcfs.completed_job_list[0].get_waiting_time()))

        for x in range(1, len(Fcfs.completed_job_list)):
            wait_time = Fcfs.completed_job_list[x].get_arrival_time() - Fcfs.completed_job_list[x-1].get_arrival_time() - Fcfs.completed_job_list[x-1].get_execution_time()
            if wait_time > 0:
                wait_time = 0
            else:
                wait_time = abs(wait_time)
            Fcfs.completed_job_list[x].set_waiting_time(wait_time)
            print("job id, arrival time, execution time, waiting time", int(Fcfs.completed_job_list[x].JobId),
                  int(Fcfs.completed_job_list[x].arrival_time),
                  int(Fcfs.completed_job_list[x].execution_time), int(Fcfs.completed_job_list[x].get_waiting_time()))


    def calculate_wait_time_same_arrival(self):
        """Calculate wait time when arrival times are same
        This method calculates the waiting time
        of each job and stores it in waiting_time attribute
        of respective job object
        :param
        :return:
        """
        Fcfs.completed_job_list[0].set_waiting_time(0)
        print("job id, arrival time, execution time, waiting time", int(Fcfs.completed_job_list[0].JobId),
              int(Fcfs.completed_job_list[0].arrival_time),
              int(Fcfs.completed_job_list[0].execution_time), int(Fcfs.completed_job_list[0].get_waiting_time()))

        for x in range(1, len(Fcfs.completed_job_list)):
            wait_time = Fcfs.completed_job_list[x-1].get_waiting_time() + Fcfs.completed_job_list[x-1].get_execution_time()
            Fcfs.completed_job_list[x].set_waiting_time(wait_time)
            print("job id, arrival time, execution time, waiting time", int(Fcfs.completed_job_list[x].JobId), int(Fcfs.completed_job_list[x].arrival_time),
                  int(Fcfs.completed_job_list[x].execution_time), int(Fcfs.completed_job_list[x].get_waiting_time()))

    def calculate_completion_time(self,job_list,cpu_time_slice):
        """Calculate completion time
        This method calculates the completion time
        of each job and stores calculated
        completion_time in the respective job object
        :param job_list:
        :param cpu_time_slice:
        :return:
        """

        Fcfs.convert_to_queue(job_list)

        while len(Fcfs.queue) > 0:
            running = Fcfs.queue.popleft();
            job_burst = running.get_execution_time()
            running.set_status("RUNNING")

            while job_burst > 0:
                job_burst = job_burst - cpu_time_slice
                if job_burst < 0:
                    Fcfs.completion_time = Fcfs.completion_time + job_burst + cpu_time_slice
                    remaining_slice = abs(job_burst)
                    cpu_time_slice = remaining_slice
                else:
                    Fcfs.completion_time = Fcfs.completion_time + cpu_time_slice

            running.set_status("COMPLETED")
            running.set_completion_time(Fcfs.completion_time)
            print("Job id, Completion time:", running.JobId, Fcfs.completion_time)
            Fcfs.completed_job_list.append(running)

    def calculate_turn_around_time(self):
        """ Calculate turn around time
        This method calculates the turn around time
        of the each job and stores it in turn_around_time attribute
        :param completed_job_list:
        :return:
        """
        for x in range(0, len(Fcfs.completed_job_list)):
            turn_around_time = Fcfs.completed_job_list[x].get_waiting_time() + Fcfs.completed_job_list[x].get_execution_time()
            Fcfs.completed_job_list[x].set_turnaround_time(turn_around_time)

    def convert_to_queue(job_list):
       """
       Convert the input list to queue
       :param job_list:
       :return:
       """
       for x in range(0, len(job_list)):
            Fcfs.queue.append(job_list[x])

    def check_arrival_time(self):
        """
        Check if the arrival time of the
        jobs are same or different
        :return:
        """
        is_arrival_same = False
        for x in range(len(Fcfs.completed_job_list) - 1, 0, -1):
            if Fcfs.completed_job_list[x].get_arrival_time() == Fcfs.completed_job_list[x - 1].get_arrival_time():
                is_arrival_same = True
        return is_arrival_same

    def execute_fcfs(num_of_jobs, cpu_slice, job_list):
        """
        Execute various methods of Fcfs
        to calculate completion time, waiting time
        and turn around time.
        :param cpu_slice:
        :param job_list:
        :return:
        """
        fcfs = Fcfs()

        # Sort jobs based on arrival Time
        sorted_job_list = fcfs.sort_job(job_list)

        print("Calling -------> calculate_completion_time")

        fcfs.calculate_completion_time(sorted_job_list, cpu_slice)

        if fcfs.check_arrival_time == True:
            print("Calling -------> calculate_wait_time_same_arrival")
            fcfs.calculate_wait_time_same_arrival()
        else:
            print("Calling -------> calculate_wait_time_different_arrival")
            fcfs.calculate_wait_time_different_arrival()

        fcfs.calculate_turn_around_time()
        print("Throughput: ",fcfs.completion_time/num_of_jobs)

        return fcfs.completed_job_list
