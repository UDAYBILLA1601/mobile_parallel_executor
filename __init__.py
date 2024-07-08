from psutil import process_iter
from time import sleep


def kill_node_processes():
    for proc in process_iter():
        if proc.name() in ['node.exe', 'node']:
            proc.kill()
            sleep(2)