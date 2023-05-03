from threading import Timer
from time import sleep


class App2(Timer):
    def __init__(self, interval = 1):
        Timer.__init__(self, interval, self.run)
        self.counter = 0

    def run(self):
        while not self.finished.wait(self.interval):
            self.loop()

    def loop(self):
        self.counter+=1
        print(f'App 2 Loop: {self.counter}')
        

if __name__ == "__main__":
    app = App2(1)
    app.run()