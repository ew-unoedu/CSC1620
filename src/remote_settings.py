# Project_1 created and submitted by Edwin Wright.
# CSCI1620-850.1255

import csv
import os.path

class RemoteSettings:
    """
    Class to construct RemoteSettings objects.
    """
    def __init__(self):
        # Declare and set initial variables.
        self.channel_dict: dict = {0: 'Binaries/off.jpg',
                                   1: 'Binaries/nbc.jpg', 2: 'Binaries/cbs.jpg', 3: 'Binaries/abc.jpg',
                                   4: 'Binaries/pbs.jpg', 5: 'Binaries/fox.jpg', 6: 'Binaries/weather.jpg',
                                   7: 'Binaries/cnn.jpg', 8: 'Binaries/msnbc.jpg', 9: 'Binaries/scifi.jpg',
                                   10: 'Binaries/hdmi1.jpg', 11: 'Binaries/hdmi2.jpg', 12: 'Binaries/hdmi3.jpg'}
        # Initial settings if no file exists
        self.settings_dict: dict = {'current_input': 11, 'current_channel': 1, 'volume': 0}
        # Settings file to retain last settings when powered off.
        self.settings_file: str = "settings.csv"

    def remote_settings_on(self) -> dict:
        """
        Function to read settings file to update settings_dict attribute from RemoteSettings class object.
        """
        # Checks if there is an existing settings file and assigns key values, if none, initial dict is used.
        if os.path.isfile(self.settings_file):
            with open(self.settings_file, 'r') as input_file:
                csv_file = csv.reader(input_file, delimiter=',')
                for row in csv_file:
                    self.settings_dict.update({'current_input': int(row[0]),
                                          'current_channel': int(row[1]),
                                          'volume': int(row[2])
                                          })

        return self.settings_dict

    def remote_settings_off(self, settings: list):
        """
        Function to write from a list of settings when the remote is powered off.
        """
        with open(self.settings_file, 'w', newline='') as output_csv_file:
            csv_file = csv.writer(output_csv_file, delimiter=',')
            csv_file.writerow(settings)
