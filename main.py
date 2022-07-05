import os
import datetime
import socket
import keyboard
import sys

class Tooling():
    def __init__(self, user, timestamp):
        self.user = user
        self.timestamp = timestamp

    def do_action(self):
        print(f"Hey Current User: {self.user}.\nIt is currently {self.timestamp}")
        option = self.get_user_option()
        self.do_option_processing(option)


    def do_option_processing(self, option):
        if option == 1:
            print("Showing all information...")
        elif option == 2:
            print("Showing network information...")
        elif option == 3:
            print("Showing performance information...")
        else:
            print("Unexpected input. Exiting...")
            sys.exit()

    def gather_all_information(self):
        pass

    def gather_network_information(self):
        print(f"Local IP Address: {socket.gethostbyname(socket.gethostname())}")
        pass

    def gather_performance_information(self):
        pass

    def get_user_option(self):
        user_option = None
        while user_option not in [1, 2, 3, 4]:
            try:
                user_option = input("What would you like to show:\n\t1) All Information.\n\t2) Network Information\n\t3) Performance Information\n\t4) Exit\n")
                user_option = int(user_option)
                if user_option not in [1,2,3,4]:
                    print("You need to select one of the available options.")
                if user_option == 4:
                    print("Exiting...")
                    sys.exit()
            except ValueError:
                print("You need to select a number from the list shown.")
        return user_option



if __name__ == "__main__":
    new_sys_details = Tooling(os.getlogin(), datetime.datetime.now())
    new_sys_details.do_action()