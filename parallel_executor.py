import multiprocessing
import os
from multiprocessing import Manager, Lock
from time import sleep
from psutil import process_iter
from assignports import AssignPorts
from test_sequence_parser import ParseTestSequenceData
from mobilesdiscover import MobilesList
from portscanner import SocketPorts
from typing import Dict


def kill_node_processes() -> None:
    """
    Terminates all running Node.js processes.
    """
    for proc in process_iter():
        if proc.name() in ['node.exe', 'node']:
            proc.kill()
            sleep(2)


def script_executor(test_execute_args: Dict, lock: Lock, port: int, device_id: str) -> None:
    """
    Executes the test script with the given arguments.
    :param test_execute_args: Dictionary of test execution arguments
    :param lock: Multiprocessing lock
    :param port: Port number
    :param device_id: Device ID
    """
    lock.acquire()
    virtual_path = ParseTestSequenceData().get_virtual_path()
    os.chdir(virtual_path)
    os.system('activate')

    test_script = ' '.join([f"{key} {value}" if key != 'test_run_cmd' else value for key, value in
                            test_execute_args.items()])

    os.system(test_script)

    while not SocketPorts.is_port_available(port):
        print(f"port busy: {port} for {device_id}")
    sleep(3)
    lock.release()


if __name__ == "__main__":
    kill_node_processes()

    parser = ParseTestSequenceData()
    mobile_list = MobilesList()
    manager = Manager()
    ports_map = AssignPorts()

    device_port_map = ports_map.get_devices_port_map()
    mobiles_discovered = mobile_list.get_connected_mobiles()
    device_locks: Dict[str, Lock] = {mobile: manager.Lock() for mobile in mobiles_discovered}

    if not mobiles_discovered:
        print("No Mobiles Discovered. Please connect the Devices")
        exit(0)

    pool = multiprocessing.Pool(processes=6)

    for test_exe_cmd in parser.get_test_data():
        device = test_exe_cmd['--device_id']
        port = test_exe_cmd['--port']
        pool.apply_async(script_executor, args=(test_exe_cmd, device_locks[device], port, device))

    pool.close()
    pool.join()