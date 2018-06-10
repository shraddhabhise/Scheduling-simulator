import matplotlib.pyplot as plot

# Reference: https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
class PlotGraphs(object):

        # def __init__(self, waiting_time_list, completion_time_list):
        #         self.waiting_time_list = waiting_time_list
        #         self.completion_time_list = completion_time_list



        def compare_waiting_times(self,waiting_time_list):
                # x-coordinates of left sides of bars
                left = [1, 2, 3]


                # heights of bars
                height = waiting_time_list

                print("Waiting times from PlotGraphs:")
                for x in range(len(height)):
                    print("height[0]:", height[x])

                # labels for bars
                tick_label = ['Fcfs', 'Priority', 'CFS']

                # plotting a bar chart
                plot.bar(left, height, tick_label=tick_label,
                         width=0.6, color=['blue'])

                # naming the x-axis
                plot.xlabel('x - axis (Algorithms)')
                # naming the y-axis
                plot.ylabel('y - axis (Time in Seconds)')
                # plot title
                plot.title('Waiting Time Comparison')

                # function to show the plot
                plot.show()

        def compare_completion_times(self, completion_time_list):
                # x-coordinates of left sides of bars
                left = [1, 2, 3]


                # heights of bars
                height = completion_time_list

                print("Completion times from PlotGraphs:")
                for x in range(len(height)):
                    print("height:", height[x])

                # labels for bars
                tick_label = ['Fcfs', 'Priority', 'Linux']

                # plotting a bar chart
                plot.bar(left, height, tick_label=tick_label,
                         width=0.6, color=['blue'])

                # naming the x-axis
                plot.xlabel('x - axis (Algorithms)')
                # naming the y-axis
                plot.ylabel('y - axis (Time in Seconds)')
                # plot title
                plot.title('Completion Time Comparison')

                # function to show the plot
                plot.show()


        def compare_turnaround_times(self, turnaround_time_list):
                # x-coordinates of left sides of bars
                left = [1, 2, 3]


                # heights of bars
                height = turnaround_time_list

                print("Turn Around Times from PlotGraphs:")
                for x in range(len(height)):
                    print("height:", height[x])

                # labels for bars
                tick_label = ['Fcfs', 'Priority', 'Linux']

                # plotting a bar chart
                plot.bar(left, height, tick_label=tick_label,
                         width=0.6, color=['blue'])

                # naming the x-axis
                plot.xlabel('x - axis (Algorithms)')
                # naming the y-axis
                plot.ylabel('y - axis (Time in Seconds)')
                # plot title
                plot.title('Turn Around Time Comparison')

                # function to show the plot
                plot.show()

        def compare_throughputs(self, throughput_list):
                # x-coordinates of left sides of bars
                left = [1, 2, 3]


                # heights of bars
                height = throughput_list

                print("Throughput from PlotGraphs:")
                for x in range(len(height)):
                    print("height:", height[x])

                # labels for bars
                tick_label = ['Fcfs', 'Priority', 'Linux']

                # plotting a bar chart
                plot.bar(left, height, tick_label=tick_label,
                         width=0.6, color=['blue'])

                # naming the x-axis
                plot.xlabel('x - axis (Algorithms)')
                # naming the y-axis
                plot.ylabel('y - axis (Time in Seconds)')
                # plot title
                plot.title('Throughput Comparison')

                # function to show the plot
                plot.show()

