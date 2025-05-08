import os
import subprocess

# Run a Bash command using os.system
print("📁 Listing directory contents using os.system:")
os.system("ls")

# Run a Bash command using subprocess.run
print("\n📂 Listing directory contents using subprocess.run:")
subprocess.run(["ls"])
