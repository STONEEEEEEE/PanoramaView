from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QGraphicsPixmapItem, QGraphicsScene
from PyQt5.QtCore import Qt

from GUI import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # 窗口初始化
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.reInit()


    def reInit(self):
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(450, 450))
        self.label.setStyleSheet("border-image:url(:/map/map.jpg)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        # 设定全景框参数
        self.disp_w = 757
        self.disp_h = 552
        self.pos_horz = 0
        self.pos_vert = 0

        # 为方向键绑定事件
        self.pushButton.clicked.connect(self.leftMove)
        self.pushButton_2.clicked.connect(self.downMove)
        self.pushButton_3.clicked.connect(self.rightMove)
        self.pushButton_4.clicked.connect(self.upMove)

        # 选定位置前方向键不可用
        self.setPushbuttonEnable(False)

    # 设置方向键激活状态
    def setPushbuttonEnable(self, bool):
        self.pushButton.setEnabled(bool)
        self.pushButton_2.setEnabled(bool)
        self.pushButton_3.setEnabled(bool)
        self.pushButton_4.setEnabled(bool)


    def mousePressEvent(self, event):  # 鼠标按下事件
        pos = event.pos()  # 返回鼠标所在点QPoint
        self.statusBar.clearMessage()
        self.statusBar.showMessage('Mouse is pressed at (%d,%d) of widget ' % (pos.x(), pos.y()), 0)
        print('Mouse is pressed at (%d,%d) of screen ' % (pos.x(), pos.y()))
        if 80 <= pos.x() <= 125 and 20 <= pos.y() <= 35:
            self.pix = QPixmap("..\\data\\srcfile\\zhuxuan1.jpg")
            img_w = self.pix.width()
            img_h = self.pix.height()
            self.label_2.setFixedSize(self.disp_w, self.disp_h)
            self.verticalScrollBar.setRange(0, img_h - self.disp_h)
            self.verticalScrollBar.valueChanged.connect(self.vertPosChanged)
            self.horizontalScrollBar.setRange(0, img_w - self.disp_w)
            self.horizontalScrollBar.setFixedWidth(self.disp_w)
            self.horizontalScrollBar.valueChanged.connect(self.horzPosChanged)
            # 状态栏提示
            self.statusBar.showMessage("当前位置：校区一号门")
            # 初始化图片位置
            self.label_2.setPixmap(self.pix.copy(self.pos_horz, self.pos_vert, self.disp_w, self.disp_h))
            # 启动方向键控制
            self.setPushbuttonEnable(True)

        elif 190 <= pos.x() <= 240 and 140 <= pos.y() <= 175:
            self.pix = QPixmap("..\\data\\srcfile\\zhuxuan2.jpg")
            img_w = self.pix.width()
            img_h = self.pix.height()
            self.label_2.setFixedSize(self.disp_w, self.disp_h)
            self.verticalScrollBar.setRange(0, img_h - self.disp_h)
            self.verticalScrollBar.valueChanged.connect(self.vertPosChanged)
            self.horizontalScrollBar.setRange(0, img_w - self.disp_w)
            self.horizontalScrollBar.setFixedWidth(self.disp_w)
            self.horizontalScrollBar.valueChanged.connect(self.horzPosChanged)
            # 状态栏提示
            self.statusBar.showMessage("当前位置：中山图书馆")
            # 初始化图片位置
            self.label_2.setPixmap(self.pix.copy(self.pos_horz, self.pos_vert, self.disp_w, self.disp_h))
            # 启动方向键控制
            self.setPushbuttonEnable(True)

        elif 195 <= pos.x() <= 235 and 205 <= pos.y() <= 230:
            self.pix = QPixmap("..\\data\\srcfile\\zhuxuan3.jpg")
            img_w = self.pix.width()
            img_h = self.pix.height()
            self.label_2.setFixedSize(self.disp_w, self.disp_h)
            self.verticalScrollBar.setRange(0, img_h - self.disp_h)
            self.verticalScrollBar.valueChanged.connect(self.vertPosChanged)
            self.horizontalScrollBar.setRange(0, img_w - self.disp_w)
            self.horizontalScrollBar.setFixedWidth(self.disp_w)
            self.horizontalScrollBar.valueChanged.connect(self.horzPosChanged)
            # 状态栏提示
            self.statusBar.showMessage("当前位置：静湖")
            # 初始化图片位置
            self.label_2.setPixmap(self.pix.copy(self.pos_horz, self.pos_vert, self.disp_w, self.disp_h))
            # 启动方向键控制
            self.setPushbuttonEnable(True)

        elif 250 <= pos.x() <= 290 and 360 <= pos.y() <= 390:
            self.pix = QPixmap("..\\data\\srcfile\\zhuxuan4.jpg")
            img_w = self.pix.width()
            img_h = self.pix.height()
            self.label_2.setFixedSize(self.disp_w, self.disp_h)
            self.verticalScrollBar.setRange(0, img_h - self.disp_h)
            self.verticalScrollBar.valueChanged.connect(self.vertPosChanged)
            self.horizontalScrollBar.setRange(0, img_w - self.disp_w)
            self.horizontalScrollBar.setFixedWidth(self.disp_w)
            self.horizontalScrollBar.valueChanged.connect(self.horzPosChanged)
            # 状态栏提示
            self.statusBar.showMessage("当前位置：操场山顶")
            # 初始化图片位置
            self.label_2.setPixmap(self.pix.copy(self.pos_horz, self.pos_vert, self.disp_w, self.disp_h))
            # 启动方向键控制
            self.setPushbuttonEnable(True)


    def horzPosChanged(self, pos):
        self.pos_horz = pos
        self.label_2.setPixmap(self.pix.copy(self.pos_horz, self.pos_vert, self.disp_w, self.disp_h))

    def vertPosChanged(self, pos):
        self.pos_vert = pos
        self.label_2.setPixmap(self.pix.copy(self.pos_horz, self.pos_vert, self.disp_w, self.disp_h))

    def rightMove(self):
        if self.pos_horz + self.disp_w <= self.pix.width():
            self.pos_horz = self.pos_horz + 20
            self.label_2.setPixmap(self.pix.copy(self.pos_horz, self.pos_vert, self.disp_w, self.disp_h))

    def leftMove(self):
        if self.pos_horz >= 20:
            self.pos_horz = self.pos_horz - 20
            self.label_2.setPixmap(self.pix.copy(self.pos_horz, self.pos_vert, self.disp_w, self.disp_h))

    def upMove(self):
        if self.pos_vert >= 20:
            self.pos_vert = self.pos_vert - 20
            self.label_2.setPixmap(self.pix.copy(self.pos_horz, self.pos_vert, self.disp_w, self.disp_h))

    def downMove(self):
        if self.pos_vert + self.disp_h <= self.pix.height():
            self.pos_vert = self.pos_vert + 20
            self.label_2.setPixmap(self.pix.copy(self.pos_horz, self.pos_vert, self.disp_w, self.disp_h))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()  # 创建窗体对象
    mainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
