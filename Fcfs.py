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

    @staticmethod
    def sort_job(job_list):
        """ Sort the job list based on arrival time
        :param job_list:Job
        :return:
        """
        sorted_job_list = sorted(job_list, key=lambda x: x.arrival_time, reverse=False)
        print("Sorted List: ")
        for x in range(0, len(sorted_job_list)):
            print("job id, arrival time, execution time", int(sorted_job_list[x].JobId),
                  int(sorted_job_list[x].arrival_time), int(sorted_job_list[x].execution_time))
        return sorted_job_list


    def calculate_wait_time_different_arrival(self, job_list):
        """Calculate wait time when arrival times are different
        This method calculates the waiting time
        of each job and stores it in
        waiting_time attribute of the job object
        :param job_list: Job
        :return:
        """
        self.convert_to_queue(job_list)

        if len(self.queue) > 0:
            first_job = self.queue.popleft()
            first_job.set_waiting_time(0)
            previous_job = first_job
            print("job id, arrival time, execution time, waiting time", int(first_job.JobId), int(first_job.arrival_time),
                int(first_job.execution_time), int(first_job.waiting_time))

        while len(self.queue) > 0:
            running = self.queue.popleft()
            wait_time = running.get_arrival_time() - previous_job.get_arrival_time() - previous_job.get_execution_time()
            if wait_time > 0:
                wait_time = 0
            else:
                wait_time = abs(wait_time)
            running.set_waiting_time(wait_time)

            print("job id, arrival time, execution time, waiting time", int(running.JobId), int(running.arrival_time),int(running.execution_time), int(running.get_waiting_time()))
            previous_job = running


    def calculate_wait_time_same_arrival(self, job_list):
        """Calculate wait time when arrival times are same
        This method calculates the waiting time
        of each job and stores it in waiting_time attribute
        of respective job object
        :param job_list:Job
        :return:
        """
        self.convert_to_queue(job_list)
        if len(self.queue) > 0:
            first_job = self.queue.popleft()
            first_job.set_waiting_time(0)
            previous_job = first_job
            print("job id, arrival time, execution time, waiting time", int(first_job.JobId), int(first_job.arrival_time),int(first_job.execution_time), int(first_job.waiting_time))

        while len(self.queue) > 0:
            running = self.queue.popleft()
            wait_time = previous_job.get_waiting_time() + previous_job.get_execution_time()
            running.set_waiting_time(wait_time)
            print("job id, arrival time, execution time, waiting time", int(running.JobId), int(running.arrival_time),int(running.execution_time), int(running.get_waiting_time()))
            previous_job = running


    def calculate_completion_time(self, job_list,cpu_time_slice):
        """Calculate completion time
        This method calculates the completion time
        of each job and stores calculated
        completion_time in the respective job object
        :param job_list:
        :param cpu_time_slice:
        :return:
        """
        completion_time = 0
        self.convert_to_queue(job_list)

        while len(self.queue) > 0:
            running = self.queue.popleft();
            job_burst = running.get_execution_time()
            running.set_status("RUNNING")

            while job_burst > 0:
                job_burst = job_burst - cpu_time_slice
                if job_burst < 0:
                    completion_time = completion_time + job_burst + cpu_time_slice
                    remaining_slice = abs(job_burst)
                    cpu_time_slice = remaining_slice
                else:
                    completion_time = completion_time + cpu_time_slice

            running.set_status("COMPLETED")
            running.set_completion_time(completion_time)
            print("Job id, Completion time:", running.JobId, completion_time)
            self.completed_job_list.append(running)


    def calculate_turn_around_time(self, job_list):
        """ Calculate turn around time
        This method calculates the turn around time
        of the each job and stores it in turn_around_time attribute
        :param job_list:
        :return:
        """
        for x in range(0, len(job_list) - 1):
            turn_around_time = job_list[x].get_waiting_time() + job_list[x].get_execution_time()
            job_list[x].set_turn_around_time(turn_around_time)


    def convert_to_queue(self, job_list):
       """
       Convert the input list to queue
       :param job_list:
       :return:
       """
       for x in range(0, len(job_list)):
            self.queue.append(job_list[x])


    def create_jobs(self):
        """
        Create jobs to execute
        :return:
        """

        for x in range(0, 3):
            exec_time = random.randint(1, 30)
            job = Job(job_id=x, execution_time=exec_time)
            job.JobId = x
            job.set_arrival_time(random.randint(1, 30))
            self.ready_job_list.append(job)


    def main(self):
        #Create Jobs
        is_arrival_same = False

        self.create_jobs()

        # Sort Arrival Time
        sorted_job_list = Fcfs.sort_job(self.ready_job_list)

        print("Calling -------> calculate_completion_time")

        self.calculate_completion_time(sorted_job_list, 5)

        for x in range(len(self.completed_job_list) - 1, 0, -1):
            if self.completed_job_list[x].get_arrival_time() == self.completed_job_list[x-1].get_arrival_time():
                is_arrival_same = True

        if is_arrival_same:
            print("Calling -------> calculate_wait_time_same_arrival")
            self.calculate_wait_time_same_arrival(self.completed_job_list)
        else:
            print("Calling -------> calculate_wait_time_different_arrival")
            self.calculate_wait_time_different_arrival(self.completed_job_list)

        self.calculate_turn_around_time(self.completed_job_list)


if __name__ == "__main__":
    f = Fcfs()
    f.main()



