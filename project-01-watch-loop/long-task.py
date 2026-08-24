import time

print("Long task started...")

time.sleep(120)

with open("task-complete.txt", "w") as f:
    f.write("Task completed successfully!")

print("Long task finished!")