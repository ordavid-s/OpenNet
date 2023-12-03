class OpCodes:
    SUCCESS = 0  # Managed to get internet access with client/route
    FAIL = 1  # Did not manage to get internet access with client/route
    NOT_TRIED = 2  # have not tried client/route yet
    UNKNOWN = 3  # for routes, when didn't work could be client did not have access

class Priorities:
    # client priorities
    internet_connection = 0
    ip_mac_internet_communication = 1
    ip_mac = 2
    incomplete_internet_communication = 3
    incomplete = 4

    # route priorities
    internet_connection_route = 0
    default_route = 1

class ClientFeatures:
    mac = "MAC"
    ip = "IP"
    status = "STATUS"
    client_type = "CLIENT_TYPE"
    priority = "PRIORITY"
    ssid = "SSID"