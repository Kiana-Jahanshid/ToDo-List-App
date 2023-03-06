from PySide6.QtWidgets import *
from PySide6.QtCore import * 
from functools import partial
from main_window import Ui_MainWindow
from database import Database
from PySide6.QtGui import QFont, QMouseEvent 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        global mylist , priority_list 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mylist = []
        self.del_list=[]
        self.done_list = []
        self.labels = []
        self.priority_list = []
        self.db = Database()
        self.read_from_database()
        self.check()
        
        priority_list = ['normal' , 'high']
        self.ui.comboBox.addItems(priority_list)
        QToolTip.setFont(QFont('Arial', 14))

        self.ui.btn_new_task.clicked.connect(self.new_task)
        self.ui.btn_sort.clicked.connect(self.sort_tasks)
        self.ui.comboBox.activated.connect(self.current_text)
        


    def current_text(self, _): # We receive the index, but don't use it.
        global ctext
        ctext = self.ui.comboBox.currentText()
        print("Current text", ctext)
        return ctext
    
    def new_task(self):
        new_title = self.ui.tb_new_task_title.text() # ---> baraye line edit a hamoon text estefade mikonim
        new_description = self.ui.tb_new_task_description.toPlainText() #baraye textedit hast
        new_time = self.ui.time.text()
        new_date = self.ui.date.text()
        priority = ctext
        is_done = 0
        feedback = self.db.add_new_task(new_title , new_description , is_done , priority , new_date , new_time)
        if feedback == True :
            self.read_from_database()
            self.ui.tb_new_task_title.setText("")
            self.ui.tb_new_task_description.setText("")
            self.ui.date.setText("")
            self.ui.time.setText("")
        else :
            msg_box = QMessageBox()
            msg_box.setText("AN ERROR HAS BEEN ACCURED")
            msg_box.exec()



    def read_from_database(self):
        global tasks
        tasks = self.db.get_tasks_from_db()
        self.read_data(tasks)
        print(tasks)

    def read_data(self , tasks):
        global new_checkbox  , recyclebin_btn , new_label , priority
        for i in range(len(tasks)) :
            new_checkbox = QCheckBox() 
            new_checkbox.setFixedWidth(80)
            new_label = QLabel()      
            new_label.setText(tasks[i][1]) 
            priority = QLabel()
            priority.setText(tasks[i][4])
            new_label_2 = QLabel()
            new_label_2.setText(tasks[i][2]) #description

            self.done_list.append(tasks[i][3])
            print(self.done_list)

            recyclebin_btn = QPushButton("🗑")
            recyclebin_btn.setFixedWidth(70)

            if tasks[i][4]=="high":
                new_checkbox.setStyleSheet(u"color: rgb(255, 10, 90);\n""background-color: qlineargradient(spread:pad, x1:0.52, y1:1, x2:0.531421, y2:0.318, stop:0 rgba(232, 232, 232, 0), stop:1 rgba(255, 255, 255, 0));")
                new_label.setStyleSheet(u"color: rgb(255, 10, 90);\n""background-color: qlineargradient(spread:pad, x1:0.52, y1:1, x2:0.531421, y2:0.318, stop:0 rgba(232, 232, 232, 0), stop:1 rgba(255, 255, 255, 0));")
                priority.setStyleSheet(u"color: rgb(255, 10, 90);\n""background-color: qlineargradient(spread:pad, x1:0.52, y1:1, x2:0.531421, y2:0.318, stop:0 rgba(232, 232, 232, 0), stop:1 rgba(255, 255, 255, 0));")
                font1 = QFont()
                font1.setFamily(u"MV Boli")
                font1.setPointSize(15)
                new_label.setFont(font1)
                priority.setFont(font1)

            elif tasks[i][4] == "normal":
                new_checkbox.setStyleSheet(u"color: rgb(5, 100, 255);\n""background-color: qlineargradient(spread:pad, x1:0.52, y1:1, x2:0.531421, y2:0.318, stop:0 rgba(232, 232, 232, 0), stop:1 rgba(255, 255, 255, 0) );")
                new_label.setStyleSheet(u"color: rgb(5, 100, 255);\n""background-color: qlineargradient(spread:pad, x1:0.52, y1:1, x2:0.531421, y2:0.318, stop:0 rgba(232, 232, 232, 0), stop:1 rgba(255, 255, 255, 0) );")
                priority.setStyleSheet(u"color: rgb(5, 100, 255);\n""background-color: qlineargradient(spread:pad, x1:0.52, y1:1, x2:0.531421, y2:0.318, stop:0 rgba(232, 232, 232, 0), stop:1 rgba(255, 255, 255, 0) );")
                font2 = QFont()
                font2.setFamily(u"MV Boli")
                font2.setPointSize(15)
                new_label.setFont(font2)
                priority.setFont(font2) 


            self.labels.append(new_label)
            self.mylist.append(new_checkbox)
            self.del_list.append(recyclebin_btn)
            self.priority_list.append(priority)

            new_checkbox.toggled.connect(self.check)
            recyclebin_btn.clicked.connect(partial(self.delete ,i ))

            new_label.setToolTip(QCoreApplication.translate("MainWindow", f"<html><head/><body><p>{tasks[i][5]} <br> {tasks[i][6]} <br> {tasks[i][2]}</p></body></html>", None))
            priority.setToolTip(QCoreApplication.translate("MainWindow", f"<html><head/><body><p>{tasks[i][5]} <br> {tasks[i][6]} <br> {tasks[i][2]}</p></body></html>", None))

            self.ui.gl_tasks2.addWidget(new_checkbox ,  i  , 1 )  
            self.ui.gl_tasks2.addWidget(new_label , i , 2)
            self.ui.gl_tasks2.addWidget(priority , i  ,3 )
            self.ui.gl_tasks2.addWidget(recyclebin_btn , i , 4)
        
        c = 0
        for item in self.done_list: 
            if item == '1' :
                self.mylist[c].setText("Checked")
                self.mylist[c].setChecked(1)
            else :
                self.mylist[c].setChecked(False)
            c+= 1



    def check (self):
        for i in range(len(tasks)):
                task_title=tasks[i][1]
                if self.mylist[i].isChecked() :
                    self.mylist[i].setText("Checked")
                    self.mylist[i].setChecked(1)
                    self.db.task_done(task_title)            


    def sort_tasks(self):
        for i in reversed(range(self.ui.gl_tasks2.count())): 
            self.ui.gl_tasks2.itemAt(i).widget().setParent(None)

        sorted_list = self.db.sort()
        task_list = []
        for task in sorted_list :
                 task_list.append(task)          
        print(task_list )
        tasks = task_list
        self.read_data(tasks)


    def delete(self , i ):
        if self.db.remove_task(i+1):
            for btn in self.del_list :
                 self.del_list[i].deleteLater()
            self.labels[i].clear()
            #self.mylist[i].clear()
            self.priority_list[i].clear()

if __name__ == "__main__" :
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
