from Jobs import Job
from collections import deque


class CFS:
    queue = deque()
    queue1 = deque()
    list_priority = []

    def sort_job(self, jobList):

        """ Sort the job list based on execution_time
        :param job_list:Job
        :return:
        """
        sorted_job_list = sorted(jobList, key=lambda x: x.execution_time, reverse=False)
        print("Sorted List: ")
        for x in range(0, len(sorted_job_list)):
            print("job id",int(sorted_job_list[x].JobId), "execution time", int(sorted_job_list[x].execution_time))
            # sorted_job_list[x].arrival_time = len(sorted_job_list) - (x+1)
            print("job id",sorted_job_list[x].JobId, " arrival time", sorted_job_list[x].arrival_time)
        return sorted_job_list

    def convert_to_queue(self, sortedList):
        """
        Convert the input list to queue
        :param job_list:
        :return:
        """
        for i in range(len(sortedList)):
            CFS.queue.append(sortedList[i])
        return CFS.queue

    def calculate_times(self, queue, num_jobs, cpu_slice):
        completionTime = 0.0
        remaining_slice = 0
        number_of_jobs = num_jobs
        while(len(queue)>0):
            flag = 0
            temp_slice = (cpu_slice / number_of_jobs)
            for i in range(number_of_jobs):
                running = CFS.queue.pop()
                print("temporary slice:", temp_slice)
                running.execution_time = running.execution_time - temp_slice
                print("JobId, Exec time", running.JobId, running.execution_time)

                if (running.execution_time > 0):
                    CFS.queue.appendleft(running)
                    completionTime = completionTime + temp_slice
                    print("process not complete",completionTime)
                else:
                    flag =flag+1
                    completionTime = completionTime + abs(running.execution_time)
                    running.completion_time = completionTime + running.arrival_time
                    running.waiting_time = running.completion_time -(running.arrival_time+running.execution_time)
                    print("process complete")
                    print("process id:", running.JobId)
                    print("Completion time is :", running.completion_time)
                    print("Waiting time:", running.waiting_time)
                    print("turnaround time :", running.completion_time-running.arrival_time)
                    # running.completion_time = completionTime
            if flag>0:
                number_of_jobs = number_of_jobs - flag

    def execute_priority(self, num_of_jobs, cpu_slice, job_List):
        sorted_job_list = self.sort_job(job_List)
        # queue = CFS.convert_to_queue(sorted_job_list)
        for i in range(len(sorted_job_list)):
            CFS.queue.append(sorted_job_list[i])
        # print(CFS.queue)
        CFS.list_cfs = CFS.calculate_times(self, CFS.queue, num_of_jobs, cpu_slice)
        return CFS.list_cfs