"""os.system can be uses to execute basic commands"""
import os

res = os.system("gnome-system-monitor")
print(f"{res=}")
