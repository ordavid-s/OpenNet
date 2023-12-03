class OpCodes:
    SUCCESS = 0  # Managed to get internet access with client/route
    FAIL = 1  # Did not manage to get internet access with client/route
    NOT_TRIED = 2  # have not tried client/route yet
    UNKNOWN = 3  # for routes, when didn't work could be client did not have access

class ClientFeatures:
    mac = "MAC"
    ip = "IP"
    status = "STATUS"
    client_type = "CLIENT_TYPE"
    priority = "PRIORITY"