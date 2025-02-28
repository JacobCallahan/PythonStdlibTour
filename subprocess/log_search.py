import subprocess


result = subprocess.run(
    "grep -i error my_program.log".split(), 
    capture_output=True, 
    text=True
)

print(f"Found the following errors:\n{result.stdout}")
