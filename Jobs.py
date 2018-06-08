import random
class Job:

    def __init__(self, job_id, execution_time, priority, arrival_time, status="CREATED"):
        self.status = status
        self.waiting_time = None
        self.arrival_time = arrival_time
        self.completion_time = None
        self.execution_time = execution_time  #Time required by the job to execute.
        self.JobId = job_id
        self.priority = priority
        self.turnaroundTime = None

     #Set the timer to count value, passed by from the simulator
    def set_status(self, status):
        self.status=status

    def get_status(self):
        return self.status

    def set_waiting_time(self, waiting_time):
        self.waiting_time=waiting_time

    def get_waiting_time(self):
        return self.waiting_time

    def set_arrival_time(self, arrival_time):
        self.arrival_time=arrival_time

    def get_arrival_time(self):
        return self.arrival_time

    def set_execution_time(self, execution_time):
        self.execution_time = execution_time

    def get_execution_time(self):
        return self.execution_time

    def set_completion_time(self, completion_time):
        self.completion_time=completion_time

    def get_completion_time(self):
        return self.completion_time

    def set_priority(self, priority):
        self.priority = priority

    def get_priority(self):
        return self.priority

    def set_turnaround_time(self, turnaround_Time):
        self.turnaroundTime = turnaround_Time

    def get_turnaround_Time(self):
        return self.turnaroundTime

    def set_job_id(self, JobId):
        self.status = JobId

    def get_job_id(self):
        return self.JobId

def create_Jobs(num_jobs):
    job_list = []

    for x in range(num_jobs):
        exec_time = random.randint(1, 10)
        priority = random.randint(1, 5)
        arrival_time = random.randint(1, 40)
        job_list.append(Job(job_id=x, execution_time=exec_time, priority=priority, arrival_time = x))
    return job_list



