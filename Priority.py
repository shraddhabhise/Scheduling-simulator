from Jobs import Job
from collections import deque


class Priority:
#This class is responsible for implementation of Priority scheduling algorithm

   queue = deque()
   list_priority = []
   priority_throughput = 0

   def sort_job(jobList):

       """ Sort the job list based on priorities time
       :param job_list:Jobs
       :return:
       """
       sorted_job_list = sorted(jobList, key=lambda x: x.priority, reverse=False)
       return sorted_job_list

   def convert_to_queue(sortedList):

       """
       Convert the input list to queue
       :param sortedList: list sorted according to priorities
       :return:
       """
       for i in range(len(sortedList)):
           Priority.queue.append(sortedList[i])
       return Priority.queue


   def calculate_times(queue, num_jobs, cpu_slice):

       """
       This definition is responsible to run the priority scheduling algorithm and
       calculate waiting time, completion time, turnaround time for each process and
       total turnaround time and throughput.
       :param queue: queue containing jobs, sorted according to priorities.
       num_jobs: number of jobs
       cpu_slice: cpu time slice for which jobs can run.
       :return:
       """
       #completionTime is a responsible for keeping a count of total completion time
       completionTime = 0

       #remaining_slice is responsible for keeing a count of time slice remaining after
       # a particular process completes running
       remaining_slice = 0

       while len(Priority.queue) > 0:                  # Run till the queue of jobs is not empty
           running = queue.pop()
           print("JobId:", running.JobId, "Execution time:", running.execution_time , "Priority: ", running.priority)
           Job.set_waiting_time(running, completionTime)
           job_burst = Job.get_execution_time(running)
           while job_burst > 0:                        # Run till execution time is still remaining
               job_burst = job_burst - cpu_slice
               if job_burst < 0:
                   remaining_slice = abs(job_burst)
                   completionTime = completionTime + job_burst + cpu_slice
                   cpu_slice = remaining_slice

               else:                                   # if execution time is 0 or less then 0, i.e if process is complete
                   completionTime = completionTime + cpu_slice

           # set completeion time of running job
           Job.set_completion_time(running, completionTime)

           # set turnaround time of running job
           Job.set_turnaround_time(running, Job.get_completion_time(running))

           # append a completed job to a list
           Priority.list_priority.append(running)

           print("Completion time", running.completion_time)
           print("Turnaround time", running.turnaroundTime)
           print("Waiting ", running.waiting_time)
           print("-----------------------------------------------------------------")

       # calculate total throughput
       Priority.priority_throughput = num_jobs / completionTime
       print("Priority Completion time:", completionTime)
       print(" Throughput ", Priority.priority_throughput)

       # calculate total turnaround time
       total_TurnarounTime = completionTime / num_jobs
       print("Average Turn around time ", total_TurnarounTime)
       print("-----------------------------------------------------------------")
       return Priority.list_priority

   def execute_priority(self, num_of_jobs, cpu_slice, job_List):
       sorted_job_list = Priority.sort_job(job_List)
       queue = Priority.convert_to_queue(sorted_job_list)
       Priority.list_priority = Priority.calculate_times(queue, num_of_jobs, cpu_slice)
       return Priority.list_priority



