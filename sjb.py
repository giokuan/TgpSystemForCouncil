from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
import mysql.connector as mc
import pymysql
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QVBoxLayout, QHBoxLayout, QHeaderView,QTableWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox,QFileDialog
import sys


class Ui_MainWindow(object):

    def messageBox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setStyleSheet('QMessageBox {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255)); color: white;}\
            QPushButton{color: white; font-size: 16px; background-color: rgb(75,75,75);\
            border-radius: 5px; padding: 10px; text-align: center;} QPushButton:hover{color: rgb(0, 170, 127);}')
        mess.setWindowIcon(QtGui.QIcon('logo/ico_logo.ico'))
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setIcon(QMessageBox.Information)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_() 

    def exit_app(self):
        msg=QMessageBox()
        msg.setStyleSheet('QMessageBox {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255)); color: white;}\
            QPushButton{color: white; font-size: 16px; background-color: rgb(75,75,75); \
            border-radius: 5px; padding: 10px; text-align: center;}QPushButton:hover{color: rgb(0, 170, 127);}') 
        msg.setWindowIcon(QtGui.QIcon('logo/ico_logo.ico'))
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

    def browse_image(self):
        filename = QFileDialog.getOpenFileName( caption = "Open file", directory=None, filter="Image (*.png * .jpg);;All Files(*.*)")   
        self.addPic_edit.setText(filename[0])
        self.load_image()

    def load_image(self):
        p = self.addPic_edit.text()
        self.picture_label.setPixmap(QtGui.QPixmap(p)) 

    def default(self):
        self.addPic_edit.setText("logo/Men.png")
        self.picture_label.setPixmap(QtGui.QPixmap("logo/Men.png")) 
        pass
        

    def insert_data(self):
        p = self.addPic_edit.text()
        if len(p) == 0:
            self.messageBox("Add Photo","You have no photo selected, \n Default Photo will be use!")
            self.default()
        else:
            
        
            with open(p, 'rb') as f:
                m=f.read()

            lname=self.lname_edit.text()
            fname=self.fname_edit.text()
            aka1=self.aka_edit.text()
            batch=self.batch_edit.text()
            tbirth=self.tbirth_edit.text()
            current=self.current_edit.text()
            root=self.root_edit.text()
            status=self.status_edit.text()
            address=self.address_edit.text()

            self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="myproject3")
       
            query=("INSERT INTO projecttau3 (last_name, first_name, aka, batch_name, T_birth, current_chapter, root_chapter, stat, address,photo) VALUES  (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)")
            cur=self.conn.cursor()
            data= cur.execute(query, (lname.upper(),fname.upper(),aka1.upper(),batch.upper(),tbirth.upper(),current.upper(),root.upper(),status.upper(),address.upper(),m))
        

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
                    self.messageBox("Tau Gamma Phi", " Member Data Saved")
                    self.conn.commit()
                    #self.Savebutton.setEnabled(False)
                    #self.addbuttom.setEnabled(True)
                    self.cancel()
                    self.loadData()

    def cell_click_disabledTextbox(self):
        self.add_btn.setEnabled(True)
        self.save_btn.setEnabled(False)
        self.cancel_btn.setEnabled(False)
        self.refresh_btn.setEnabled(True)
        self.edit_btn.setEnabled(True)
        self.update_btn.hide()
        self.save_btn.show()

        self.lname_edit.setEnabled(False)
        self.fname_edit.setEnabled(False)
        self.aka_edit.setEnabled(False)
        self.batch_edit.setEnabled(False)
        self.tbirth_edit.setEnabled(False)
        self.current_edit.setEnabled(False)
        self.root_edit.setEnabled(False)
        self.status_edit.setEnabled(False)
        self.address_edit.setEnabled(False)

        self.lname_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.fname_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.aka_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.batch_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.tbirth_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.current_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.root_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.status_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.address_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")



    def cell_click(self,columnCount,rowCount):

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
            pic = col[10]

        self.id_edit.setText(i)
        self.lname_edit.setText(lname)
        self.fname_edit.setText(fname)
        self.aka_edit.setText(aka1)
        self.batch_edit.setText(batch)
        self.tbirth_edit.setText(tbirth)
        self.current_edit.setText(current)
        self.root_edit.setText(root)
        self.status_edit.setText(status)
        self.address_edit.setText(add)
        self.cell_click_disabledTextbox()

        with open('logo/pic.png', 'wb') as f:
                f.write(pic)
                self.addPic_edit.setText('logo/pic.png')
                self.picture_label.setPixmap(QtGui.QPixmap("logo/pic.png"))


        
    def loadData(self):
        
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

    def update(self):
        p = self.addPic_edit.text() 
        with open(p, 'rb') as f:
            m=f.read()
        
        mem_id=self.id_edit.text()
        lname=self.lname_edit.text()
        fname=self.fname_edit.text()
        aka1=self.aka_edit.text()
        batch=self.batch_edit.text()
        tbirth=self.tbirth_edit.text()
        current=self.current_edit.text()
        root=self.root_edit.text()
        status=self.status_edit.text()
        address=self.address_edit.text()
        
        self.conn=pymysql.connect(host="localhost", user="root", password="noahkuan03", db="myproject3")
        cur=self.conn.cursor()

        sql = "UPDATE projecttau3 SET last_name = '"+ lname.upper() +"', first_name= '" + fname.upper() + "', aka = '" + aka1.upper() + "', batch_name= '" + batch.upper()\
                 + "', T_birth = '" + tbirth.upper() + "', current_chapter = '" + current.upper()+ "', root_chapter = '" + root.upper() + "', stat = '" + status.upper() + "', address = '"\
                  + address.upper() + "', photo= %s WHERE member_id = '"+mem_id+"' "
        
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
                cur.execute(sql,m)
                self.messageBox("Tau Gamma Phi", " Member Data Updated")
                self.conn.commit()
                self.loadData()
                self.cell_click_disabledTextbox()

                #self.cancel()


    def add(self):
        self.lname_edit.setEnabled(True)
        self.fname_edit.setEnabled(True)
        self.aka_edit.setEnabled(True)
        self.batch_edit.setEnabled(True)
        self.tbirth_edit.setEnabled(True)
        self.current_edit.setEnabled(True)
        self.root_edit.setEnabled(True)
        self.status_edit.setEnabled(True)
        self.address_edit.setEnabled(True)

        self.edit_btn.setEnabled(False)
        self.add_btn.setEnabled(False)
        self.save_btn.setEnabled(True)
        self.cancel_btn.setEnabled(True)
        self.refresh_btn.setEnabled(False)
        self.camera_btn.setEnabled(True)

        self.lname_edit.clear()
        self.fname_edit.clear()
        self.aka_edit.clear()
        self.batch_edit.clear()
        self.tbirth_edit.clear()
        self.current_edit.clear()
        self.root_edit.clear()
        self.status_edit.clear()
        self.address_edit.clear()
        self.id_edit.clear()
        self.search_edit.clear()
        self.default()

        self.lname_edit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.fname_edit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.aka_edit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.batch_edit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.tbirth_edit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.current_edit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.root_edit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.status_edit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
        self.address_edit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
    
    def cancel(self):
        self.lname_edit.setEnabled(False)
        self.fname_edit.setEnabled(False)
        self.aka_edit.setEnabled(False)
        self.batch_edit.setEnabled(False)
        self.tbirth_edit.setEnabled(False)
        self.current_edit.setEnabled(False)
        self.root_edit.setEnabled(False)
        self.status_edit.setEnabled(False)
        self.address_edit.setEnabled(False)

        self.edit_btn.setEnabled(True)
        self.add_btn.setEnabled(True)
        self.save_btn.setEnabled(False)
        self.save_btn.show()
        self.update_btn.hide()
        self.cancel_btn.setEnabled(False)
        self.refresh_btn.setEnabled(True)
        self.edit_btn.setEnabled(True)
        self.camera_btn.setEnabled(False)

        self.lname_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.fname_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.aka_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.batch_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.tbirth_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.current_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.root_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.status_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.address_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")

        self.lname_edit.clear()
        self.fname_edit.clear()
        self.aka_edit.clear()
        self.batch_edit.clear()
        self.tbirth_edit.clear()
        self.current_edit.clear()
        self.root_edit.clear()
        self.status_edit.clear()
        self.address_edit.clear()
        self.id_edit.clear()
        self.default()

        
    def refresh(self):

        self.id_edit.clear()
        self.lname_edit.clear()
        self.fname_edit.clear()
        self.aka_edit.clear()
        self.batch_edit.clear()
        self.tbirth_edit.clear()
        self.current_edit.clear()
        self.root_edit.clear()
        self.status_edit.clear()
        self.address_edit.clear()

        self.lname_edit.setEnabled(False)
        self.fname_edit.setEnabled(False)
        self.aka_edit.setEnabled(False)
        self.batch_edit.setEnabled(False)
        self.tbirth_edit.setEnabled(False)
        self.current_edit.setEnabled(False)
        self.root_edit.setEnabled(False)
        self.status_edit.setEnabled(False)
        self.address_edit.setEnabled(False)

        self.edit_btn.setEnabled(True)
        self.add_btn.setEnabled(True)
        self.save_btn.setEnabled(False)
        self.cancel_btn.setEnabled(False)
        self.refresh_btn.setEnabled(True)
        self.default()

        self.lname_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.fname_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.aka_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.batch_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.tbirth_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.current_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.root_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.status_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.address_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.loadData()

    def edit(self):
        mem_id = self.id_edit.text()
        if len(mem_id) == 0:
            self.messageBox("Tau Gamma Phi", "No Data Found")
            return
        else:
            self.lname_edit.setEnabled(True)
            self.fname_edit.setEnabled(True)
            self.aka_edit.setEnabled(True)
            self.batch_edit.setEnabled(True)
            self.tbirth_edit.setEnabled(True)
            self.current_edit.setEnabled(True)
            self.root_edit.setEnabled(True)
            self.status_edit.setEnabled(True)
            self.address_edit.setEnabled(True)

            self.cancel_btn.setEnabled(True)
            self.add_btn.setEnabled(False)
            self.refresh_btn.setEnabled(False)
            self.edit_btn.setEnabled(False)
            self.camera_btn.setEnabled(True)
            self.update_btn.show()
            self.save_btn.hide()

            self.lname_edit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
            self.fname_edit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
            self.aka_edit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
            self.batch_edit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
            self.tbirth_edit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
            self.current_edit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
            self.root_edit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
            self.status_edit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")
            self.address_edit.setStyleSheet("background-color: rgb(24, 24, 24);color: rgb(6, 254, 192)")

    def search_radio(self):
        self.search_btn.show()
        self.search_edit.show()
        self.advance_search_btn.hide()
        self.search_lname_edit.hide()
        self.search_fname_edit.hide()
        self.search_lname_edit.clear()
        self.search_fname_edit.clear()

    def advance_radio(self):
        self.search_btn.hide()
        self.search_edit.hide()
        self.advance_search_btn.show()
        self.search_lname_edit.show()
        self.search_fname_edit.show()
        self.search_edit.clear()

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
            lname = self.search_edit.text()
            
            mycursor.execute("SELECT * FROM projecttau3 WHERE last_name = '"+lname+"' OR current_chapter = '"+lname+"'");
            result = mycursor.fetchall()
          
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                  
        except mc.Error as e:
            print ("Error Occured")

    
    def advance_search(self):
        row = 0
       
        mydb = mc.connect(
            host = "localhost",
            user = "root",
            password= "noahkuan03",
            database = "myproject3"
        )
        mycursor = mydb.cursor()
        lname = self.search_lname_edit.text()
        fname= self.search_fname_edit.text()
        mycursor.execute("SELECT * FROM projecttau3 WHERE last_name = '"+lname+"' AND first_name = '"+fname+"'");
        result = mycursor.fetchall()
        if len(lname) == 0 or len(fname) == 0:
            self.messageBox("Information", " Last Name or First Neme Field  Cannot be empty!")

        else:
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    
    

           

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1129, 788)
        MainWindow.setMaximumSize(QtCore.QSize(1129, 788))
        MainWindow.setMinimumSize(QtCore.QSize(1129, 788))
        MainWindow.setWindowFlags( QtCore.Qt.WindowCloseButtonHint )
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/ico_logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        #BACKGROUND LABEL
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 0, 1151, 771))
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo/back2.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        #LOGO LABEL
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(30, 10, 131, 121))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("logo/logo.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        
       
        
        #TITLE LABEL
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(170, 40, 891, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_label.setObjectName("title_label")
        
        #TABLE FRAME
        self.table_frame = QtWidgets.QFrame(self.centralwidget)
        self.table_frame.setGeometry(QtCore.QRect(35, 140, 1061, 251))
        self.table_frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.table_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.table_frame.setObjectName("table_frame")


        ###########-------------TABLE------------------------########################
        self.tableWidget = QtWidgets.QTableWidget(self.table_frame)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 1021, 211))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: qlineargradient(spread:pad,\
            x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        font = self.tableWidget.font()
        font.setBold(True)
        font.setPointSize(8)
        self.tableWidget.setFont(font)


        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.cellClicked.connect(self.cell_click)
        self.tableWidget.setAlternatingRowColors(True)
        self.loadData()

        
        #MEMBER ID LABEL
        self.id_label = QtWidgets.QLabel(self.centralwidget)
        self.id_label.setGeometry(QtCore.QRect(40, 590, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.id_label.setFont(font)
        self.id_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.id_label.setObjectName("id_label")
        
        #MEMBER ID EDIT TEXTBOX
        self.id_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.id_edit.setGeometry(QtCore.QRect(40, 620, 161, 31))
        self.id_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.id_edit.setObjectName("id_edit")
        self.id_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.id_edit.setFont(font)
        
        
        #LAST NAME LABEL
        self.lname_label = QtWidgets.QLabel(self.centralwidget)
        self.lname_label.setGeometry(QtCore.QRect(220, 410, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lname_label.setFont(font)
        self.lname_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.lname_label.setObjectName("lname_label")

        #LAST NAME EDIT TEXTBOX
        self.lname_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.lname_edit.setGeometry(QtCore.QRect(220, 440, 251, 31))
        self.lname_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.lname_edit.setObjectName("lname_edit")
        self.lname_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.lname_edit.setFont(font)
        

        #FIRSTNAME LABEL
        self.fname_label = QtWidgets.QLabel(self.centralwidget)
        self.fname_label.setGeometry(QtCore.QRect(220, 470, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fname_label.setFont(font)
        self.fname_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.fname_label.setObjectName("fname_label")
        
        #FIRST NAME EDIT TEXTBOX
        self.fname_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.fname_edit.setGeometry(QtCore.QRect(220, 500, 251, 31))
        self.fname_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.fname_edit.setObjectName("fname_edit")
        self.fname_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.fname_edit.setFont(font)


        #AKA LABEL
        self.aka_label = QtWidgets.QLabel(self.centralwidget)
        self.aka_label.setGeometry(QtCore.QRect(220, 530, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.aka_label.setFont(font)
        self.aka_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.aka_label.setObjectName("aka_label")
        
        #AKA EDIT TEXTBOX
        self.aka_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.aka_edit.setGeometry(QtCore.QRect(220, 560, 251, 31))
        self.aka_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.aka_edit.setObjectName("aka_edit")
        self.aka_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.aka_edit.setFont(font)
        
        
        #BATCH NAME LABEL
        self.batch_label = QtWidgets.QLabel(self.centralwidget)
        self.batch_label.setGeometry(QtCore.QRect(500, 410, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.batch_label.setFont(font)
        self.batch_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.batch_label.setObjectName("batch_label")

        #BATCH NAME EDIT TEXTBOX
        self.batch_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.batch_edit.setGeometry(QtCore.QRect(500, 440, 251, 31))
        self.batch_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.batch_edit.setObjectName("batch_edit")
        self.batch_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.batch_edit.setFont(font)


        #T-BIRTH LABEL
        self.tbirth_label = QtWidgets.QLabel(self.centralwidget)
        self.tbirth_label.setGeometry(QtCore.QRect(500, 470, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tbirth_label.setFont(font)
        self.tbirth_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.tbirth_label.setObjectName("tbirth_label")

        #T-BIRTH EDIT TEXTBOX
        self.tbirth_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.tbirth_edit.setGeometry(QtCore.QRect(500, 500, 251, 31))
        self.tbirth_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.tbirth_edit.setObjectName("tbirth_edit")
        self.tbirth_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.tbirth_edit.setFont(font)

        
        #STATUS LABEL
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(500, 530, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.status_label.setFont(font)
        self.status_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.status_label.setObjectName("status_label")

        #STATUS EDIT TEXTBOX
        self.status_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.status_edit.setGeometry(QtCore.QRect(500, 560, 251, 31))
        self.status_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.status_edit.setObjectName("status_edit")
        self.status_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.status_edit.setFont(font)


        #CURRENT CHAPTER LABEL
        self.current_label = QtWidgets.QLabel(self.centralwidget)
        self.current_label.setGeometry(QtCore.QRect(780, 410, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.current_label.setFont(font)
        self.current_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.current_label.setObjectName("current_label")

        #CURRENT CHAPTER EDIT TEXTBOX
        self.current_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.current_edit.setGeometry(QtCore.QRect(780, 440, 251, 31))
        self.current_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.current_edit.setObjectName("current_edit")
        self.current_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.current_edit.setFont(font)

        #ADDRESS LABEL
        self.address_label = QtWidgets.QLabel(self.centralwidget)
        self.address_label.setGeometry(QtCore.QRect(220, 590, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.address_label.setFont(font)
        self.address_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.address_label.setObjectName("address_label")

        #ADDRESS EDIT TEXTBOX
        self.address_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.address_edit.setGeometry(QtCore.QRect(220, 620, 531, 31))
        self.address_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.address_edit.setObjectName("address_edit")
        self.address_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.address_edit.setFont(font)

       
        #ROOT CHAPTER LABEL
        self.root_label = QtWidgets.QLabel(self.centralwidget)
        self.root_label.setGeometry(QtCore.QRect(780, 470, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.root_label.setFont(font)
        self.root_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.root_label.setObjectName("root_label")

        #ROOT CHAPTER EDIT TEXTBOX
        self.root_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.root_edit.setGeometry(QtCore.QRect(780, 500, 251, 31))
        self.root_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.root_edit.setObjectName("root_edit")
        self.root_edit.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.root_edit.setFont(font)


        #PICTURE LABEL
        self.picture_label = QtWidgets.QLabel(self.centralwidget)
        self.picture_label.setGeometry(QtCore.QRect(40, 430, 161, 161))
        self.picture_label.setFrameShape(QtWidgets.QFrame.Box)
        self.picture_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.picture_label.setText("")
        self.picture_label.setObjectName("picture_label")
        self.picture_label.setPixmap(QtGui.QPixmap("logo/Men.png")) 
        self.picture_label.setScaledContents(True)
        

        
        ##############-----------------BUTTONS----------------#####################

        #ADD PICTURE BUTTON / CAMERA BUTTON
        self.camera_btn = QtWidgets.QPushButton(self.centralwidget)
        self.camera_btn.setGeometry(QtCore.QRect(40, 400, 41, 21))
        self.camera_btn.setStyleSheet("background-color:\
            qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
            stop:1 rgba(255, 255, 255, 255));")
        self.camera_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.camera_btn.setIcon(icon)
        self.camera_btn.setObjectName("camera_btn")
        self.camera_btn.clicked.connect(self.browse_image)
        self.camera_btn.setEnabled(False)


        

        #ADD PICTURE CAMERA TEXTBOX
        self.addPic_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.addPic_edit.setGeometry(QtCore.QRect(90, 400, 71, 21))
        self.addPic_edit.setStyleSheet("background-color: rgb(207, 207, 207);color: rgb(24, 24, 24)")
        self.addPic_edit.setObjectName("addPic_edit")
        self.addPic_edit.setText("logo/Men.png")
        self.addPic_edit.hide()

        #SEARCH FRAME
        self.search_frame = QtWidgets.QFrame(self.centralwidget)
        self.search_frame.setGeometry(QtCore.QRect(780, 560, 251, 161))
        self.search_frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.search_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.search_frame.setObjectName("search_frame")

        #SEARCH RADIO BUTTON
        self.search_radioButton = QtWidgets.QRadioButton(self.search_frame)
        self.search_radioButton.setGeometry(QtCore.QRect(30, 10, 82, 17))
        self.search_radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.search_radioButton.setObjectName("search_radioButton")
        self.search_radioButton.toggled.connect(self.search_radio)

        #ADVANCE SEARCH RADIO BUTTON
        self.advance_radioButton = QtWidgets.QRadioButton(self.search_frame)
        self.advance_radioButton.setGeometry(QtCore.QRect(110, 10, 121, 17))
        self.advance_radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.advance_radioButton.setObjectName("advance_radioButton")
        self.advance_radioButton.toggled.connect(self.advance_radio)

        
        #SEARCH BUTTON
        self.search_btn = QtWidgets.QPushButton(self.search_frame)
        self.search_btn.setGeometry(QtCore.QRect(20, 60, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.search_btn.setFont(font)
        self.search_btn.setStyleSheet("background-color:\
            qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
            stop:1 rgba(255, 255, 255, 255));")
        self.search_btn.setObjectName("search_btn")
        self.search_btn.clicked.connect(self.search)


        #SEARCH EDIT LAST NAME OR CHAPTER
        self.search_edit = QtWidgets.QLineEdit(self.search_frame)
        self.search_edit.setGeometry(QtCore.QRect(20, 90, 211, 31))
        self.search_edit.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.search_edit.setObjectName("search_lname_edit")
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.search_edit.setFont(font)


        

        #ADVANCE SEARCH BUTTON
        self.advance_search_btn = QtWidgets.QPushButton(self.search_frame)
        self.advance_search_btn.setGeometry(QtCore.QRect(20, 40, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.advance_search_btn.setFont(font)
        self.advance_search_btn.setStyleSheet("background-color:\
            qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
            stop:1 rgba(255, 255, 255, 255));")
        self.advance_search_btn.setObjectName("advance_search_btn")
        self.advance_search_btn.hide()
        self.advance_search_btn.clicked.connect(self.advance_search)
        
        
        #ADVANCE SEARCH EDIT LAST NAME
        self.search_lname_edit = QtWidgets.QLineEdit(self.search_frame)
        self.search_lname_edit.setGeometry(QtCore.QRect(20, 70, 211, 31))
        self.search_lname_edit.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.search_lname_edit.setObjectName("search_lname_edit")
        self.search_lname_edit.hide()
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.search_lname_edit.setFont(font)

        #ADVANCE SEARCH EDIT FIRST NAME
        self.search_fname_edit = QtWidgets.QLineEdit(self.search_frame)
        self.search_fname_edit.setGeometry(QtCore.QRect(20, 110, 211, 31))
        self.search_fname_edit.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.search_fname_edit.setObjectName("search_fname_edit")
        self.search_fname_edit.hide()
        self.search_fname_edit.setFont(font)


        
        #ADD NEW BUTTON
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(40, 680, 101, 41)) 
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.add_btn.setFont(font)
        self.add_btn.setStyleSheet("background-color: \
            qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
            stop:1 rgba(255, 255, 255, 255));")
        self.add_btn.setObjectName("add_btn")
        self.add_btn.clicked.connect(self.add)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/reg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_btn.setIcon(icon)

        
        #SAVE BUTTON
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(160, 680, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet("background-color:\
            qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
            stop:1 rgba(255, 255, 255, 255));")
        self.save_btn.setObjectName("save_btn")
        self.save_btn.setEnabled(False)
        self.save_btn.clicked.connect(self.insert_data)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_btn.setIcon(icon)

        #UPDATE BUTTON
        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setGeometry(QtCore.QRect(160, 680, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.update_btn.setFont(font)
        self.update_btn.setStyleSheet("background-color:\
            qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
            stop:1 rgba(255, 255, 255, 255));")
        self.update_btn.setObjectName("update_btn")
        self.update_btn.hide()
        self.update_btn.clicked.connect(self.update)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_btn.setIcon(icon)


        
        #CANCEL BUTTON
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(280, 680, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet("background-color: \
            qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
            stop:1 rgba(255, 255, 255, 255));")
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.clicked.connect(self.cancel)
        self.cancel_btn.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_btn.setIcon(icon)

        
        #EDIT BUTTON
        self.edit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_btn.setGeometry(QtCore.QRect(400, 680, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.edit_btn.setFont(font)
        self.edit_btn.setStyleSheet("background-color:\
            qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
            stop:1 rgba(255, 255, 255, 255));")
        self.edit_btn.setObjectName("edit_btn")
        self.edit_btn.clicked.connect(self.edit)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_btn.setIcon(icon)

        
        #REFRESH BUTTON
        self.refresh_btn = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(520, 680, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.refresh_btn.setFont(font)
        self.refresh_btn.setStyleSheet("background-color:\
            qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0),\
            stop:1 rgba(255, 255, 255, 255));")
        self.refresh_btn.setObjectName("refresh_btn")
        self.refresh_btn.clicked.connect(self.refresh)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_btn.setIcon(icon)

        
        #EXIT BUTTON
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(640, 680, 111, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.exit_btn.setFont(font)
        self.exit_btn.setStyleSheet("background-color: \
            qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), \
            stop:1 rgba(255, 255, 255, 255));")
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(self.exit_app)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon)
        
        self.label.raise_()
        self.logo_label.raise_()
        self.title_label.raise_()
        self.fname_label.raise_()
        self.lname_label.raise_()
        self.fname_edit.raise_()
        self.lname_edit.raise_()
        self.table_frame.raise_()
        self.id_edit.raise_()
        self.id_label.raise_()
        self.aka_edit.raise_()
        self.aka_label.raise_()
        self.picture_label.raise_()
        self.batch_edit.raise_()
        self.tbirth_label.raise_()
        self.tbirth_edit.raise_()
        self.status_label.raise_()
        self.status_edit.raise_()
        self.current_label.raise_()
        self.current_edit.raise_()
        self.batch_label.raise_()
        self.address_label.raise_()
        self.address_edit.raise_()
        self.camera_btn.raise_()
        self.addPic_edit.raise_()
        self.root_label.raise_()
        self.root_edit.raise_()
        self.search_frame.raise_()
        self.add_btn.raise_()
        self.save_btn.raise_()
        self.update_btn.raise_()
        self.cancel_btn.raise_()
        self.edit_btn.raise_()
        self.refresh_btn.raise_()
        self.exit_btn.raise_()
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lname_edit, self.fname_edit)
        MainWindow.setTabOrder(self.fname_edit, self.aka_edit)
        MainWindow.setTabOrder(self.aka_edit, self.batch_edit)
        MainWindow.setTabOrder(self.batch_edit, self.tbirth_edit)
        MainWindow.setTabOrder(self.tbirth_edit, self.status_edit)
        MainWindow.setTabOrder(self.status_edit, self.current_edit)
        MainWindow.setTabOrder(self.current_edit, self.root_edit)
        MainWindow.setTabOrder(self.root_edit, self.address_edit)
        MainWindow.setTabOrder(self.address_edit, self.id_edit)
        MainWindow.setTabOrder(self.id_edit, self.camera_btn)
        MainWindow.setTabOrder(self.camera_btn, self.tableWidget)
        MainWindow.setTabOrder(self.tableWidget, self.search_radioButton)
        MainWindow.setTabOrder(self.search_radioButton, self.advance_radioButton)
        MainWindow.setTabOrder(self.advance_radioButton, self.add_btn)
        MainWindow.setTabOrder(self.add_btn, self.save_btn)
        MainWindow.setTabOrder(self.save_btn, self.cancel_btn)
        MainWindow.setTabOrder(self.cancel_btn, self.edit_btn)
        MainWindow.setTabOrder(self.edit_btn, self.refresh_btn)
        MainWindow.setTabOrder(self.refresh_btn, self.exit_btn)
        MainWindow.setTabOrder(self.exit_btn, self.search_btn)
        MainWindow.setTabOrder(self.search_btn, self.search_lname_edit)
        MainWindow.setTabOrder(self.search_lname_edit, self.search_fname_edit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SAN JUAN BATANGAS MUNICIPAL COUNCIL"))
        self.lname_label.setText(_translate("MainWindow", "Last Name:"))
        self.fname_label.setText(_translate("MainWindow", "First Name:"))
        self.title_label.setText(_translate("MainWindow", "SAN JUAN BATANGAS MUNICIPAL COUNCIL"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "MEMBER ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "LAST NAME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "FIRST NAME"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "AKA"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "BATCH NAME"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "T-BIRTH"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "CURRENT CHAPTER"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "ROOT CHAPTER"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "STATUS"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "ADDRESS"))
        self.id_label.setText(_translate("MainWindow", "Member ID:"))
        self.aka_label.setText(_translate("MainWindow", "A.K.A"))
        self.batch_label.setText(_translate("MainWindow", "Batch Name:"))
        self.tbirth_label.setText(_translate("MainWindow", "T-Birth:"))
        self.status_label.setText(_translate("MainWindow", "Status:"))
        self.current_label.setText(_translate("MainWindow", "Current Chapter:"))
        self.address_label.setText(_translate("MainWindow", "Address:"))
        self.root_label.setText(_translate("MainWindow", "Root Chapter:"))
        self.search_radioButton.setText(_translate("MainWindow", "Search"))
        self.advance_radioButton.setText(_translate("MainWindow", "Advance Sesarch"))
        self.search_btn.setText(_translate("MainWindow", "Search"))
        self.advance_search_btn.setText(_translate("MainWindow", "Advance Search"))
        self.search_lname_edit.setPlaceholderText(_translate("MainWindow", "Enter Last Name"))
        self.search_fname_edit.setPlaceholderText(_translate("MainWindow", "Enter First Name"))
        self.search_edit.setPlaceholderText(_translate("MainWindow", "Enter Last Name or Chapter"))
        self.tbirth_edit.setPlaceholderText(_translate("MainWindow", "MM/DD/YYYY"))

        self.add_btn.setText(_translate("MainWindow", "Add New"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.update_btn.setText(_translate("MainWindow", "Update"))

        self.cancel_btn.setText(_translate("MainWindow", "Cancel"))
        self.edit_btn.setText(_translate("MainWindow", "Edit"))
        self.refresh_btn.setText(_translate("MainWindow", "Refresh"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
