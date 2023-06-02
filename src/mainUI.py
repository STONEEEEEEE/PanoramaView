import os

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QGraphicsPixmapItem, QGraphicsScene, QGraphicsView, \
    QDialog, QLabel
from PyQt5.QtCore import Qt

from GUI import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # 窗口初始化
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.reInit()

    def panoramaShow(self):
        frame = QImage(outfiles)
        pix = QPixmap.fromImage(frame)
        item = QGraphicsPixmapItem(pix)
        scene = QGraphicsScene()
        scene.addItem(item)
        self.graphicsView.setScene(scene)

    def reInit(self):
        # 设定全景框参数  手工设定，大小随pano_label改变
        self.disp_w = 1157
        self.disp_h = 857
        self.pos_horz = 0
        self.pos_vert = 0

        # 为方向键绑定事件
        self.pushButton.clicked.connect(self.leftMove)
        self.pushButton_2.clicked.connect(self.downMove)
        self.pushButton_3.clicked.connect(self.rightMove)
        self.pushButton_4.clicked.connect(self.upMove)
        self.pushButton_5.clicked.connect(self.showResult1)
        self.pushButton_6.clicked.connect(self.showResult2)

        # 选定位置前方向键不可用
        self.setPushbuttonEnable(False)

    # 设置方向键激活状态
    def setPushbuttonEnable(self, bool):
        self.pushButton.setEnabled(bool)
        self.pushButton_2.setEnabled(bool)
        self.pushButton_3.setEnabled(bool)
        self.pushButton_4.setEnabled(bool)

    def wheelEvent(self, event): # 滚轮事件
        zoomInFactor = 1.25
        zoomOutFactor = 1 / zoomInFactor
        oldPos = self.graphicsView.mapToScene(event.pos())
        if event.angleDelta().y() > 0:
            zoomFactor = zoomInFactor
        else:
            zoomFactor = zoomOutFactor
        self.graphicsView.scale(zoomFactor, zoomFactor)
        newPos = self.graphicsView.mapToScene(event.pos())
        delta = newPos - oldPos
        self.graphicsView.translate(delta.x(), delta.y())
        # 获取图片大小
        rect = self.graphicsView.scene().sceneRect()
        width = rect.width()
        height = rect.height()
        # 计算图片中心点
        center = QtCore.QPointF(width / 2, height / 2)
        # 将视图中心设置为图片中心点
        self.graphicsView.centerOn(center)

    def mousePressEvent(self, event):  # 鼠标按下事件
        global place, outfiles
        pos = event.pos()  # 返回鼠标所在点QPoint
        self.pos_label.setText("")
        print('Mouse is pressed at (%d,%d) of screen ' % (pos.x(), pos.y()))
        if 80 <= pos.x() <= 125 and 20 <= pos.y() <= 35:
            place = 1
            outfiles = 'data\\dongbeimen\\pano1.png'
            self.pix = QPixmap(outfiles)
            img_w = self.pix.width()
            img_h = self.pix.height()
            # 位置提示
            self.pos_label.setText("当前位置：东北门")
            print(outfiles)
            # 初始化图片位置
            self.panoramaShow()
            # 启动方向键控制
            self.setPushbuttonEnable(True)
        elif 195 <= pos.x() <= 235 and 205 <= pos.y() <= 230:
            place = 10
            outfiles = 'data\\jinghu\\pano1.png'
            self.pix = QPixmap(outfiles)
            img_w = self.pix.width()
            img_h = self.pix.height()
            # 位置提示
            self.pos_label.setText("当前位置：静湖")
            print(outfiles)
            # 初始化图片位置
            self.panoramaShow()
            # 启动方向键控制
            self.setPushbuttonEnable(True)
        elif 285 <= pos.x() <= 315 and 140 <= pos.y() <= 170:
            place = 7
            outfiles = 'data\\zhuxuan\\pano1.jpg'
            self.pix = QPixmap(outfiles)
            img_w = self.pix.width()
            img_h = self.pix.height()
            # 位置提示
            self.pos_label.setText("当前位置：竹轩")
            print(outfiles)
            # 初始化图片位置
            self.panoramaShow()
            # 启动方向键控制
            self.setPushbuttonEnable(True)
        elif 290 <= pos.x() <= 320 and 300 <= pos.y() <= 330:
            place = 6
            outfiles = 'data\\caochangA\\pano1.png'
            self.pix = QPixmap(outfiles)
            img_w = self.pix.width()
            img_h = self.pix.height()
            # 位置提示
            self.pos_label.setText("当前位置：外操场")
            print(outfiles)
            # 初始化图片位置
            self.panoramaShow()
            # 启动方向键控制
            self.setPushbuttonEnable(True)
        elif 360 <= pos.x() <= 375 and 350 <= pos.y() <= 365:
            place = 2
            outfiles = 'data\\tiyuguanA\\pano1.png'
            self.pix = QPixmap(outfiles)
            img_w = self.pix.width()
            img_h = self.pix.height()
            # 位置提示
            self.pos_label.setText("当前位置：体育馆内")
            print(outfiles)
            # 初始化图片位置
            self.panoramaShow()
            # 启动方向键控制
            self.setPushbuttonEnable(True)
        elif 340 <= pos.x() <= 360 and 330 <= pos.y() <= 350:
            place = 2
            outfiles = 'data\\tiyuguanB\\pano1.png'
            self.pix = QPixmap(outfiles)
            img_w = self.pix.width()
            img_h = self.pix.height()
            # 位置提示
            self.pos_label.setText("当前位置：体育馆外")
            print(outfiles)
            # 初始化图片位置
            self.panoramaShow()
            # 启动方向键控制
            self.setPushbuttonEnable(True)
        elif 265 <= pos.x() <= 290 and 340 <= pos.y() <= 365:
            place = 2
            outfiles = 'data\\caochangB\\pano1.png'
            self.pix = QPixmap(outfiles)
            img_w = self.pix.width()
            img_h = self.pix.height()
            # 位置提示
            self.pos_label.setText("当前位置：内操场")
            print(outfiles)
            # 初始化图片位置
            self.panoramaShow()
            # 启动方向键控制
            self.setPushbuttonEnable(True)
        elif 300 <= pos.x() <= 350 and 350 <= pos.y() <= 395:
            place = 2
            outfiles = 'data\\wanmei\\pano1.png'
            self.pix = QPixmap(outfiles)
            img_w = self.pix.width()
            img_h = self.pix.height()
            # 位置提示
            self.pos_label.setText("当前位置：丸美学生活动中心")
            print(outfiles)
            # 初始化图片位置
            self.panoramaShow()
            # 启动方向键控制
            self.setPushbuttonEnable(True)
        elif (450 + self.map_label.x()) <= pos.x() or pos.x() <=self.map_label.x() or (450 + self.map_label.y()) <= pos.y() or pos.y() <= self.map_label.y() :
            self.pos_label.setText("")
        else:
            self.pos_label.setText("当前位置：暂无全景图")

    def rightMove(self):
            self.graphicsView.horizontalScrollBar().setValue(self.graphicsView.horizontalScrollBar().value() + 300)

    def leftMove(self):
            self.graphicsView.horizontalScrollBar().setValue(self.graphicsView.horizontalScrollBar().value() - 300)

    def upMove(self):
            self.graphicsView.verticalScrollBar().setValue(self.graphicsView.verticalScrollBar().value() - 50)

    def downMove(self):
            self.graphicsView.verticalScrollBar().setValue(self.graphicsView.verticalScrollBar().value() + 50)

    # 过程展示1
    def showResult1(self):
        dialog_fault1 = QDialog()
        dialog_fault1.setGeometry(10, 10, 1019, 1037)
        gridLayout = QtWidgets.QGridLayout(dialog_fault1)
        gridLayout.setObjectName("gridLayout")
        label_3 = QtWidgets.QLabel(dialog_fault1)
        label_3.setStyleSheet("border-image:url(data/caochangA/10to11_source.png)")
        label_3.setObjectName("label_3")
        gridLayout.addWidget(label_3, 3, 0, 1, 2)
        label_5 = QtWidgets.QLabel(dialog_fault1)
        label_5.setStyleSheet("border-image:url(data/caochangA/10to11_warp.png)")
        label_5.setObjectName("label_5")
        gridLayout.addWidget(label_5, 1, 0, 1, 1)
        label_4 = QtWidgets.QLabel(dialog_fault1)
        label_4.setStyleSheet("border-image:url(data/caochangA/10to11_best.png)")
        label_4.setObjectName("label_4")
        gridLayout.addWidget(label_4, 4, 0, 1, 2)
        label_2 = QtWidgets.QLabel(dialog_fault1)
        label_2.setStyleSheet("border-image:url(data/caochangA/1-11.png)")
        label_2.setObjectName("label_2")
        gridLayout.addWidget(label_2, 0, 1, 1, 1)
        label_6 = QtWidgets.QLabel(dialog_fault1)
        label_6.setStyleSheet("border-image:url(data/caochangA/10to11_vis.png)")
        label_6.setObjectName("label_6")
        gridLayout.addWidget(label_6, 2, 0, 1, 2)
        label = QtWidgets.QLabel(dialog_fault1)
        label.setStyleSheet("border-image:url(data/caochangA/1-10.png)")
        label.setObjectName("label")
        gridLayout.addWidget(label, 0, 0, 1, 1)
        dialog_fault1.exec_()


    # 过程展示2
    def showResult2(self):
        dialog_fault2 = QDialog()
        dialog_fault2.setGeometry(10, 10, 2019, 837)
        gridLayout = QtWidgets.QGridLayout(dialog_fault2)
        gridLayout.setObjectName("gridLayout")
        label_3 = QtWidgets.QLabel(dialog_fault2)
        label_3.setStyleSheet("border-image:url(data/zhuxuan/pano.jpg)")
        label_3.setObjectName("label_3")
        gridLayout.addWidget(label_3, 0, 0, 1, 2)
        label_4 = QtWidgets.QLabel(dialog_fault2)
        label_4.setStyleSheet("border-image:url(data/zhuxuan/pano1.jpg)")
        label_4.setObjectName("label_4")
        gridLayout.addWidget(label_4, 1, 0, 1, 2)
        dialog_fault2.exec_()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()  # 创建窗体对象
    mainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
