import AutoClick
from PyQt5.QtWidgets import QPushButton, qApp, QAction, QMainWindow, QComboBox, QLineEdit
from PyQt5.QtGui import QIcon


class main(QMainWindow):
    global click

    def __init__(self):
        super().__init__()
        self.load_data = 0
        self.load_data2 = 0
        self.login_btn = QPushButton('창켜', self)
        self.start_btn = QPushButton('시작', self)
        self.load_btn = QPushButton('불러오기', self)
        self.loadList_combobox = QComboBox(self)
        self.loadList2_combobox = QComboBox(self)
        self.load_txt = QLineEdit(self)
        self.initUI()

    def initUI(self):
        self.viewPrint()

    def viewPrint(self):
        # 메뉴 안에 끄기
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        # 상단 메뉴가 등장!?
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        # 버튼
        self.login_btn.move(15, 50)
        self.login_btn.resize(self.login_btn.sizeHint())
        self.login_btn.clicked.connect(self.startLogin)

        self.start_btn.move(200, 50)
        self.start_btn.resize(self.start_btn.sizeHint())
        self.start_btn.clicked.connect(self.startClick)

        self.load_btn.move(100, 50)
        self.load_btn.resize(self.load_btn.sizeHint())
        self.load_btn.clicked.connect(self.loadListClick)

        self.loadList_combobox.move(15, 100)
        self.loadList_combobox.setFixedWidth(300)
        self.loadList_combobox.currentIndexChanged.connect(self.currentIndexChanged)

        self.loadList2_combobox.move(15, 200)
        self.loadList2_combobox.setFixedWidth(300)
        self.loadList2_combobox.currentIndexChanged.connect(self.currentIndexChanged2)

        self.load_txt.move(15, 300)

        # 상태바
        self.statusBar()

        # 윈도우 생성
        self.setWindowTitle('start')
        self.setGeometry(500, 200, 500, 500)  # 가로위치, 세로위치, 가로길이, 세로길이
        self.show()

    def startLogin(self):
        global click
        click = AutoClick.AutoClick()
        click.login()

    def startClick(self):
        global click
        click.start_click(self.load_data, self.load_data2, self.load_txt.text())

    def loadListClick(self):
        global click
        try:
            self.loadList_combobox.clear()
            loadList = click.load_list()
            for l in loadList:
                self.loadList_combobox.addItem(l.text, l)

            self.loadList2_combobox.clear()
            sel_position_name = click.load_send_job()
            for n in sel_position_name:
                self.loadList2_combobox.addItem(n.text.strip(), n)

        except Exception as e:
            print(e)

    def currentIndexChanged(self, index):
        self.load_data = index

    def currentIndexChanged2(self, index):
        self.load_data2 = index