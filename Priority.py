from Jobs import Job
from collections import deque


class Priority:

    queue = deque()

    def sort_job(jobList):

        """ Sort the job list based on arrival time
        :param job_list:Job
        :return:
        """
        sorted_job_list = sorted(jobList, key=lambda x: x.priority, reverse=False)
        print("Sorted List: ")
        for x in range(0, len(sorted_job_list)):
            print("job id, arrival time, execution time", int(sorted_job_list[x].JobId),
                  int(sorted_job_list[x].priority), int(sorted_job_list[x].execution_time))
        return sorted_job_list


    def convert_to_queue(sortedList):
        """
        Convert the input list to queue
        :param job_list:
        :return:
        """
        for i in range(len(sortedList)):
            Priority.queue.append(sortedList[i])
        return Priority.queue


    def calculate_times(queue, num_jobs, cpu_slice):

        completionTime = 0
        remaining_slice = 0
        while len(Priority.queue) > 0:
            running = queue.pop()
            print("JobId, Exec time, Priority", running.JobId, running.execution_time, running.priority)
            Job.set_waiting_time(running, completionTime)
            job_burst = Job.get_execution_time(running)
            while job_burst > 0:
                job_burst = job_burst - cpu_slice
                if job_burst < 0:
                    remaining_slice = abs(job_burst)
                    completionTime = completionTime + job_burst + cpu_slice
                    cpu_slice = remaining_slice

                else:
                    completionTime = completionTime + cpu_slice
            Job.set_completion_time(running, completionTime)
            Job.set_turnaround_time(running, Job.get_completion_time(running))

            print("Completion time", running.completion_time)
            print("Turnaround time", running.turnaroundTime)
            print("Waiting ", running.waiting_time)
        throughput = completionTime / num_jobs
        print(" Throughput ", completionTime, num_jobs, throughput)
        total_TurnarounTime = completionTime / num_jobs
        print("Average Turn around time ", total_TurnarounTime)

    def execute_priority(num_of_jobs,cpu_slice,job_List):
        sorted_job_list = Priority.sort_job(job_List)
        queue = Priority.convert_to_queue(sorted_job_list)
        Priority.calculate_times(queue, num_of_jobs, cpu_slice)



