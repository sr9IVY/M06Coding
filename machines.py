#Student: Sidart Rav
#Filename: machines.py
import multiprocessing
import time
import random
from datetime import datetime

def machine_process(machine_name):
    """Simulates a washing machine or dryer process."""
    wait_time = random.uniform(0, 1)  # Random wait between 0 and 1 seconds
    time.sleep(wait_time)  # Machine waits before running
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current time
    print(f"{machine_name} started at {current_time} after waiting {wait_time:.2f} seconds.")

if __name__ == "__main__":
    machines = ["Clothes Washing Machine 1", "Clothes Washing Machine 2", "Clothes Gas Dryer 1"]
    processes = []

    for machine in machines:
        p = multiprocessing.Process(target=machine_process, args=(machine,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All machines have completed their cycles.")