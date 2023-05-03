from threading import Thread
from time import sleep
from apps.app1.application import App1
from apps.app2.application import App2
from apps.app3.application import App3

class Application(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        print("Application starting")
        app1 = App1(10.0)
        app2 = App2(1.0)
        app3 = App3(2.0)
        
        app1.start()
        app2.start()
        app3.start()



if __name__ == "__main__":
    app = Application(None)
    app.setDaemon(True)
    app.start()
    counter = 0
    while True:
        counter+=1
        sleep(1)
        if counter>31:
            app.join()
        if counter > 50:
            break
        
