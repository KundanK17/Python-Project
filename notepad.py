from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # set initial path to None
        self.path = None
        # set properties for main window
        MainWindow.setWindowTitle('Untitled - Notepad')
        MainWindow.resize(500, 500)
        
        # create central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        
        # create grid layout
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        # create text editor
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        # set font to the editor
        font = QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont)
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        # create menu
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 501, 21))
        self.menuFile = QtWidgets.QMenu('File', self.menubar)
        self.menuEdit = QtWidgets.QMenu('Edit', self.menubar)
        MainWindow.setMenuBar(self.menubar)
        # create file menu options
        self.actionNew = QtWidgets.QAction('New', MainWindow)
        self.actionNew.setShortcut('Ctrl+N')
        self.actionNew.triggered.connect(self.new_file)
        self.actionOpen = QtWidgets.QAction('Open', MainWindow)
        self.actionOpen.setShortcut('Ctrl+O')
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave = QtWidgets.QAction('Save', MainWindow)
        self.actionSave.setShortcut('Ctrl+S')
        self.actionSave.triggered.connect(self.save_file) 
        self.actionSave_As = QtWidgets.QAction('Save As', MainWindow)
        self.actionSave_As.setShortcut('Ctrl+Shift+S')
        self.actionSave_As.triggered.connect(self.file_save_as)        
        self.actionExit = QtWidgets.QAction('Exit', MainWindow)
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.triggered.connect(self.exit)
        # create edit menu options
        self.actionUndo = QtWidgets.QAction('Undo', MainWindow)
        self.actionUndo.setShortcut('Ctrl+Z')
        self.actionUndo.triggered.connect(self.plainTextEdit.undo) 
        self.actionCut = QtWidgets.QAction('Cut', MainWindow)
        self.actionCut.setShortcut('Ctrl+X')
        self.actionCut.triggered.connect(self.plainTextEdit.cut)        
        self.actionCopy = QtWidgets.QAction('Copy', MainWindow)
        self.actionCopy.setShortcut('Ctrl+C')
        self.actionCopy.triggered.connect(self.plainTextEdit.copy)        
        self.actionPaste = QtWidgets.QAction('Paste', MainWindow)
        self.actionPaste.setShortcut('Ctrl+V')
        self.actionPaste.triggered.connect(self.plainTextEdit.paste)        
        self.actionSelect_All = QtWidgets.QAction('Select All', MainWindow)
        self.actionSelect_All.setShortcut('Ctrl+A')
        self.actionSelect_All.triggered.connect(self.plainTextEdit.selectAll)
        # add actions
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuEdit.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def new_file(self):
        MainWindow.setWindowTitle('Untitled - Notepad')
        self.plainTextEdit.clear()
    
    def open_file(self):
        global path
        # get text file path to open
        path, _ = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open File',
                                                        '', 'Text documents (*.txt)')
        if path=="":
            path = None
        else:
            self.path = path
            with open(path, 'r') as f:
                # read the file
                text = f.read()
                # set text
                self.plainTextEdit.setPlainText(text)
                # update the title
                self.update_title()
    def update_title(self): 
        # setting window title with file name
        MainWindow.setWindowTitle('%s - PyQt5 Notepad' %(os.path.basename(self.path)
                                                  if self.path else 'Untitled'))
    def save_file(self):
        global path
        if self.path is None:
            # call save as method
            self.file_save_as()
        else:
            # get the text
            text = self.plainTextEdit.toPlainText()
            # open file to write the text
            with open(path, 'w') as f:
                # write text in the file
                f.write(text)
    def file_save_as(self):
        path, _ = QtWidgets.QFileDialog.getSaveFileName(MainWindow, 'Save File', '',
                             'Text documents (*.txt)')
 
        if path=="":
            path = None
 
        else:
            self.path = path
            # get the text
            text = self.plainTextEdit.toPlainText()
     
            # opening file to write
            with open(path, 'w') as f:
                # write text in the file
                f.write(text)
            # update the title
            self.update_title()
    def exit(self):
        MainWindow.close()
              
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())