from messanger.socket import Sockets

class Main():
    # creates an instants of the sockets class and calls the run function
    def __init__(self):
        self.s = Sockets()
        self.run()
        
    # Calls the set name from the sockets class function.
    def set_up(self):
        self.s.set_name()
    
    # while the function is running it will call the begin function 
    # from the socket class.
    def run(self):
        self.set_up()
        while True: 
            self.s.begin()
            
            
if __name__ == "__main__":
    main = Main()
