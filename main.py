# Python Stop Watch
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTime, QTimer

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stop Watch")
        self.setWindowIcon(QIcon("time-tracking.ico"))
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00.00", self)
        self.start = QPushButton("Start", self)
        self.pause = QPushButton("Pause", self)
        self.restart = QPushButton("Restart", self)
        self.timer = QTimer(self)

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        hbox.addWidget(self.start)
        hbox.addWidget(self.pause)  
        hbox.addWidget(self.restart)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)  
        vbox.addLayout(hbox)  
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.setStyleSheet("""  
                           QWidget {
                               font-weight: bold;
                           }
                           QLabel {
                               font-weight: bold;
                               font-size: 70px;
                               color: green;
                               background-color: black;
                               padding: 10px;
                               border-radius: 20px;
                               padding: 30px;
                               font-family: calibri;
                           }
                           QPushButton {
                               font-size: 30px;
                               padding: 20px;
                               font-family: calibri;
                               font-weight: bold;
                           }   
                           """)

        self.start.clicked.connect(self.start_click) 
        self.pause.clicked.connect(self.pause_click)  
        self.restart.clicked.connect(self.restart_click) 

        self.timer.timeout.connect(self.update_display)

    def format_time(self, time):
        hours = time.hour() 
        minutes = time.minute()  
        seconds = time.second()  
        milliseconds = time.msec() // 10  
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

    def start_click(self):
        self.timer.start(10) 

    def pause_click(self):
        self.timer.stop()  

    def restart_click(self):
        self.timer.stop()  
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))


def main():
    app = QApplication(sys.argv) 
    widget = StopWatch()  
    widget.show()  
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

