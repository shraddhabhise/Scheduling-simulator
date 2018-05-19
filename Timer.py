class Timer:

    def __init__(self, count=100,step=1,cycles=0,stop=False):
        self.count = count
        self.current_cnt=0
        self.step = step
        self.cpu_cycles=cycles
        self.stop=False    #decrements count by step value

     #Set the timer to count value, passed by from the simulator
    def setTimer(self, count):
        self.count=count

    def get_CPUTime(self):
    	return self.current_cnt

    def get_CPUCycles(self):
        return self.cpu_cycles

    #Starts decrementing the count value by step.
    async def start_Timer(self):
        cnt=self.count
        if self.stop==True:
            self.stop=False
        while not self.stop :
            if cnt == 0:
                self.cpu_cycles=self.cpu_cycles+1
                cnt=self.count
            else:
                cnt=cnt-self.step
                self.current_cnt=cnt

    def stop_Timer(self):
    	self.stop=True





