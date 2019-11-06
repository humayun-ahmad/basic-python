import threading

class buckysMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())
x = buckysMessenger(name = 'send out the messege')
y = buckysMessenger(name = 'recive out the messge')
x.start()
y.start()
