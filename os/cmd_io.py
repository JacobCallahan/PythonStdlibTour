"""os.popen allows us to take input or get output"""
import os

process = os.popen("ls -lah")
pwd = process.readlines()
process.close()

for line in pwd:
    print(line.strip())

process = os.popen("wc", "w", buffering=1024)
process.write("This is some\ntest input.\nAnother line of input!")
process.close()
