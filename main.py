from messanger.socket import Sockets

class Main():
    def __init__(self):
        self.s = Sockets()
        self.run()
        
        
    def set_up(self):
        self.s.set_name()
        
    def run(self):
        self.set_up()
        while True: 
            self.s.begin()
            
            
if __name__ == "__main__":
    main = Main()