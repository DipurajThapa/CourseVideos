# file: practice/solutions/task3.py
system = "Windows"
if system == "Windows":
    command = ".venv\\Scripts\\activate"
else:
    command = "source .venv/bin/activate"
print(f"On {system}, type: {command}")
