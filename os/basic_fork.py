"""We can split off from the main process with os.fork"""
import os
import time

print("Starting")
pid = os.fork()

if pid:  # a non-zero pid means we're the parent
    print(f"Parent waiting 5 second for child {pid=}")
    time.sleep(5)
    os.kill(pid, 9)
else:
    while True:
        print("Child running...")
        time.sleep(1)
print(f"Finished. {pid=}")
