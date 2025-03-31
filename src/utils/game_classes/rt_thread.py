
class RealTimeThread ():

    def __init__(self, name = 'default name', tick_rate = 1.0, tick_functions = [], start_scene = 'None', module_data = None):
        self.tick_rate = 1.0
        self.tick_functions = tick_functions
        self.name = name
        self.thread_position = 'init'
        self.current_scene = start_scene
        self.module_data = module_data

    def __str__(self):
        return f'This is the {self.name} thread. This thread is currently at {self.thread_position} with a tick rate of {self.tick_rate}'
    
    def tick(self):
        self.thread_position = 'Running.'
        try:
            for function in self.tick_functions:
                function()
        except:
            print(f'TICK ERROR AT {self.name} THREAD: position at {self.thread_position}')
        self.thread_position = 'Thread completed.'