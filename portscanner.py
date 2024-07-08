import socket
from typing import List, Optional
from mobilesdiscover import MobilesList


class SocketPorts:
    """
    Class to manage and check availability of network ports.
    """
    __HOST: str = '127.0.0.1'
    __DEFAULT_PORT_START: int = 4723
    __DEFAULT_PORT_END: int = 5500

    def __init__(self):
        self.__ports_supported: List[int] = list(
            range(SocketPorts.__DEFAULT_PORT_START, SocketPorts.__DEFAULT_PORT_END))
        self.__available_ports: List[int] = []

        mobiles_obj = MobilesList()
        self.__number_of_ios = mobiles_obj.number_of_ios_connected()
        self.__number_of_android = mobiles_obj.number_of_android_connected()

    @classmethod
    def is_port_available(cls, port: int) -> bool:
        """
        Checks if a specific port is available.
        :param port: Port number to check
        :return: True if port is available, False otherwise
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex((SocketPorts.__HOST, port)) != 0

    def get_available_ports(self) -> Optional[List[int]]:
        """
        Gets a list of available ports based on the number of connected devices.
        :return: List of available ports or None if no ports needed
        """
        required_ports = self.__number_of_android + 2 * self.__number_of_ios
        if required_ports == 0:
            return None

        available_ports = []
        for port in self.__ports_supported:
            if len(available_ports) >= required_ports:
                break
            if SocketPorts.is_port_available(port):
                available_ports.append(port)

        return available_ports
