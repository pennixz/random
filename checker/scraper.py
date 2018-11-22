import subprocess
import time

while True:
    file = 'check_game_mode.cmd'
    subprocess.call([file])
    time.sleep(2)
