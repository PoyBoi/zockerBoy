import subprocess

listOutput = subprocess.run(r'python .\zockerBoy\src\logo_det.py --i C:\Users\parvs\Downloads\games_cyberpunk_posters.webp --d 1')

print("Output is", listOutput)