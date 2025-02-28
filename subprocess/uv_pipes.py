import subprocess

uv_process = subprocess.Popen(
    ["uv", "python", "list"], 
    stdout=subprocess.PIPE
)

grep_process = subprocess.Popen(
    ["grep", "3.13"], 
    stdin=uv_process.stdout, 
    stdout=subprocess.PIPE,
    text=True
)

stdout, stderr = grep_process.communicate()
print(f"Python 3.13 versions:\n{stdout}")
