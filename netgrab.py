import socket


class NetGrab:
    def __init__(self):
        # Call functions to gather information, and store in variables.
        local_ip_address = self.grab_local_ip_address()


        # Display information to user
        print("Local IP Address:", local_ip_address)


    def grab_local_ip_address(self):
        return socket.gethostbyname(socket.gethostname())