from heapq import *
import GtaClient
import itertools

class ClientHeap:
    def __init__(self):
        self._heap = []
        self._client_finder = {}
        self._counter = itertools.count()

    def add_client(self, client: GtaClient)->None:
        pass

    def pop_client(self)->GtaClient:
        pass

    def is_included(self, client: GtaClient)->bool:
        if self._client_finder.get(client.identifier, None):
            return True
        return False

    def __iter__(self):
        for item in sorted(self._heap, key=lambda client: client.priority):
            yield item