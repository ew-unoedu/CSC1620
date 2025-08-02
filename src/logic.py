# Project_1 created and submitted by Edwin Wright.
# CSCI1620-850.1255

from PyQt6.QtWidgets import *
from gui import *
from remote_settings import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("TV Remote")
        self.setFixedSize(440, 420)

        # Initial settings and states.
        self.settings: RemoteSettings = RemoteSettings()
        self.power_state: bool = False  # True = power on and False = power off
        self.current_input: int = 0
        self.current_channel: int = 0
        self.mute_state: bool = False
        self.volume: int = 0

        self.button_power.clicked.connect(lambda: self.power())  # Power on/off toggle.
        self.button_input.clicked.connect(lambda: self.input(self.current_input))  # Input toggle.

        self.button_mute.clicked.connect(lambda: self.volume_select(99))  # Value used for mute condition.
        self.button_volup.clicked.connect(lambda: self.volume_select(self.volume + 1))  # Increase volume.
        self.button_voldown.clicked.connect(lambda: self.volume_select(self.volume - 1))  # Decrease volume.

        self.button_chanup.clicked.connect(lambda: self.channel_select(self.current_channel + 1))  # Next channel.
        self.button_chandown.clicked.connect(lambda: self.channel_select(self.current_channel - 1)) # Previous channel.

        # Direct channel selections.
        self.button_chan1.clicked.connect(lambda: self.channel_select(1))
        self.button_chan2.clicked.connect(lambda: self.channel_select(2))
        self.button_chan3.clicked.connect(lambda: self.channel_select(3))
        self.button_chan4.clicked.connect(lambda: self.channel_select(4))
        self.button_chan5.clicked.connect(lambda: self.channel_select(5))
        self.button_chan6.clicked.connect(lambda: self.channel_select(6))
        self.button_chan7.clicked.connect(lambda: self.channel_select(7))
        self.button_chan8.clicked.connect(lambda: self.channel_select(8))
        self.button_chan9.clicked.connect(lambda: self.channel_select(9))

    def power(self):
        if self.power_state:
            self.power_state = False
            pixmap = QtGui.QPixmap(self.settings.channel_dict[0])
            self.settings.remote_settings_off([self.current_input, self.current_channel, self.volume])
        else:
            self.power_state = True
            self.mute_state = False
            self.settings.remote_settings_on()
            self.current_input = (self.settings.settings_dict['current_input'] - 1)
            self.current_channel = self.settings.settings_dict['current_channel']
            self.volume = self.settings.settings_dict['volume']
            self.slider_volume.setValue(self.volume)
            pixmap = QtGui.QPixmap(self.settings.channel_dict[self.current_channel])
        self.label_image.setPixmap(pixmap)

    def input(self, input_hdmi: int):
        if self.power_state:
            if input_hdmi == 12:
                self.current_input = 9
                pixmap = QtGui.QPixmap(self.settings.channel_dict[self.current_channel])
            else:
                self.current_input = input_hdmi + 1
                pixmap = QtGui.QPixmap(self.settings.channel_dict[self.current_input])
            self.label_image.setPixmap(pixmap)

    def volume_select(self, volume: int):
        if self.power_state:
            if volume == -1:
                self.volume = 0  # Sets to minimum volume allowed.
            elif volume == 10:
                self.volume = 9  # Sets to maximum volume allowed.
            elif volume == 99:
                if self.mute_state:  # If muted volume unmutes else volume mutes
                    self.mute_state = False
                else:
                    self.mute_state = True
                    self.slider_volume.setValue(volume - volume)
            else:
                self.volume = volume

            if not self.mute_state:
                self.slider_volume.setValue(self.volume)

    def channel_select(self, channel: int):
        if self.power_state:
            if channel == 0:
                self.current_channel = 9
            elif channel == 10:
                self.current_channel = 1
            else:
                self.current_channel = channel

            pixmap = QtGui.QPixmap(self.settings.channel_dict[self.current_channel])
            self.label_image.setPixmap(pixmap)
