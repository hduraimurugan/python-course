from datetime import  datetime

print(datetime.now())
with open("time_log.txt", "w") as f:
    f.write(f"Script ran at: {datetime.now()} \n")