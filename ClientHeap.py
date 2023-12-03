from heapq import *
from GtaClient import GtaClient
import itertools

REMOVED = None

class ClientHeap:
    def __init__(self):
        self._heap = []
        self._client_finder = {}
        self._counter = itertools.count()

    def add_client(self, client: GtaClient)->None:
        if client.identifier in self._client_finder:
            self.remove_client(client)
        count = next(self._counter)
        entry = [client.priority, count, client]
        self._client_finder[client.identifier] = entry
        heappush(self._heap, entry)

    def remove_client(self, client: GtaClient)->None:
        entry = self._client_finder.pop(client.identifier)
        entry[-1] = REMOVED

    def pop_client(self)->GtaClient:
        while self._heap:
            priority, count, client = heappop(self._heap)
            if client is not REMOVED:
                del self._client_finder[client.identifier]
                return client

    def is_included(self, client: GtaClient)->bool:
        if self._client_finder.get(client.identifier, None):
            return True
        return False

    def __iter__(self):
        for _, _, item in sorted(self._heap, key=lambda client: client[2].priority):
            yield item