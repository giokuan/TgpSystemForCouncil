
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import mysql.connector as mc
import pymysql
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QVBoxLayout, QHBoxLayout, QHeaderView,QTableWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class Ui_mainForm(object):

    def messageBox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setIcon(QMessageBox.Information)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()


    def popup(self):
        msg=QMessageBox() 
        msg.setWindowTitle("Exit")
        msg.setText("Are you sure you wan't to Exit?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Ok| QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        
        res = msg.exec_()
        if res == QMessageBox.Ok:  
            sys.exit()
        if res == QMessageBox.Cancel:
            pass
        

    def insert_data(self):
        lname=self.lname_edit.text()
        fname=self.fname_edit.text()
        aka1=self.aka_edit.text()
        batch=self.batchname_edit.text()
        tbirth=self.tbirth_edit.text()
        current=self.current_edit.text()
        root=self.root_edit.text()
        status=self.status_edit.text()
        address=self.address_edit.text()

        self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="myproject3")
       
        query=("INSERT INTO projecttau3 (last_name, first_name, aka, batch_name, T_birth, current_chapter, root_chapter, stat, address) VALUES  (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        cur=self.conn.cursor()
        data= cur.execute(query, (lname.upper(),fname.upper(),aka1.upper(),batch.upper(),tbirth.upper(),current.upper(),root.upper(),status.upper(),address.upper()))
        

        if (data):
            msg=QMessageBox()
            if    len(lname) == 0:
                self.messageBox("Information", " Last Name Cannot be empty!")
                return
            elif  len(fname) == 0:
                self.messageBox("Information", " First Name Cannot be empty!")
                return
            elif  len(aka1)  == 0:
                self.messageBox("Information", " A.K.A Cannot be empty!")
                return
            elif  len(batch) == 0:
                self.messageBox("Information", " Batch Name Cannot be empty!")
                return
            elif  len(tbirth)== 0:
                self.messageBox("Information", " Triskelion Birth Cannot be empty!")
                return
            elif  len(current)== 0:
                self.messageBox("Information", " Current Chapter Cannot be empty!")
                return
            elif  len(root)== 0:
                self.messageBox("Information", " Root Chapter Cannot be empty!")
                return
            elif  len(status)== 0:
                self.messageBox("Information", " Status Cannot be empty!")
                return
            elif  len(address) == 0:
                self.messageBox("Information", " Address Cannot be empty!")
                return
                

            else:
                self.messageBox("Saved", " Member Data Saved")
                self.conn.commit()
                self.Savebutton.setEnabled(False)
                self.addbuttom.setEnabled(True)
                self.cancel()
                self.loadData()
            
            

    def update(self):
        
        mem_id=self.id_edit.text()
        lname=self.lname_edit.text()
        fname=self.fname_edit.text()
        aka1=self.aka_edit.text()
        batch=self.batchname_edit.text()
        tbirth=self.tbirth_edit.text()
        current=self.current_edit.text()
        root=self.root_edit.text()
        status=self.status_edit.text()
        address=self.address_edit.text()
        
        self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="myproject3")
        cur=self.conn.cursor()

        sql = "UPDATE projecttau3 SET last_name = '"+ lname.upper() +"', first_name= '" + fname.upper() + "', aka = '" + aka1.upper() + "', batch_name= '" + batch.upper()\
                 + "', T_birth = '" + tbirth.upper() + "', current_chapter = '" + current.upper()+ "', root_chapter = '" + root.upper() + "', stat = '" + status.upper() + "', address = '"\
                  + address.upper() + "' WHERE member_id = '"+mem_id+"' "
        
        if (sql):
            msg=QMessageBox()
            if    len(lname) == 0:
                self.messageBox("Information", " Last Name Cannot be empty!")
                return
            elif  len(fname) == 0:
                self.messageBox("Information", " First Name Cannot be empty!")
                return
            elif  len(aka1)  == 0:
                self.messageBox("Information", " A.K.A Cannot be empty!")
                return
            elif  len(batch) == 0:
                self.messageBox("Information", " Batch Name Cannot be empty!")
                return
            elif  len(tbirth)== 0:
                self.messageBox("Information", " Triskelion Birth Cannot be empty!")
                return
            elif  len(current)== 0:
                self.messageBox("Information", " Current Chapter Cannot be empty!")
                return
            elif  len(root)== 0:
                self.messageBox("Information", " Root Chapter Cannot be empty!")
                return
            elif  len(status)== 0:
                self.messageBox("Information", " Status Cannot be empty!")
                return
            elif  len(address) == 0:
                self.messageBox("Information", " Address Cannot be empty!")
                return
                

            else:
                cur.execute(sql)
                self.messageBox("Updated", " Member Data Updated")
                self.conn.commit()
                self.loadData()
                self.cancel()
                self.hide_button2()

    def cell_click(self,columnCount,rowCount):
        self.cancel()
        self.editbutton.setEnabled(True)
        self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="myproject3")
        cur=self.conn.cursor()
        item = self.tableWidget.selectedItems()
        i = (item[0].text())
        if rowCount != (0):
            return

        else:
            cur.execute ("SELECT * from projecttau3 WHERE member_id=" +str(i))
            col = cur.fetchone()
            #print (row)           
            lname = col[1]
            fname = col[2]
            aka1 = col[3]
            batch = col [4]
            tbirth = col[5]
            current = col[6]
            root = col[7]
            status = col[8]
            add = col[9]

        self.id_edit.setText(i)
        self.lname_edit.setText(lname)
        self.fname_edit.setText(fname)
        self.aka_edit.setText(aka1)
        self.batchname_edit.setText(batch)
        self.tbirth_edit.setText(tbirth)
        self.current_edit.setText(current)
        self.root_edit.setText(root)
        self.status_edit.setText(status)
        self.address_edit.setText(add)
        
    
    def loadData(self):
        self.searchEdit.clear()
        self.search_chapter.clear()
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels(['Member ID', ' Last Name', 'Firs Name', 'A.K.A','Batch Name', 'T-Birth','Current Chapter','Root Chapter', 'Status', 'Address'])
        
        row = 0
        try: 
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password= "noahkuan03",
                database = "myproject3"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM projecttau3 ORDER BY last_name ASC" )
            result = mycursor.fetchall()
            
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                  
        except mc.Error as e:
            print ("Error Occured")
           

    def search(self):    
        row = 0
        try: 
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password= "noahkuan03",
                database = "myproject3"
            )
            mycursor = mydb.cursor()
            se = self.searchEdit.text()
            sc= self.search_chapter.text()
            mycursor.execute("SELECT * FROM projecttau3 WHERE last_name = '"+se+"' OR current_chapter = '"+sc+"'");
            result = mycursor.fetchall()
          
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                  
        except mc.Error as e:
            print ("Error Occured")


    def specific_search(self):
        row = 0
       
        mydb = mc.connect(
            host = "localhost",
            user = "root",
            password= "noahkuan03",
            database = "myproject3"
        )
        mycursor = mydb.cursor()
        se = self.searchEdit.text()
        sc= self.search_chapter.text()
        mycursor.execute("SELECT * FROM projecttau3 WHERE last_name = '"+se+"' AND current_chapter = '"+sc+"'");
        result = mycursor.fetchall()
        if len(se) == 0 or len(sc) == 0:
            self.messageBox("Information", " Last Name or Chapter Field  Cannot be empty!")

        else:
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                  
       


    def add_new_button(self):
        self.lname_edit.setEnabled(True)
        self.fname_edit.setEnabled(True)
        self.current_edit.setEnabled(True)
        self.status_edit.setEnabled(True)
        self.batchname_edit.setEnabled(True)
        self.address_edit.setEnabled(True)
        self.aka_edit.setEnabled(True)
        self.root_edit.setEnabled(True)
        self.tbirth_edit.setEnabled(True)
        self.addbuttom.setEnabled(False)
        self.clear.setEnabled(True)
        self.Savebutton.setEnabled(True)
    
    def clearfield(self):    
        self.lname_edit.clear()
        self.fname_edit.clear()
        self.current_edit.clear()
        self.status_edit.clear()
        self.batchname_edit.clear()
        self.address_edit.clear()
        self.address_edit.clear()
        self.aka_edit.clear()
        self.root_edit.clear()
        self.tbirth_edit.clear()
        self.id_edit.clear()
        self.editbutton.setEnabled(False)
        

    def cancel(self):
        self.lname_edit.setEnabled(False) 
        self.fname_edit.setEnabled(False)
        self.current_edit.setEnabled(False)
        self.status_edit.setEnabled(False)
        self.batchname_edit.setEnabled(False)
        self.address_edit.setEnabled(False)
        self.aka_edit.setEnabled(False)
        self.root_edit.setEnabled(False)
        self.tbirth_edit.setEnabled(False)
        self.clearfield()
        self.editbutton.setEnabled(False)
        self.addbuttom.setEnabled(True)
        self.clear.setEnabled(False)
        self.Savebutton.setEnabled(False)


    def hide_button(self):
        self.Savebutton.hide()
        self.update_button.show()


    def hide_button2(self):
        self.Savebutton.show()
        self.update_button.hide()


    def close(self):
        self.popup()

    
    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.resize(1058, 638)
        mainForm.setAcceptDrops(False)
        #icon = QtGui.QIcon.fromTheme("fv")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("form_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainForm.setWindowIcon(icon)
        mainForm.setAccessibleName("")
        self.centralwidget = QtWidgets.QWidget(mainForm)
        self.centralwidget.setObjectName("centralwidget")


        #SEARCH TEXTBOX
        self.searchEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchEdit.setGeometry(QtCore.QRect(598, 40, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchEdit.setFont(font)
        self.searchEdit.setObjectName("searchEdit")

        #SEARCH CHAPTER
        self.search_chapter = QtWidgets.QLineEdit(self.centralwidget)
        self.search_chapter.setGeometry(QtCore.QRect(823, 40, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_chapter.setFont(font)
        self.search_chapter.setObjectName("search_chapter")


        #MEMBER ID TEXTBOX
        self.id_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.id_edit.setEnabled(False)
        self.id_edit.setGeometry(QtCore.QRect(150, 40, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.id_edit.setFont(font)
        self.id_edit.setObjectName("id_edit")


        #LAST NAME TEXTBOX
        self.lname_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.lname_edit.setEnabled(False)
        self.lname_edit.setGeometry(QtCore.QRect(150, 80, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lname_edit.setFont(font)
        self.lname_edit.setObjectName("lname_edit")
        self.lname_edit.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        

        #FIRST NAME TEXTBOX
        self.fname_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.fname_edit.setEnabled(False)
        self.fname_edit.setGeometry(QtCore.QRect(150, 120, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fname_edit.setFont(font)
        self.fname_edit.setObjectName("fname_edit")


        #AKA TEXTBOX
        self.aka_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.aka_edit.setEnabled(False)
        self.aka_edit.setGeometry(QtCore.QRect(150, 160, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.aka_edit.setFont(font)
        self.aka_edit.setObjectName("aka_edit")


        #BATCH NAME TEXTBOX
        self.batchname_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.batchname_edit.setEnabled(False)
        self.batchname_edit.setGeometry(QtCore.QRect(150, 200, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.batchname_edit.setFont(font)
        self.batchname_edit.setObjectName("batchname_edit")


        #TBIRTH TEXTBOX
        self.tbirth_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.tbirth_edit.setEnabled(False)
        self.tbirth_edit.setGeometry(QtCore.QRect(150, 240, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tbirth_edit.setFont(font)
        self.tbirth_edit.setObjectName("tbirth_edit")


        #CURRENT CHAPTER TEXTBOX
        self.current_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.current_edit.setEnabled(False)
        self.current_edit.setGeometry(QtCore.QRect(150, 280, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.current_edit.setFont(font)
        self.current_edit.setObjectName("current_edit")


        #ROOT CHAPTER TEXTBOX
        self.root_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.root_edit.setEnabled(False)
        self.root_edit.setGeometry(QtCore.QRect(150, 320, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.root_edit.setFont(font)
        self.root_edit.setObjectName("root_edit")


        #STATUS TEXTBOX
        self.status_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.status_edit.setEnabled(False)
        self.status_edit.setGeometry(QtCore.QRect(150, 360, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.status_edit.setFont(font)
        self.status_edit.setObjectName("status_edit")


        #ADDRESS TEXTBOX
        self.address_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.address_edit.setEnabled(False)
        self.address_edit.setGeometry(QtCore.QRect(150, 400, 884, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.address_edit.setFont(font)
        self.address_edit.setObjectName("address_edit")

        
        #TABLE
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(330, 80, 705, 311))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(100)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.cellClicked.connect(self.cell_click)
        self.loadData()
        

        #MEMBER ID LABEL
        self.id_label = QtWidgets.QLabel(self.centralwidget)
        self.id_label.setGeometry(QtCore.QRect(40, 40, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.id_label.setFont(font)
        self.id_label.setObjectName("id_label")

        
        #LAST NAME LABEL
        self.lname_label = QtWidgets.QLabel(self.centralwidget)
        self.lname_label.setGeometry(QtCore.QRect(40, 80, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lname_label.setFont(font)
        self.lname_label.setObjectName("lname_label")

        
        #FIRST NAME LABEL
        self.fname_label = QtWidgets.QLabel(self.centralwidget)
        self.fname_label.setGeometry(QtCore.QRect(40, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.fname_label.setFont(font)
        self.fname_label.setObjectName("fname_label")


        #AKA LABEL
        self.aka_label = QtWidgets.QLabel(self.centralwidget)
        self.aka_label.setGeometry(QtCore.QRect(40, 160, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.aka_label.setFont(font)
        self.aka_label.setObjectName("aka_label")


        #BATCH NAME LABEL
        self.batch_label = QtWidgets.QLabel(self.centralwidget)
        self.batch_label.setGeometry(QtCore.QRect(40, 200, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.batch_label.setFont(font)
        self.batch_label.setObjectName("batch_label")


        #TBIRTH LABEL
        self.tbirth_label = QtWidgets.QLabel(self.centralwidget)
        self.tbirth_label.setGeometry(QtCore.QRect(40, 240, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tbirth_label.setFont(font)
        self.tbirth_label.setObjectName("tbirth_label")


        #CURRENT CHAPTER LABEL
        self.current_label = QtWidgets.QLabel(self.centralwidget)
        self.current_label.setGeometry(QtCore.QRect(40, 280, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.current_label.setFont(font)
        self.current_label.setObjectName("current_label")


        #ROOT CHAPTER LABEL
        self.root_label = QtWidgets.QLabel(self.centralwidget)
        self.root_label.setGeometry(QtCore.QRect(40, 320, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.root_label.setFont(font)
        self.root_label.setObjectName("root_label")


        #STATUS LABEL
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(40, 360, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.status_label.setFont(font)
        self.status_label.setObjectName("status_label")


        #ADDRESS LABEL
        self.addres_label = QtWidgets.QLabel(self.centralwidget)
        self.addres_label.setGeometry(QtCore.QRect(40, 400, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.addres_label.setFont(font)
        self.addres_label.setObjectName("addres_label")

        
        #ADD BUTTON
        self.addbuttom = QtWidgets.QPushButton(self.centralwidget)
        self.addbuttom.setGeometry(QtCore.QRect(150, 460, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.addbuttom.setFont(font)
        self.addbuttom.setObjectName("addbuttom")
        self.addbuttom.clicked.connect(self.add_new_button)
        self.addbuttom.clicked.connect(self.clearfield)


        #SAVE BUTTON
        self.Savebutton = QtWidgets.QPushButton(self.centralwidget)
        self.Savebutton.setGeometry(QtCore.QRect(300, 460, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Savebutton.setFont(font)
        self.Savebutton.setObjectName("Savebutton")
        self.Savebutton.setEnabled(False)
        self.Savebutton.clicked.connect(self.insert_data)


        #UPDATE BUTTON
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setGeometry(QtCore.QRect(300, 460, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.update_button.setFont(font)
        self.update_button.setObjectName("updatebutton")
        self.update_button.setEnabled(True)
        self.update_button.clicked.connect(self.update)
        self.update_button.hide()


        #CANCEL BUTTON
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(450, 460, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.clear.clicked.connect(self.cancel)
        self.clear.setEnabled(False)
        self.clear.clicked.connect(self.hide_button2)
        

        #EDIT BUTTON
        self.editbutton = QtWidgets.QPushButton(self.centralwidget)
        self.editbutton.setGeometry(QtCore.QRect(600, 460, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.editbutton.setFont(font)
        self.editbutton.setObjectName("editbutton")
        self.editbutton.clicked.connect(self.add_new_button)
        self.editbutton.clicked.connect(self.hide_button)
        self.editbutton.setEnabled(False)
        

        #REFRESH BUTTON
        self.refreshbutton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshbutton.setGeometry(QtCore.QRect(747, 460, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.refreshbutton.setFont(font)
        self.refreshbutton.setObjectName("refreshbutton")
        self.refreshbutton.clicked.connect(self.loadData)
        self.refreshbutton.clicked.connect(self.cancel)
        self.refreshbutton.clicked.connect(self.hide_button2)

        
        #EXIT BUTTON
        self.exitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.exitbutton.setGeometry(QtCore.QRect(895, 460, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exitbutton.setFont(font)
        self.exitbutton.setObjectName("exitbutton")
        self.exitbutton.clicked.connect(self.close)


        #TIPAZ LOGO
        self.label_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_pic.setGeometry(QtCore.QRect(370, 490, 521, 181))
        self.label_pic.setText("")
        self.label_pic.setPixmap(QtGui.QPixmap("and3.png"))
        self.label_pic.setObjectName("label")


        #SEARCH BUTTON
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(465, 40, 121, 33))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(self.search)

        #SPECIFIC SEARCH BUTTON
        self.search_specific = QtWidgets.QPushButton(self.centralwidget)
        self.search_specific.setGeometry(QtCore.QRect(330, 40, 121, 33))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_specific.setFont(font)
        self.search_specific.setObjectName("searchButton")
        self.search_specific.clicked.connect(self.specific_search)

        
        mainForm.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainForm)
        self.statusbar.setObjectName("statusbar")
        mainForm.setStatusBar(self.statusbar)


        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)
    

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate("mainForm", "TAU GAMMA PHI TRISKELION GRAND FRATERNITY FOR COUNCIL"))
        self.status_label.setText(_translate("mainForm", "Status"))
        self.addres_label.setText(_translate("mainForm", "Address"))
        self.batch_label.setText(_translate("mainForm", "Batch Name"))
        self.clear.setText(_translate("mainForm", "Cancel"))
        self.editbutton.setText(_translate("mainForm", "Edit"))
        self.aka_label.setText(_translate("mainForm", "A.K.A"))
        self.root_label.setText(_translate("mainForm", "Root Chapter"))
        self.refreshbutton.setText(_translate("mainForm", "Refresh"))
        self.exitbutton.setText(_translate("mainForm", "Exit"))
        self.Savebutton.setText(_translate("mainForm", "Save"))
        self.searchButton.setText(_translate("mainForm", "Search"))
        self.search_specific.setText(_translate("mainForm", "Search Specific"))
        self.tbirth_label.setText(_translate("mainForm", "T-Birth"))
        self.current_label.setText(_translate("mainForm", "Current Chapter"))
        self.lname_label.setText(_translate("mainForm", "Last Name"))
        self.fname_label.setText(_translate("mainForm", "First Name"))
        self.id_label.setText(_translate("mainForm", "Member ID"))
        self.addbuttom.setText(_translate("mainForm", "Add New"))
        self.update_button.setText(_translate("mainForm", "Update"))
        self.tbirth_edit.setPlaceholderText(_translate("MainWindow", "MM/DD/YYYY"))
        self.searchEdit.setPlaceholderText(_translate("MainWindow", "Enter Last Name"))
        self.search_chapter.setPlaceholderText(_translate("MainWindow", "Enter Chapter"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainForm = QtWidgets.QMainWindow()
    ui = Ui_mainForm()
    ui.setupUi(mainForm)
    mainForm.show()
    sys.exit(app.exec_())
