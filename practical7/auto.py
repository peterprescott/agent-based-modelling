import subprocess

for i in range(0,1000,100):
    subprocess.run(f"python model.py 0 {i} 100 10")

