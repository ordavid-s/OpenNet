from constants import *


class GtaClient:

    @staticmethod
    def empty_client():
        return GtaClient("", "", -1, -1)

    type_client=0
    type_route=1
    def __init__(self, mac: str, ip: str, status: int, priority: int, client_type=type_client):
        self._mac = mac
        self._ip = ip
        self._status = status
        self._type = client_type
        self._priority = priority

    @property
    def identifier(self):
        return self._mac.lower()

    @property
    def type(self):
        return self._type

    @property
    def ip(self):
        return self._ip

    @property
    def status(self):
        return self._status

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value

    def set_value(self, key: str, value: str):
        if key == ClientFeatures.mac:
            self._mac = value
            return

        if key == ClientFeatures.ip:
            self._ip = value
            return

        if key == ClientFeatures.status:
            self._status = int(value)
            return

        if key == ClientFeatures.client_type:
            self._type = int(value)

        if key == ClientFeatures.priority:
            self._priority = int(value)

    def __repr__(self):
        return f"MAC: {self._mac} IP: {self._ip}"