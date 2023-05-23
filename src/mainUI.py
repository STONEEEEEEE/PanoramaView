from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem

from GUI import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # 窗口初始化
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)






        frame = QImage("..\\img\\zhuxuan.jpg")
        pix = QPixmap.fromImage(frame)
        item = QGraphicsPixmapItem(pix)
        scene = QGraphicsScene()
        scene.addItem(item)
        self.graphicsView.setScene(scene)
        self.graphicsView.show()



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()  # 创建窗体对象
    mainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
