class viceVote(QMainWindow):

    def __init__(self):
        super(viceVote, self).__init__()
        loadUi('votersVice.ui', self)
        self.vice1.setCheckable(True)
        self.vice2.setCheckable(True)
        self.vice3.setCheckable(True)
        self.vice4.setCheckable(True)
        self.vice1.clicked.connect(self.togglepres1)
        self.vice2.clicked.connect(self.togglepres2)
        self.vice3.clicked.connect(self.togglepres3)
        self.vice4.clicked.connect(self.togglepres4)
        self.backVice.clicked.connect(self.backButVice)
        self.nextVice.clicked.connect(self.nextButVice)

    def togglepres1(self):
        if self.vice1.isChecked():
            #self.pres1.setStyleSheet("background-color : lightblue")
            for statusBut in [self.vice2,self.vice3,self.vice4]:
                if statusBut.isChecked() == True:
                    statusBut.toggle()

    def togglepres2(self):
        if self.vice2.isChecked():
            for statusBut in [self.vice1, self.vice3, self.vice4]:
                if statusBut.isChecked() == True:
                    statusBut.toggle()
    def togglepres3(self):
        if self.vice3.isChecked():
            for statusBut in [self.vice1, self.vice2, self.vice4]:
                if statusBut.isChecked() == True:
                    statusBut.toggle()
    def togglepres4(self):
        if self.vice4.isChecked():
            for statusBut in [self.vice1, self.vice2, self.vice3]:
                if statusBut.isChecked() == True:
                    statusBut.toggle()

    def nextButVice(self):
        for statusBut in [self.vice1, self.vice2, self.vice3, self.vice4]:
            if statusBut.isChecked() == True:
                print(statusBut.text())
                pass # need storage
    def backButVice(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)