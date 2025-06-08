import time
from datetime import  datetime

def task():
    with open("time_log.txt", "a")as f:
        f.write(f"Script ran at: {datetime.now()} \n")
    print(f"Script ran at: {datetime.now()}\n")

while True:
    task()
    time.sleep(5)