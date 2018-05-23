from Jobs import Job
from collections import deque
import random

class Priority:

    queue = deque()

    def sort_job(jobList):

        for i in range(0, (len(jobList)-1)):
            for j in range(0, (len(jobList)-i -1)):
                if int(jobList[j].priority) > int(jobList[j+1].priority):
                    temp = jobList[j]
                    jobList[j] = jobList[j+1]
                    jobList[j+1] = temp

        return jobList

    def create_Jobs(num_jobs):
        job_list = []

        for x in range(num_jobs):
            exec_time = random.randint(1, 10)
            priority = random.randint(1, 5)
            job_list.append(Job(job_id=x, execution_time=exec_time, priority=priority))
        return job_list

    def convert_to_queue(sortedList):
        """
        Convert the input list to queue
        :param job_list:
        :return:
        """
        for i in range(len(sortedList)):
            Priority.queue.append(sortedList[i])
        return Priority.queue


    def calculate_times(queue, num_jobs):

        completionTime = 0
        remaining_slice = 0
        cpu_slice = 5
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

            print("completion time", running.completion_time)
            print("turnaround time", running.turnaroundTime)
            print("waiting ", running.waiting_time)
        throughput = completionTime / num_jobs
        print("completion time, num_jobs, Throughput ", completionTime, num_jobs, throughput)
        total_TurnarounTime = completionTime / num_jobs
        print("Average Turn around time ", total_TurnarounTime)

def main():
    print("Starting Simulator")
    num_jobs= 3
    jobList = Priority.create_Jobs(num_jobs)
    sortedList = Priority.sort_job(jobList)

    print("Sorted List: ")
    for x in range(0, len(sortedList)):
        print("Priority, execution time",int(sortedList[x].priority), int(sortedList[x].execution_time))

    queue =Priority.convert_to_queue(sortedList)
    Priority.calculate_times(queue, num_jobs)

if __name__ == "__main__":
    main()



