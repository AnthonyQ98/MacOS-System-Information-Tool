import netgrab
import performgrab

class AllGrab:
    def __init__(self):
        self.grab_all_info()
    def grab_all_info(self):
        netgrab.NetGrab()
        performgrab.PerformGrab()