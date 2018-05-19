import random
class Job:

    def __init__(self,job_id,execution_time,status="CREATED"):
        self.status=status
        self.waiting_time=None
        self.arrival_time=None
        self.completion_time=None
        self.execution_time=execution_time  #Time required by the job to execute.
        self.JobId=job_id

     #Set the timer to count value, passed by from the simulator
    def set_Status(self, status):
        self.status=status

    def get_Status(self):
        return self.status

    def set_WaitingTime(self, waiting_time):
        self.waiting_time=waiting_time

    def get_WaitingTime(self):
        return self.waiting_time

    def set_Arrival_Time(self, arrival_time):
        self.arrival_time=arrival_time

    def get_Arrival_Time(self):
        return self.arrival_time

    def set_Completion_Time(self, completion_time):
        self.completion_time=completion_time

    def get_Completion_Time(self):
        return self.completion_time


def create_Jobs(num_jobs):
    job_list=[]

    for x in range(num_jobs):
        exec_time=random.randint(1,1000)
        job_list.append(Job(job_id=x,execution_time=exec_time))
    return job_list



