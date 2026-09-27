import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget


class App(QMainWindow):
    """XQ9-Hub 遠端管理軟體主程式"""

    def __init__(self):
        # 確保 QApplication 實例存在
        self.app = QApplication.instance() or QApplication(sys.argv)
        super().__init__()

        self.initUI()

    def initUI(self):
        # 設定視窗標題與初始尺寸（可自由調整大小 / Resize）
        self.setWindowTitle("XQ9-Hub")
        self.resize(1024, 768)
        self.setMinimumSize(400, 300)

        # 中央容器元件
        self.central_widget = QWidget(self)
        self.central_widget.setObjectName("centralWidget")
        self.setCentralWidget(self.central_widget)

        # 主要垂直佈局（負責邊框 Padding 與元件排列）
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setSpacing(10)

        # 建立 title 元素（佔 10% height, 100% width）
        self.title = QLabel("XQ9 Hub", self)
        self.title.setObjectName("title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        # 放置於畫面最上方，下方加上 stretch 讓後續元素可順暢向下擴展
        self.main_layout.addWidget(self.title)
        self.main_layout.addStretch()

        # 設定視窗底色 #2c292d
        self.setStyleSheet("""
            QMainWindow, #centralWidget {
                background-color: #2c292d;
            }
        """)

        # 初始套用響應式尺寸與樣式（3% Padding、2% 圓角、10% 高度）
        self.update_responsive_layout()

        # 顯示視窗
        self.show()

    def update_responsive_layout(self):
        """依當前視窗大小動態計算與更新百分比邊距、圓角半徑與元件高度"""
        w = self.width()
        h = self.height()

        # 邊框保留 3% Padding
        pad_x = max(1, int(w * 0.01))
        pad_y = max(1, int(h * 0.01))
        self.main_layout.setContentsMargins(pad_x, pad_y, pad_x, pad_y)

        # title 佔 10% height（100% width 由 QVBoxLayout 自動填滿）
        title_h = max(24, int(h * 0.10))
        self.title.setFixedHeight(title_h)

        # 圓角半徑為 2% width
        border_radius = max(2, int(w * 0.012))

        # 字體大小隨標題列高度自動縮放 (約 35%)
        font_size = max(12, int(title_h * 0.35))

        # 計算 title 寬度與 5% 左邊距（讓文字與元素左邊緣保持 5% 距離）
        title_w = max(1, w - 2 * pad_x)
        title_pad_left = max(1, int(title_w * 0.05))

        # 設定 title 元素背景 #2b2c3b、圓角、字體 Consolas / Monospace、顏色 #fdf9f3、5% 左側內邊距
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
        """當視窗 resize 時即時更新百分比佈局與樣式"""
        super().resizeEvent(event)
        self.update_responsive_layout()

    def mainLoop(self):
        """啟動 PyQt 事件主迴圈"""
        sys.exit(self.app.exec())


if __name__ == "__main__":
    app = App()
    app.mainLoop()
