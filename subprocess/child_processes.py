import random
import subprocess
import time

# sleep X
processes = [
    subprocess.Popen(["sleep", str(random.randint(1, 5))])
    for _ in range(5)
]

# print each process id
for i, process in enumerate(processes, 1):
    print(f"Process {i} started with PID: {process.pid}")

# monitoring processes
while processes:
    print("Checking processes...")
    for i, process in enumerate(processes[:], 1):
        if process.poll() is None:
            print(f"Process {i} (PID: {process.pid}) is still running...")
        else:
            print(f"Process {i} (PID: {process.pid}) has completed.")
            processes.remove(process)
    if processes:
        print(f"{len(processes)} processes are still running.\n")
    time.sleep(1)

print("All processes have completed!")
