import subprocess

result = subprocess.run('echo "another log line" >> my_program.log', shell=True)

print(f"Return code: {result.returncode}")
