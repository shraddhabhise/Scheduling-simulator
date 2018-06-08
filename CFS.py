from Jobs import Job
from collections import deque


class CFS:
    queue = deque()
    queue1 = deque()
    list_CFS = []

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
            sorted_job_list[x].arrival_time = 0
            sorted_job_list[x].cpu_burst = 0
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
        number_of_jobs = num_jobs
        while(len(queue)>0):
            flag = 0
            temp_slice = (cpu_slice / number_of_jobs)
            for i in range(number_of_jobs):
                running = CFS.queue.pop()
                # print("temporary slice:", temp_slice)
                running.execution_time = running.execution_time - temp_slice
                running.cpu_burst = running.cpu_burst + temp_slice
                # print("JobId, Exec time", running.JobId, running.execution_time)

                if (running.execution_time > 0):
                    CFS.queue.appendleft(running)
                    completionTime = completionTime + temp_slice
                    # print("process not complete",completionTime)
                elif running.execution_time <= 0 :
                    flag =flag+1
                    completionTime = completionTime + (temp_slice - abs(running.execution_time))
                    running.completion_time = completionTime
                    # print(Job.get_execution_time(running))
                    waitingTime =running.completion_time - running.cpu_burst
                    running.waiting_time = waitingTime

                    CFS.list_CFS.append(running)
                    print("process complete")
                    print("process id:", running.JobId)
                    print("Completion time is :", running.completion_time)
                    print("Waiting time:", running.waiting_time)
                    print("turnaround time :", running.completion_time-running.arrival_time)

            if flag>0:
                number_of_jobs = number_of_jobs - flag

        return CFS.list_CFS

    def execute_priority(self, num_of_jobs, cpu_slice, job_List):
        sorted_job_list = self.sort_job(job_List)
        for i in range(len(sorted_job_list)):
            CFS.queue.append(sorted_job_list[i])
        # print(CFS.queue)
        CFS.list_CFS = CFS.calculate_times(self, CFS.queue, num_of_jobs, cpu_slice)
        return CFS.list_CFS