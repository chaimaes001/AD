# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 19:46:09 2021
@author: Chaimae
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys
import matplotlib.pyplot as plt
import cv2
import numpy as np
import time
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import ExtraTreeClassifier

#pretraitement des images
data=[]
data1=[]
def alphabet_learning():    
    for i in range(1,63): 
        image=plt.imread("apprentissage/"+str(i)+".png")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY )
        img=np.array(image)                
        img=img.flatten()                
        data.append(img)        
    return data
   
def alphabet_test():
    for i in range(1,42): 
        image=plt.imread("TEST/"+str(i)+".png")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY )
        img=np.array(image)
        img=img.flatten()                
        data1.append(img) 
    return data1 

images=alphabet_learning()
images_test=alphabet_test()

target=["A","A","A","A","A","B","B","B","C","C","D","D","E","E","E","F","F","G","G","H","H",
    "I","I","I","I","I","J","J","K","K","L","L","M","M","N","N","O","O","O","P", "P","Q","Q","R","R","S", "S",
    "T","T","U","U","U","V", "V","W","W","X","X","Y","Y","Z","Z"]
test=["A","A","B","B","C","C","D","D","E","E","F","F","G","H","H","I","I","J","J","K","L","M","M","N",
      "N","O","O","P","P","Q","R","S","S","T","U","U","V","W","X","Y","Z"]
#modèles des classifieurs et apprentissage      
clf=DecisionTreeClassifier(criterion="entropy",random_state=1,max_features=0.9,max_depth=5)
t1=time.time()
clf.fit(images,target)
t2=time.time()
t_clf=t2-t1

extra=ExtraTreeClassifier(criterion="entropy",random_state=1,max_features=0.9,splitter="best",max_depth=5)
te1=time.time()
extra.fit(images, target)
te2=time.time()
t_extra=te2-te1

#interface graphique
class Ui_page_test2(object):
    def setupUi(self, page_test2):
        page_test2.setObjectName("page_test2")
        page_test2.resize(707, 231)
        self.centralwidget = QtWidgets.QWidget(page_test2)
        self.centralwidget.setObjectName("centralwidget")
        self.label_titre = QtWidgets.QLabel(self.centralwidget)
        self.label_titre.setGeometry(QtCore.QRect(230, 20, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_titre.setFont(font)
        self.label_titre.setObjectName("label_titre")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 50, 91, 21))
        self.pushButton.setObjectName("pushButton")
        self.label_img = QtWidgets.QLabel(self.centralwidget)
        self.label_img.setGeometry(QtCore.QRect(100, 80, 50, 50))
        self.label_img.setText("")
        self.label_img.setObjectName("label_img")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(230, 100, 211, 21))
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        page_test2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(page_test2)
        self.statusbar.setObjectName("statusbar")
        page_test2.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(page_test2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 707, 21))
        self.menubar.setObjectName("menubar")
        self.menuAppretissage = QtWidgets.QMenu(self.menubar)
        self.menuAppretissage.setObjectName("menuAppretissage")
        self.menuTest = QtWidgets.QMenu(self.menubar)
        self.menuTest.setObjectName("menuTest")
        page_test2.setMenuBar(self.menubar)
        self.actionDecisionTreeClassifier = QtWidgets.QAction(page_test2)
        self.actionDecisionTreeClassifier.setObjectName("actionDecisionTreeClassifier")
        self.actionExtraTreeClassifier = QtWidgets.QAction(page_test2)
        self.actionExtraTreeClassifier.setObjectName("actionExtraTreeClassifier")
        self.actionApprenti=QtWidgets.QAction(first_page)
        self.actionApprenti.setObjectName("actionApprenti")
        self.menuTest.addAction(self.actionDecisionTreeClassifier)
        self.menuTest.addAction(self.actionExtraTreeClassifier)
        self.menuAppretissage.addAction(self.actionApprenti)
        self.menubar.addAction(self.menuAppretissage.menuAction())
        self.menubar.addAction(self.menuTest.menuAction())

        self.actionExtraTreeClassifier.triggered.connect(lambda:self.page_test1(page_test2))
        self.menuAppretissage.triggered.connect(lambda:self.main_page(page_test2))
        self.pushButton.clicked.connect(self.openPicture)
        
        self.retranslateUi(page_test2)
        QtCore.QMetaObject.connectSlotsByName(page_test2)

    def retranslateUi(self, page_test2):
        _translate = QtCore.QCoreApplication.translate
        page_test2.setWindowTitle(_translate("page_test2", "MainWindow"))
        self.label_titre.setText(_translate("page_test2", "Test : DecisionTreeClassifier"))
        self.pushButton.setText(_translate("page_test2", "choisir une image"))
        self.menuAppretissage.setTitle(_translate("page_test2", "Apprentissage"))
        self.menuTest.setTitle(_translate("page_test2", "Test"))
        self.actionDecisionTreeClassifier.setText(_translate("page_test2", "DecisionTreeClassifier"))
        self.actionExtraTreeClassifier.setText(_translate("page_test2", "ExtraTreeClassifier"))
        self.actionApprenti.setText(_translate("page_test2","Comparaison"))
        
    def page_test1(self,page_test2):
        page_test2.hide()
        self.page_test1 = QtWidgets.QMainWindow()
        self.ui = Ui_page_test1()
        self.ui.setupUi(self.page_test1)
        self.page_test1.show()
    
    def main_page(self,page_test2):
        page_test2.hide()
        self.first_page = QtWidgets.QMainWindow()
        self.ui = Ui_first_page()
        self.ui.setupUi(self.first_page)
        self.first_page.show()
    
    def openPicture(self):
        self.label_result.setText("")
        nom_image = QFileDialog.getOpenFileName()
        self.path = nom_image[0]
        path1 = self.path
        picture = QtGui.QPixmap(path1)
        picture1 = picture.scaled(50, 50, QtCore.Qt.KeepAspectRatio)
        self.label_img.setPixmap(QtGui.QPixmap(picture1))
        self.label_img.adjustSize()
        
        image=plt.imread(self.path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY )
        img=np.array(image) 
        self.label_result.setText("C'est la lettre : "+str(clf.predict([img.flatten()])[0]))

class Ui_page_test1(object):
    def setupUi(self, page_test1):
        page_test1.setObjectName("page_test1")
        page_test1.resize(707, 231)
        self.centralwidget = QtWidgets.QWidget(page_test1)
        self.centralwidget.setObjectName("centralwidget")
        self.label_titre = QtWidgets.QLabel(self.centralwidget)
        self.label_titre.setGeometry(QtCore.QRect(230, 20, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_titre.setFont(font)
        self.label_titre.setObjectName("label_titre")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 50, 91, 21))
        self.pushButton.setObjectName("pushButton")
        self.label_img = QtWidgets.QLabel(self.centralwidget)
        self.label_img.setGeometry(QtCore.QRect(100, 80, 50, 50))
        self.label_img.setText("")
        self.label_img.setObjectName("label_img")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(230, 100, 211, 21))
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        page_test1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(page_test1)
        self.statusbar.setObjectName("statusbar")
        page_test1.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(page_test1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 707, 21))
        self.menubar.setObjectName("menubar")
        self.menuAppretissage = QtWidgets.QMenu(self.menubar)
        self.menuAppretissage.setObjectName("menuAppretissage")
        self.menuTest = QtWidgets.QMenu(self.menubar)
        self.menuTest.setObjectName("menuTest")
        page_test1.setMenuBar(self.menubar)
        self.actionDecisionTreeClassifier = QtWidgets.QAction(page_test1)
        self.actionDecisionTreeClassifier.setObjectName("actionDecisionTreeClassifier")
        self.actionExtraTreeClassifier = QtWidgets.QAction(page_test1)
        self.actionExtraTreeClassifier.setObjectName("actionExtraTreeClassifier")
        self.menuTest.addAction(self.actionDecisionTreeClassifier)
        self.menuTest.addAction(self.actionExtraTreeClassifier)      
        self.actionApprenti=QtWidgets.QAction(first_page)
        self.actionApprenti.setObjectName("actionApprenti")
        self.menuAppretissage.addAction(self.actionApprenti)
        self.menubar.addAction(self.menuAppretissage.menuAction())
        self.menubar.addAction(self.menuTest.menuAction())

        self.actionDecisionTreeClassifier.triggered.connect(lambda:self.page_test2(page_test1))
        self.menuAppretissage.triggered.connect(lambda:self.main_page(page_test1))
        self.pushButton.clicked.connect(self.openPicture)
        
        self.retranslateUi(page_test1)
        QtCore.QMetaObject.connectSlotsByName(page_test1)

    def retranslateUi(self, page_test1):
        _translate = QtCore.QCoreApplication.translate
        page_test1.setWindowTitle(_translate("page_test1", "MainWindow"))
        self.label_titre.setText(_translate("page_test1", "Test : ExtraTreeClassifier"))
        self.pushButton.setText(_translate("page_test1", "choisir une image"))
        self.menuAppretissage.setTitle(_translate("page_test1", "Apprentissage"))
        self.menuTest.setTitle(_translate("page_test1", "Test"))
        self.actionDecisionTreeClassifier.setText(_translate("page_test1", "DecisionTreeClassifier"))
        self.actionExtraTreeClassifier.setText(_translate("page_test1", "ExtraTreeClassifier"))
        self.actionApprenti.setText(_translate("page_test2","Comparaison"))
    
    def page_test2(self,page_test1):
        page_test1.hide()
        self.page_test2 = QtWidgets.QMainWindow()
        self.ui = Ui_page_test2()
        self.ui.setupUi(self.page_test2)
        self.page_test2.show()
    
    def main_page(self,page_test1):
        page_test1.hide()
        self.first_page = QtWidgets.QMainWindow()
        self.ui = Ui_first_page()
        self.ui.setupUi(self.first_page)
        self.first_page.show()
        
    def openPicture(self):
        self.label_result.setText("")
        nom_image = QFileDialog.getOpenFileName()
        self.path = nom_image[0]
        path1 = self.path
        picture = QtGui.QPixmap(path1)
        picture1 = picture.scaled(50, 50, QtCore.Qt.KeepAspectRatio)
        self.label_img.setPixmap(QtGui.QPixmap(picture1))
        self.label_img.adjustSize()
        
        image=plt.imread(self.path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY )
        img=np.array(image) 
        self.label_result.setText("C'est la lettre : "+str(extra.predict([img.flatten()])[0]))

class Ui_first_page(object):
    def setupUi(self, first_page):
        first_page.setObjectName("first_page")
        first_page.resize(707, 231)
        self.centralwidget = QtWidgets.QWidget(first_page)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 80, 662, 85))
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(220)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(45)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 20, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        first_page.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(first_page)
        self.statusbar.setObjectName("statusbar")
        first_page.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(first_page)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 707, 21))
        self.menubar.setObjectName("menubar")
        self.menuAppretissage = QtWidgets.QMenu(self.menubar)
        self.menuAppretissage.setObjectName("menuAppretissage")
        self.menuTest = QtWidgets.QMenu(self.menubar)
        self.menuTest.setObjectName("menuTest")
        first_page.setMenuBar(self.menubar)
        self.actionDecisionTreeClassifier = QtWidgets.QAction(first_page)
        self.actionDecisionTreeClassifier.setObjectName("actionDecisionTreeClassifier")
        self.actionExtraTreeClassifier = QtWidgets.QAction(first_page)
        self.actionExtraTreeClassifier.setObjectName("actionExtraTreeClassifier")
        self.actionApprenti=QtWidgets.QAction(first_page)
        self.actionApprenti.setObjectName("actionApprenti")
        self.menuAppretissage.addAction(self.actionApprenti)
        self.menuTest.addAction(self.actionDecisionTreeClassifier)
        self.menuTest.addAction(self.actionExtraTreeClassifier)
        self.menubar.addAction(self.menuAppretissage.menuAction())
        self.menubar.addAction(self.menuTest.menuAction())

        self.actionDecisionTreeClassifier.triggered.connect(lambda:self.page_test2(first_page))
        self.actionExtraTreeClassifier.triggered.connect(lambda:self.page_test1(first_page))    
        
        self.retranslateUi(first_page)
        QtCore.QMetaObject.connectSlotsByName(first_page)

    def retranslateUi(self, first_page):
        _translate = QtCore.QCoreApplication.translate
        first_page.setWindowTitle(_translate("first_page", "MainWindow"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("first_page", "Classifieur"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("first_page", "Temps d\'éxecution"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("first_page", "Précision de la classification sur le test"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("first_page", "Decision TreeClassifier"))
        #ana hna
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("first_page",  str(t_clf)+" s"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("first_page", str(clf.score(images_test, test)*100)+"%"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("first_page", "ExtraTreeClassifier"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("first_page", str(t_clf)+" s"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("first_page", str(extra.score(images_test, test)*100)+"%"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("first_page", "Comparaison des arbres de décision"))
        self.menuAppretissage.setTitle(_translate("first_page", "Apprentissage"))
        self.menuTest.setTitle(_translate("first_page", "Test"))
        self.actionDecisionTreeClassifier.setText(_translate("first_page", "DecisionTreeClassifier"))
        self.actionExtraTreeClassifier.setText(_translate("first_page", "ExtraTreeClassifier"))
        self.actionApprenti.setText(_translate("page_test2","Comparaison"))

    def page_test1(self,first_page): 
        first_page.hide()
        self.page_test1 = QtWidgets.QMainWindow()
        self.ui = Ui_page_test1()
        self.ui.setupUi(self.page_test1)
        self.page_test1.show()
    
    def page_test2(self,first_page):
        first_page.hide()
        self.page_test2 = QtWidgets.QMainWindow()
        self.ui = Ui_page_test2()
        self.ui.setupUi(self.page_test2)
        self.page_test2.show()
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    first_page = QtWidgets.QMainWindow()
    ui = Ui_first_page()
    ui.setupUi(first_page)
    first_page.show()
    sys.exit(app.exec_())
