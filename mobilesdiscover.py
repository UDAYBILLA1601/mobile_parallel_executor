from sys import platform
from typing import List
import adbutils


class MobilesList:
    """
    Class to discover connected mobile devices.
    """
    __WINDOWS = 'win32'
    __MAC = 'darwin'

    def __init__(self):
        self.__android_available: List[str] = []
        self.__ios_available: List[str] = []

        if platform == MobilesList.__WINDOWS:
            self.discover_android_mobiles()
        elif platform == MobilesList.__MAC:
            self.discover_ios_mobiles()

    def discover_android_mobiles(self) -> None:
        """
        Discovers connected Android devices using adb.
        """
        devices = adbutils.adb.device_list()
        self.__android_available = [device.serial for device in devices]

    def discover_ios_mobiles(self) -> None:
        """
        Placeholder for discovering iOS devices.
        """
        pass

    def get_android_ids(self) -> List[str]:
        """
        Returns the list of connected Android device IDs.
        :return: List of Android device IDs
        """
        return self.__android_available

    def get_ios_ids(self) -> List[str]:
        """
        Returns the list of connected iOS device IDs.
        :return: List of iOS device IDs
        """
        return self.__ios_available

    def number_of_android_connected(self) -> int:
        """
        Returns the number of connected Android devices.
        :return: Number of connected Android devices
        """
        return len(self.__android_available)

    def number_of_ios_connected(self) -> int:
        """
        Returns the number of connected iOS devices.
        :return: Number of connected iOS devices
        """
        return len(self.__ios_available)

    def get_connected_mobiles(self) -> List[str]:
        """
        Returns the list of connected mobile device IDs based on the platform.
        :return: List of connected device IDs
        """
        if platform == MobilesList.__WINDOWS:
            return self.get_android_ids()
        elif platform == MobilesList.__MAC:
            return self.get_ios_ids()
        return []
