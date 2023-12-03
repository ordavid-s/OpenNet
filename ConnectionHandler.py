import GtaClient

class ConnectionHandler:
    def __init__(self):
        pass

    def test_connection(self, interface: str, client: GtaClient, route: GtaClient)->bool:
        print(f"Tested connection for client: {client.identifier} route: {route.ip}")
        return False

    def connect(self, interface: str, client: GtaClient, route: GtaClient)->bool:
        pass
