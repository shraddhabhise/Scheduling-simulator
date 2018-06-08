#!/usr/bin/env python
# Entry point for starting the Simulator
from Fcfs import Fcfs as fcfs
from Priority import Priority as priority
from CFS import CFS as cfs
import argparse
import Jobs
from PlotGraphs import PlotGraphs


class Simulator:

    def display_graphs(self, fcfs_job_list, priority_job_list, cfs_job_list, njobs):

        wait_y_axis = self.populate_y_axis_list(fcfs_job_list, priority_job_list, cfs_job_list, njobs, "wait")
        completion_y_axis = self.populate_y_axis_list(fcfs_job_list, priority_job_list, cfs_job_list, njobs, "completion")
        pg = PlotGraphs()

        pg.compare_waiting_times(wait_y_axis)
        pg.compare_completion_times(completion_y_axis)

    def populate_y_axis_list(self, fcfs_job_list, priority_job_list, cfs_job_list, njobs, time_to_calculate):
        """
        This method calculates either wait time or completion time
        based on value time_to_calculate, and populates the y-axis list
        :param fcfs_job_list:
        :param priority_job_list:
        :param linux_job_list:
        :param njobs:
        :param time_to_calculate:
        :return:
        """
        y_axis_list = []
        if str(time_to_calculate).lower() == "wait":
            # Calculate the wait time for each algorithm
            fcfs_wait_time = self.calculate_avg_wait_time(fcfs_job_list, njobs)
            priority_wait_time = self.calculate_avg_wait_time(priority_job_list, njobs)
            cfs_wait_time = self.calculate_avg_wait_time(cfs_job_list, njobs) # Uncomment this

            # Append each wait time in the y_axis list
            y_axis_list.append(fcfs_wait_time)
            y_axis_list.append(priority_wait_time)
            y_axis_list.append(cfs_wait_time)

            return y_axis_list

        elif str(time_to_calculate).lower() == "completion":
            # Calculate the completion time for each algorithm
            fcfs_completion_time = self.calculate_avg_completion_time(fcfs_job_list, njobs)
            priority_completion_time = self.calculate_avg_completion_time(priority_job_list, njobs)
            cfs_completion_time = self.calculate_avg_completion_time(cfs_job_list, njobs) # Uncomment this

            # Append each completion time in the y_axis list
            y_axis_list.append(fcfs_completion_time)
            y_axis_list.append(priority_completion_time)
            y_axis_list.append(cfs_completion_time)

            return y_axis_list

    def calculate_avg_wait_time(self, job_list, no_of_jobs):
        """
        This method calculates average waiting time
        for given job list
        :param job_list:
        :param no_of_jobs:
        :return:
        """
        total_wait_time = 0
        for x in range(0, len(job_list)):
            total_wait_time = total_wait_time + job_list[x].get_waiting_time()

        avg_wait_time = total_wait_time / no_of_jobs
        return avg_wait_time

    def calculate_avg_completion_time(self, job_list, no_of_jobs):
        """
        This method calculates average waiting time
        for given job list
        :param job_list:
        :param no_of_jobs:
        :return:
        """
        total_completion_time = 0
        for x in range(0, len(job_list)):
            total_completion_time = total_completion_time + job_list[x].get_completion_time()

        avg_completion_time = total_completion_time / no_of_jobs
        return avg_completion_time


def main():
    print("Starting Simulator")
    parser = argparse.ArgumentParser()
    requiredArgs = parser.add_argument_group('required arguments')
    requiredArgs.add_argument("-n", "--jobs", metavar="", help="Number of Jobs to be run on a scheduling Algorithm",
                              type=int, required=True, action="store")
    requiredArgs.add_argument("-t", "--cputime", metavar="", help="CPU Time", required=True, action="store", type=int)

    args = parser.parse_args()

    njobs = args.jobs
    cpuTime = args.cputime

    if njobs > 0 and cpuTime > 0:
        # call the create jobs methods from the Jobs file

        job_List = Jobs.create_Jobs(njobs)
        print("Started Jobs execution through FCFS Scheduling")
        fcfs_job_list = fcfs().execute_fcfs(njobs, cpuTime, job_List)
        print("Finished Jobs execution through FCFS Scheduling")

        print("Started Jobs execution through Priority Scheduling")
        priority_job_list = priority().execute_priority(njobs, cpuTime, job_List)
        print("Finished Jobs execution through Priority Scheduling")

        print("Started Jobs execution through CFS Scheduling")
        cfs_job_list = cfs().execute_priority(njobs, cpuTime, job_List)
        print("Finished Jobs execution through CFS Scheduling")

        # Display graphs
        sim = Simulator()
        sim.display_graphs(fcfs_job_list, priority_job_list, cfs_job_list, njobs)

    print("Simulator Exiting")


if __name__ == "__main__":
    main()
