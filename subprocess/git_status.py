import subprocess

result = subprocess.run(["git", "status"])

print(f"Return code: {result.returncode}")

assert result.returncode == 0
