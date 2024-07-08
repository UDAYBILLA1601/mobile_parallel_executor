# test_sequence_parser.py

import argparse
import json
import os
from typing import List, Dict
from assignports import AssignPorts
from mobilesdiscover import MobilesList


class CmdLineArgs(argparse.ArgumentParser):
    """
    Class for command line argument parsing.
    """

    def __init__(self):
        super().__init__()
        self.add_argument('--test_order', default=None)
        self.add_argument('--test_package_root', default=None)
        self.add_argument('--test_suit_path', required=True)
        self.add_argument('--virtual_env_path', default=None)
        self.add_argument('--test_config_root', default=None)
        self.add_argument('--target_app', required=True)


class ParseTestSequenceData:
    """
    Class to parse test sequence data and prepare test execution commands.
    """

    def __init__(self):
        parser = CmdLineArgs()
        self.__args = parser.parse_args()
        self.__ports_map = AssignPorts()
        self.__test_suit_path = self.__args.test_suit_path
        self.__test_order = self.__args.test_order
        self.__test_package_root = self.__args.test_package_root
        self.__virtual_env_path = self.__args.virtual_env_path
        self.__mobiles_discovered = MobilesList().get_connected_mobiles()

    def get_virtual_path(self) -> str:
        """
        Returns the path to the virtual environment.
        :return: Path to the virtual environment
        """
        if self.__virtual_env_path is not None:
            return self.__virtual_env_path
        return os.environ.get('VIRTUAL_ENV_PATH', '')

    def get_test_suit_data(self) -> Dict:
        """
        Reads and returns test suite data from the provided path.
        :return: Dictionary containing test suite data
        """
        try:
            with open(self.__test_suit_path, 'r') as f:
                return json.load(f)
        except Exception:
            return {}

    def get_test_suit_order(self) -> List[str]:
        """
        Returns the order of test suites to be executed.
        :return: List of test suite order
        """
        test_suit_data = self.get_test_suit_data()
        if self.__test_order is not None:
            return self.__test_order.split(',')
        return list(test_suit_data.keys())

    def get_test_data(self) -> List[Dict]:
        """
        Prepares and returns the test execution commands.
        :return: List of test execution command dictionaries
        """
        test_exec_list = []

        device_ports_map = self.__ports_map.get_devices_port_map()
        test_suit_data = self.get_test_suit_data()

        for order in self.get_test_suit_order():
            for test in test_suit_data.get(order, []):
                test_execute_command = "python -m test_module "
                test_execute_command += test.get('path', '') + " "
                test_execute_command += ' '.join(test.get('args', []))
                if self.__test_package_root:
                    test_execute_command += f' --test_package_root {self.__test_package_root}'

                if test.get('devices') is None:
                    test['devices'] = self.__mobiles_discovered

                for device in test['devices']:
                    if device in self.__mobiles_discovered:
                        test_cmd_args = {
                            'test_run_cmd': test_execute_command,
                            '--device_id': device,
                            '--port': device_ports_map.get(device)
                        }
                        test_exec_list.append(test_cmd_args)

        return test_exec_list
