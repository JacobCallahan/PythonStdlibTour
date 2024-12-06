"""Communicate with forks by using pipes"""
import os
import time

r_desc, w_desc = os.pipe()
pid = os.fork()
if pid:
    os.close(r_desc)
    values = ["Value1", "Value2", "Value3", "Value4", "Value5", "exit"]
    for value in values:
        print(f"Parent: Sending value to child: {value}")
        os.write(w_desc, value.encode())
        time.sleep(1)
    os.close(w_desc)
    os.wait()
else:
    os.close(w_desc)
    while True:
        value = os.read(r_desc, 1024).decode()
        print(f"Child: Received value from parent: {value}")
        if value == "exit":
            print("Child exiting...")
            break
    os.close(r_desc)
