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
    completed_jobs = []
    completion_time = 0
    fcfs_throughput = 0

    @staticmethod
    def sort_job(job_list):
        """ Sort the job list based on arrival time
        :param job_list:Job
        :return: sorted_job_list
        """
        sorted_job_list = sorted(job_list, key=lambda x: x.arrival_time, reverse=False)
        return sorted_job_list

    def calculate_wait_time_different_arrival(self):
        """Calculate wait time when arrival times are different
        This method calculates the waiting time
        of each job and stores it in
        waiting_time attribute of the job object
        :return:
        """
        Fcfs.completed_jobs[0].set_waiting_time(0)

        for x in range(1, len(Fcfs.completed_jobs)):
            wait_time = Fcfs.completed_jobs[x - 1].get_arrival_time() + Fcfs.completed_jobs[x - 1].get_execution_time() + Fcfs.completed_jobs[x - 1].get_waiting_time() - Fcfs.completed_jobs[x].get_arrival_time()

            if wait_time < 0:
                wait_time = 0
            # else:
            #    wait_time = abs(wait_time)
            Fcfs.completed_jobs[x].set_waiting_time(wait_time)

    def calculate_wait_time_same_arrival(self):
        """Calculate wait time when arrival times are same
        This method calculates the waiting time
        of each job and stores it in waiting_time attribute
        of respective job object
        :param
        :return:
        """
        Fcfs.completed_jobs[0].set_waiting_time(0)

        for x in range(1, len(Fcfs.completed_jobs)):
            wait_time = Fcfs.completed_jobs[x - 1].get_waiting_time() + Fcfs.completed_jobs[x - 1].get_execution_time()
            Fcfs.completed_jobs[x].set_waiting_time(wait_time)

    def calculate_completion_time(self,job_list,cpu_time_slice):
        """Calculate completion time
        This method calculates the completion time
        of each job and stores calculated
        completion_time in the respective job object
        :param job_list:
        :param cpu_time_slice:
        :return:
        """

        self.convert_to_queue(job_list)

        while len(Fcfs.queue) > 0:
            running = Fcfs.queue.popleft()
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
            Fcfs.completed_jobs.append(running)
        print("Fcfs.completion_time",  Fcfs.completion_time)

    def calculate_turn_around_time(self):
        """ Calculate turn around time
        This method calculates the turn around time
        of the each job and stores it in turn_around_time attribute
        :param completed_job_list:
        :return:
        """
        for x in range(0, len(Fcfs.completed_jobs)):
            turn_around_time = Fcfs.completed_jobs[x].get_waiting_time() + Fcfs.completed_jobs[x].get_execution_time()
            Fcfs.completed_jobs[x].set_turnaround_time(turn_around_time)

    def convert_to_queue(self,job_list):
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
        for x in range(len(Fcfs.completed_jobs) - 1, 0, -1):
            if Fcfs.completed_jobs[x].get_arrival_time() == Fcfs.completed_jobs[x - 1].get_arrival_time():
                is_arrival_same = True
        return is_arrival_same


    def print_job_list(self, job_list):
        for x in range(len(job_list)):
            print("JobId:", job_list[x].get_job_id(), "Execution time:",job_list[x].get_execution_time() , "Arrival Time: ",job_list[x].get_arrival_time())
            print("Completion time ",job_list[x].get_completion_time())
            print("Turnaround time ", job_list[x].get_turnaround_Time())
            print("Waiting", job_list[x].get_waiting_time())
            print("-----------------------------------------------------------------")

    def execute_fcfs(self,num_of_jobs, cpu_slice, job_list):
        """
        Execute various methods of Fcfs
        to calculate completion time, waiting time
        and turn around time.
        :param cpu_slice:
        :param job_list:
        :return:
        """

        # Sort jobs based on arrival Time
        sorted_job_list = self.sort_job(job_list)

        self.calculate_completion_time(sorted_job_list, cpu_slice)


        if self.check_arrival_time == True:
            print("Calling -------> calculate_wait_time_same_arrival")
            self.calculate_wait_time_same_arrival()
        else:
            print("Calling -------> calculate_wait"
                  "_time_different_arrival")
            self.calculate_wait_time_different_arrival()

        self.calculate_turn_around_time()


        self.print_job_list(Fcfs.completed_jobs)

        print("FCFS Completion time:", Fcfs.completion_time)
        Fcfs.fcfs_throughput = num_of_jobs / Fcfs.completion_time
        print("Throughput: ", self.fcfs_throughput)

        return Fcfs.completed_jobs
