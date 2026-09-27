import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget


class App(QMainWindow):
    def __init__(self):
        self.app = QApplication.instance() or QApplication(sys.argv)
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("XQ9-Hub")
        self.resize(1024, 768)
        self.setMinimumSize(400, 300)

        self.central_widget = QWidget(self)
        self.central_widget.setObjectName("centralWidget")
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setSpacing(10)

        self.title = QLabel("XQ9 Hub", self)
        self.title.setObjectName("title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.main_layout.addWidget(self.title)
        self.main_layout.addStretch()

        self.setStyleSheet("""
            QMainWindow, #centralWidget {
                background-color: #2c292d;
            }
        """)

        self.update_responsive_layout()

        self.show()

    def update_responsive_layout(self):
        w = self.width()
        h = self.height()

        pad_x = max(1, int(w * 0.01))
        pad_y = max(1, int(h * 0.01))
        self.main_layout.setContentsMargins(pad_x, pad_y, pad_x, pad_y)

        title_h = max(24, int(h * 0.10))
        self.title.setFixedHeight(title_h)

        border_radius = max(2, int(w * 0.012))

        font_size = max(12, int(title_h * 0.35))

        title_w = max(1, w - 2 * pad_x)
        title_pad_left = max(1, int(title_w * 0.05))

        self.title.setStyleSheet(f"""
            #title {{
                background-color: #2b2c3b;
                border-radius: {border_radius}px;
                color: #fdf9f3;
                font-family: 'Consolas', 'Monospace', monospace;
                font-size: {font_size}px;
                font-weight: bold;
                padding-left: {title_pad_left}px;
            }}
        """)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_responsive_layout()

    def mainLoop(self):
        sys.exit(self.app.exec())


if __name__ == "__main__":
    app = App()
    app.mainLoop()
