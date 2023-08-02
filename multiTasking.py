import threading
import time
def threadFunc():
    count=0
    while True:
        print('Hello from new Thread ')
        time.sleep(0.5)
        print(count)
        if count >2:
           break
        count+=1

       
# Create a Thread with a function without any arguments
th = threading.Thread(target=threadFunc)
th.start()

  


