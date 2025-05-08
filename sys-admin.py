import os
import subprocess

# Run a Bash command using os.system
print("📁 Listing directory contents using os.system:")
os.system("ls")

# Run a Bash command using subprocess.run
print("\n📂 Listing directory contents using subprocess.run:")
subprocess.run(["ls"])

# Run 'ls -l' using subprocess
print("\n📜 Detailed directory listing using subprocess.run with -l:")
subprocess.run(["ls", "-l"])

# Run 'ls -l README.md' to get details for a specific file
print("\n📄 Listing details for README.md using subprocess.run:")
subprocess.run(["ls", "-l", "README.md"])

# Run 'uname -a' to get system information
print("\n🖥️ Gathering system information with uname -a:")
command = "uname"
commandArgument = "-a"
subprocess.run([command, commandArgument])

# Run 'ps -x' to list active processes
print("\n📊 Gathering active process information with ps -x:")
command = "ps"
commandArgument = "-x"
subprocess.run([command, commandArgument])
