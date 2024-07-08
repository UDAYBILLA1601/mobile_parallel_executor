from typing import Dict, Union
from portscanner import SocketPorts
from mobilesdiscover import MobilesList


class AssignPorts:
    """
    Class to assign ports to available mobile devices.
    """

    def __init__(self):
        self.__mob = MobilesList()
        self.__scanner = SocketPorts()
        self.android_available = self.__mob.get_android_ids()
        self.ios_available = self.__mob.get_ios_ids()
        self.__ports_mapper: Dict[str, Union[int, tuple]] = {}
        self.assign_ports()

    def assign_ports(self) -> None:
        """
        Assigns available ports to Android and iOS devices.
        """
        available_ports = self.__scanner.get_available_ports()
        if available_ports is None:
            return

        for android in self.android_available:
            if available_ports:
                self.__ports_mapper[android] = available_ports.pop(0)

        for ios in self.ios_available:
            if len(available_ports) >= 2:
                self.__ports_mapper[ios] = (available_ports.pop(0), available_ports.pop(0))

    def get_devices_port_map(self) -> Dict[str, Union[int, tuple]]:
        """
        Returns the map of device IDs to assigned ports.
        :return: Dictionary of device IDs and their assigned ports
        """
        return self.__ports_mapper
