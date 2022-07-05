import os
import datetime

class Tooling():
    def __init__(self, user, timestamp):
        self.user = user
        self.timestamp = timestamp

    def do_action(self):
        print(f"Current User: {self.user}.\nIt is currently {self.timestamp}")


new_sys_details = Tooling(os.getlogin(), datetime.datetime.now())
new_sys_details.do_action()