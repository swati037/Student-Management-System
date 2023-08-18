from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox, QPushButton
from PyQt5.uic import loadUi
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
mycursor = mydb.cursor()


class Get_ID(QtWidgets.QMainWindow):
    Access_ID = 2
    Access_ID2 = 1
    Access_Name = ""

#########################################################################
#                              Admin Section
#########################################################################

class SideBar(QtWidgets.QMainWindow):

    def Home(self):
        adminHP = AdminHome()
        widget.addWidget(adminHP)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def ManageStaff_f(self):
        StaffM = ManageStaff()
        widget.addWidget(StaffM)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def AddStaff_f(self):
        StaffA = AddStaff()
        widget.addWidget(StaffA)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def ManageStudent_f(self):
        StudentM = ManageStudent()
        widget.addWidget(StudentM)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def AddStudent_f(self):
        StudentA = AddStudent()
        widget.addWidget(StudentA)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def ManageCourse_f(self):
        CourseM = ManageCourse()
        widget.addWidget(CourseM)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def AddCourse_f(self):
        CourseA = AddCourse()
        widget.addWidget(CourseA)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def ManageSubject_f(self):
        SubjectM = ManageSubject()
        widget.addWidget(SubjectM)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def AddSubject_f(self):
        SubjectA = AddSubject()
        widget.addWidget(SubjectA)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def ViewAttendance_f(self):
        AttendanceV = ViewAttendance()
        widget.addWidget(AttendanceV)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def StudentFeedback_f(self):
        StudentF = StudentFeedback()
        widget.addWidget(StudentF)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def StaffFeedback_f(self):
        StaffF = StaffFeedback()
        widget.addWidget(StaffF)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def StudentLeave_f(self):
        StudentL = StudentLeave()
        widget.addWidget(StudentL)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def StaffLeave_f(self):
        StaffL = StaffLeave()
        widget.addWidget(StaffL)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class AdminLogin(Get_ID, QtWidgets.QMainWindow):
    def __init__(self):
        super(AdminLogin, self).__init__()
        loadUi("AdminLogin.ui", self)
        self.SignIn_b.clicked.connect(self.signin)

    def signin(self):

        print("Signin Button Pressed")

        Email = self.Email_tb.text()
        Password = self.Password_tb.text()
        values = (Email, Password)

        cur = mydb.cursor()

        if self.Admin_rb.isChecked():
            query = query = "SELECT * FROM AdminHOD WHERE A_Email = %s and A_Password = %s"
        elif self.Staff_rb.isChecked():
            query = "SELECT * FROM Staff WHERE Sf_Email = %s and Sf_Password = %s"
        elif self.Student_rb.isChecked():
            query = "SELECT * FROM Student WHERE St_Email = %s and St_Password = %s"
        else:
            # self.passwd_error()
            pass


        exe = cur.execute(query, values)

        if (len(cur.fetchall()) > 0):
            if self.Admin_rb.isChecked():

                exe = cur.execute(query, values)
                result = cur.fetchall()
                print(result)
                Get_ID.Access_ID = result[0][0]

                adminHP = AdminHome()
                widget.addWidget(adminHP)
                widget.setCurrentIndex(widget.currentIndex() + 1)

            elif self.Staff_rb.isChecked():

                exe = cur.execute(query, values)
                result = cur.fetchall()
                print(result)
                Get_ID.Access_ID = result[0][0]

                staffHP = StaffHome()
                widget.addWidget(staffHP)
                widget.setCurrentIndex(widget.currentIndex() + 1)

            elif self.Student_rb.isChecked():

                exe = cur.execute(query, values)
                result = cur.fetchall()
                print(result)
                Get_ID.Access_ID = result[0][0]

                studentHP = StudentHome()
                widget.addWidget(studentHP)
                widget.setCurrentIndex(widget.currentIndex() + 1)

            else:
                print("Radio Button not selected")

        else:
            print("Invalid Email or Password entered. Please Try Again")


class AdminHome(Get_ID, SideBar, QtWidgets.QMainWindow):
    def __init__(self):
        super(AdminHome, self).__init__()
        loadUi("AdminHome.ui", self)
        self.Home_b.clicked.connect(self.Home)
        self.ManageStaff_b.clicked.connect(self.ManageStaff_f)
        self.AddStaff_b.clicked.connect(self.AddStaff_f)
        self.ManageStudent_b.clicked.connect(self.ManageStudent_f)
        self.AddStudent_b.clicked.connect(self.AddStudent_f)
        self.ManageCourse_b.clicked.connect(self.ManageCourse_f)
        self.AddCourse_b.clicked.connect(self.AddCourse_f)
        self.ManageSubject_b.clicked.connect(self.ManageSubject_f)
        self.AddSubject_b.clicked.connect(self.AddSubject_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendance_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedback_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedback_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeave_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeave_f)

        self.Staffs_b.clicked.connect(self.ManageStaff_f)
        self.Students_b.clicked.connect(self.ManageStudent_f)
        self.Courses_b.clicked.connect(self.ManageCourse_f)
        self.Subjects_b.clicked.connect(self.ManageSubject_f)
        self.Logout_b.clicked.connect(self.Home_f)

        print(self.Access_ID)

    def Home_f(self):
        Logout = AdminLogin()
        widget.addWidget(Logout)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ManageStaff(Get_ID, SideBar, QtWidgets.QMainWindow):
    def __init__(self):
        super(ManageStaff, self).__init__()
        loadUi("AdminManageStaff.ui", self)
        self.ManageStaff_t.verticalHeader().setVisible(False)

        self.Home_b.clicked.connect(self.Home)
        self.ManageStaff_b.clicked.connect(self.ManageStaff_f)
        self.AddStaff_b.clicked.connect(self.AddStaff_f)
        self.ManageStudent_b.clicked.connect(self.ManageStudent_f)
        self.AddStudent_b.clicked.connect(self.AddStudent_f)
        self.ManageCourse_b.clicked.connect(self.ManageCourse_f)
        self.AddCourse_b.clicked.connect(self.AddCourse_f)
        self.ManageSubject_b.clicked.connect(self.ManageSubject_f)
        self.AddSubject_b.clicked.connect(self.AddSubject_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendance_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedback_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedback_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeave_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeave_f)

        self.Delete_b.clicked.connect(self.DeleteStaff_F)
        self.Update_b.clicked.connect(self.UpdateStaff_F)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr = mydb.cursor()
        query = "SELECT Sf_ID, Sf_Name, Sf_Gender, Sf_Email FROM Staff"
        mycurr.execute(query)

        result = mycurr.fetchall()
        self.ManageStaff_t.setRowCount(0)
        for row_number, row_data in enumerate(result):
            print(row_number)
            self.ManageStaff_t.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                print(data)
                self.ManageStaff_t.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def DeleteStaff_F(self):
        Sid = int(self.DelUpd_tb.text())
        list = [Sid]
        values = tuple(list)
        query = "DELETE FROM Staff WHERE Sf_ID = %s"
        cur = mydb.cursor()
        exe = cur.execute(query, values)
        mydb.commit()

        StaffM = ManageStaff()
        widget.addWidget(StaffM)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def UpdateStaff_F(self):
        Get_ID.Access_ID2 = int(self.DelUpd_tb.text())
        StaffU = UpdateStaff()
        widget.addWidget(StaffU)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class UpdateStaff(Get_ID, SideBar, QtWidgets.QMainWindow):
    def __init__(self):
        super(UpdateStaff, self).__init__()
        loadUi("AdminEditStaff.ui", self)
        self.Home_b.clicked.connect(self.Home)
        self.ManageStaff_b.clicked.connect(self.ManageStaff_f)
        self.AddStaff_b.clicked.connect(self.AddStaff_f)
        self.ManageStudent_b.clicked.connect(self.ManageStudent_f)
        self.AddStudent_b.clicked.connect(self.AddStudent_f)
        self.ManageCourse_b.clicked.connect(self.ManageCourse_f)
        self.AddCourse_b.clicked.connect(self.AddCourse_f)
        self.ManageSubject_b.clicked.connect(self.ManageSubject_f)
        self.AddSubject_b.clicked.connect(self.AddSubject_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendance_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedback_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedback_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeave_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeave_f)

        self.UpdateStaff_b.clicked.connect(self.UpdateStaff_F)
        print(self.Access_ID2)

        mycurr = mydb.cursor()
        query = "SELECT Sf_Name, Sf_Gender, Sf_Email, Sf_Password  FROM Staff where Sf_ID = %s"
        Sf_ID = self.Access_ID2
        values = [Sf_ID]
        mycurr.execute(query, values)
        result = mycurr.fetchall()
        print(result)
        Sf_Name = result[0][0]
        self.Name_tb.setText(Sf_Name)
        Sf_Gender = result[0][1]
        self.Gender_cmb.setCurrentText(Sf_Gender)
        Sf_Email = result[0][2]
        self.Email_tb.setText(Sf_Email)
        Sf_Password = result[0][3]
        self.Password_tb.setText(Sf_Password)

    def UpdateStaff_F(self):
        SfName = self.Name_tb.text()
        SfGender = self.Gender_cmb.currentText()
        SfEmail = self.Email_tb.text()
        if self.Password_tb.text() == self.ConfirmPassword_tb.text():
            SfPassword = self.Password_tb.text()
            query = "Update Staff set Sf_Name = %s, Sf_Gender = %s, Sf_Email = %s, Sf_Password = %s  where Sf_ID = %s"
            values = [SfName, SfGender, SfEmail, SfPassword, self.Access_ID2]
            print(values)
            cur = mydb.cursor()
            cur.execute(query, values)
            mydb.commit()

            StaffM = ManageStaff()
            widget.addWidget(StaffM)
            widget.setCurrentIndex(widget.currentIndex() + 1)

        else:
            self.PasswordError()

    def PasswordError(self):
        print("Password not matching!")
        msg = QMessageBox()
        msg.setWindowTitle("Error message!")
        msg.setText("Password not matching!. Please Enter Password Again")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()
        self.Password_tb.clear()
        self.ConfirmPassword_tb.clear()


class AddStaff(Get_ID, SideBar, QtWidgets.QMainWindow):
    def __init__(self):
        super(AddStaff, self).__init__()
        loadUi("AdminAddStaff.ui", self)
        self.Home_b.clicked.connect(self.Home)
        self.ManageStaff_b.clicked.connect(self.ManageStaff_f)
        self.AddStaff_b.clicked.connect(self.AddStaff_f)
        self.ManageStudent_b.clicked.connect(self.ManageStudent_f)
        self.AddStudent_b.clicked.connect(self.AddStudent_f)
        self.ManageCourse_b.clicked.connect(self.ManageCourse_f)
        self.AddCourse_b.clicked.connect(self.AddCourse_f)
        self.ManageSubject_b.clicked.connect(self.ManageSubject_f)
        self.AddSubject_b.clicked.connect(self.AddSubject_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendance_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedback_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedback_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeave_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeave_f)

        self.AddStaff_b_2.clicked.connect(self.AddStaff_F)

    def AddStaff_F(self):
        Name = self.Name_tb.text()
        Gender = self.Gender_cmb.currentText()
        Email = self.Email_tb.text()
        if self.Password_tb.text() == self.ConfirmPassword_tb.text():
            Password = self.Password_tb.text()
            query = "INSERT INTO Staff(Sf_Name, Sf_Gender, Sf_Email, Sf_Password) VALUES(%s,%s,%s,%s)"
            values = (Name, Gender, Email, Password)
            cur = mydb.cursor()
            cur.execute(query, values)
            mydb.commit()

            StaffM = ManageStaff()
            widget.addWidget(StaffM)
            widget.setCurrentIndex(widget.currentIndex() + 1)

        else:
            self.PasswordError()

    def PasswordError(self):
        print("Password not matching!")
        msg = QMessageBox()
        msg.setWindowTitle("Error message!")
        msg.setText("Password not matching!. Please Enter Password Again")
        msg.setIcon(QMessageBox.Information)
        print('kapil')
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()
        self.Password_tb.clear()
        self.ConfirmPassword_tb.clear()


class ManageStudent(Get_ID, SideBar, QtWidgets.QMainWindow):
    def __init__(self):
        super(ManageStudent, self).__init__()
        loadUi("AdminManageStudent.ui", self)
        self.ManageStudent_t.verticalHeader().setVisible(False)
        self.Home_b.clicked.connect(self.Home)
        self.ManageStaff_b.clicked.connect(self.ManageStaff_f)
        self.AddStaff_b.clicked.connect(self.AddStaff_f)
        self.ManageStudent_b.clicked.connect(self.ManageStudent_f)
        self.AddStudent_b.clicked.connect(self.AddStudent_f)
        self.ManageCourse_b.clicked.connect(self.ManageCourse_f)
        self.AddCourse_b.clicked.connect(self.AddCourse_f)
        self.ManageSubject_b.clicked.connect(self.ManageSubject_f)
        self.AddSubject_b.clicked.connect(self.AddSubject_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendance_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedback_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedback_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeave_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeave_f)

        self.Delete_b.clicked.connect(self.DeleteStudent_F)
        self.Update_b.clicked.connect(self.UpdateStudent_F)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr = mydb.cursor()
        query = "SELECT Student.St_ID, Student.St_Name, Student.St_Gender, Course.C_Name, Student.St_Email FROM Student INNER JOIN Course ON Student.C_ID = Course.C_ID"
        mycurr.execute(query)

        result = mycurr.fetchall()
        self.ManageStudent_t.setRowCount(0)
        for row_number, row_data in enumerate(result):
            print(row_number)
            self.ManageStudent_t.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                print(data)
                self.ManageStudent_t.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def DeleteStudent_F(self):
        Sid = int(self.DelUpd_tb.text())
        list = [Sid]
        values = tuple(list)
        query = "DELETE FROM Student WHERE St_ID = %s"
        cur = mydb.cursor()
        exe = cur.execute(query, values)
        mydb.commit()

        StudentM = ManageStudent()
        widget.addWidget(StudentM)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def UpdateStudent_F(self):
        Get_ID.Access_ID2 = int(self.DelUpd_tb.text())
        StudentU = UpdateStudent()
        widget.addWidget(StudentU)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class UpdateStudent(Get_ID, SideBar, QtWidgets.QMainWindow):
    def __init__(self):
        super(UpdateStudent, self).__init__()
        loadUi("AdminEditStudent.ui", self)
        self.Home_b.clicked.connect(self.Home)
        self.ManageStaff_b.clicked.connect(self.ManageStaff_f)
        self.AddStaff_b.clicked.connect(self.AddStaff_f)
        self.ManageStudent_b.clicked.connect(self.ManageStudent_f)
        self.AddStudent_b.clicked.connect(self.AddStudent_f)
        self.ManageCourse_b.clicked.connect(self.ManageCourse_f)
        self.AddCourse_b.clicked.connect(self.AddCourse_f)
        self.ManageSubject_b.clicked.connect(self.ManageSubject_f)
        self.AddSubject_b.clicked.connect(self.AddSubject_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendance_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedback_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedback_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeave_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeave_f)

        self.UpdateStudent_b.clicked.connect(self.UpdateStudent_F)
        print(self.Access_ID2)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr = mydb.cursor()
        query = "SELECT St_Name, St_Gender, St_Email, St_Password, C_ID FROM Student where St_ID = %s"
        St_ID = self.Access_ID2
        values = [St_ID]
        mycurr.execute(query, values)
        result = mycurr.fetchall()
        print(result)

        St_Name = result[0][0]
        self.Name_tb.setText(St_Name)
        St_Gender = result[0][1]
        self.Gender_cmb.setCurrentText(St_Gender)
        St_Email = result[0][2]
        self.Email_tb.setText(St_Email)
        St_Password = result[0][3]
        self.Password_tb.setText(St_Password)
        C_ID = result[0][4]


        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr1 = mydb.cursor()
        query1 = "SELECT C_Name FROM Course"
        mycurr1.execute(query1)
        Courselist  = []
        # Dump results into a list called customerlist
        Courselist = [row[0] for row in mycurr1.fetchall()]
        for i in Courselist:
            self.Course_cmb.addItem(str(i))

        #mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr2 = mydb.cursor()
        query2 = "SELECT C_ID FROM Course"
        mycurr2.execute(query2)
        Courselist2 = []
        # Dump results into a list called customerlist
        Courselist2 = [row[0] for row in mycurr2.fetchall()]
        print(Courselist2)
        print(C_ID)
        index = Courselist2.index(C_ID)
        print('The index of i:', index)
        self.Course_cmb.setCurrentText(Courselist[index])
        print(str(index))
        print(Courselist[index])

    def UpdateStudent_F(self):
        StName = self.Name_tb.text()
        StGender = self.Gender_cmb.currentText()
        StCourse = self.Course_cmb.currentText()
        StEmail = self.Email_tb.text()

        query2 = "SELECT C_ID FROM Course WHERE C_Name = %s"
        list2 = [StCourse]
        values2 = tuple(list2)
        print(values2)
        cur2 = mydb.cursor()
        cur2.execute(query2, values2)
        C_ID = cur2.fetchone()
        print(C_ID)


        if self.Password_tb.text() == self.ConfirmPassword_tb.text():
            StPassword = self.Password_tb.text()
            query = "Update Student set St_Name = %s, St_Gender = %s, St_Email = %s, St_Password = %s, C_ID = %s where St_ID = %s"
            values = [StName, StGender, StEmail, StPassword, C_ID[0], self.Access_ID2]
            print(values)
            cur = mydb.cursor()
            cur.execute(query, values)
            mydb.commit()

            StudentM = ManageStudent()
            widget.addWidget(StudentM)
            widget.setCurrentIndex(widget.currentIndex() + 1)

        else:
            self.PasswordError()

    def PasswordError(self):
        print("Password not matching!")
        msg = QMessageBox()
        msg.setWindowTitle("Error message!")
        msg.setText("Password not matching!. Please Enter Password Again")
        msg.setIcon(QMessageBox.Information)
        print('kapil')
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()
        self.Password_tb.clear()
        self.ConfirmPassword_tb.clear()


class AddStudent(Get_ID, SideBar, QtWidgets.QMainWindow):
    def __init__(self):
        super(AddStudent, self).__init__()
        loadUi("AdminAddStudent.ui", self)
        self.Home_b.clicked.connect(self.Home)
        self.ManageStaff_b.clicked.connect(self.ManageStaff_f)
        self.AddStaff_b.clicked.connect(self.AddStaff_f)
        self.ManageStudent_b.clicked.connect(self.ManageStudent_f)
        self.AddStudent_b.clicked.connect(self.AddStudent_f)
        self.ManageCourse_b.clicked.connect(self.ManageCourse_f)
        self.AddCourse_b.clicked.connect(self.AddCourse_f)
        self.ManageSubject_b.clicked.connect(self.ManageSubject_f)
        self.AddSubject_b.clicked.connect(self.AddSubject_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendance_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedback_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedback_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeave_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeave_f)

        self.AddStudent_b_2.clicked.connect(self.AddStudent_F)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr1 = mydb.cursor()
        query1 = "SELECT C_Name FROM Course"
        mycurr1.execute(query1)
        Courselist = []
        # Dump results into a list called customerlist
        Courselist = [row[0] for row in mycurr1.fetchall()]
        for i in Courselist:
            self.Course_cmb.addItem(str(i))


    def AddStudent_F(self):
        Name = self.Name_tb.text()
        Gender = self.Gender_cmb.currentText()
        Email = self.Email_tb.text()
        Course = self.Course_cmb.currentText()

        query2 = "SELECT C_ID FROM Course WHERE C_Name = %s"
        list2 = [Course]
        values2 = tuple(list2)
        print(values2)
        cur2 = mydb.cursor()
        cur2.execute(query2, values2)
        C_ID = cur2.fetchone()
        print(C_ID)

        if self.Password_tb.text() == self.ConfirmPassword_tb.text():
            Password = self.Password_tb.text()

            # Getting the ID of the Course
            query = "INSERT INTO Student(St_Name, St_Gender, St_Email, St_Password, C_ID) VALUES(%s,%s,%s,%s,%s)"
            values = (Name, Gender, Email, Password, C_ID[0])
            cur = mydb.cursor()
            print(query)
            print(values)
            cur.execute(query, values)
            print("Hello")
            mydb.commit()

            StudentM = ManageStudent()
            widget.addWidget(StudentM)
            widget.setCurrentIndex(widget.currentIndex() + 1)

        else:
            self.PasswordError()

    def PasswordError(self):
        print("Password not matching!")
        msg = QMessageBox()
        msg.setWindowTitle("Error message!")
        msg.setText("Password not matching!. Please Enter Password Again")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()
        self.Password_tb.clear()
        self.ConfirmPassword_tb.clear()


##################################  MANAGE COURSE PAGE  ##################################################
class ManageCourse(Get_ID, SideBar, QtWidgets.QMainWindow):
    def __init__(self):
        super(ManageCourse, self).__init__()
        loadUi("AdminManageCourse.ui", self)
        self.ManageCourse_t.verticalHeader().setVisible(False)
        self.Home_b.clicked.connect(self.Home)
        self.ManageStaff_b.clicked.connect(self.ManageStaff_f)
        self.AddStaff_b.clicked.connect(self.AddStaff_f)
        self.ManageStudent_b.clicked.connect(self.ManageStudent_f)
        self.AddStudent_b.clicked.connect(self.AddStudent_f)
        self.ManageCourse_b.clicked.connect(self.ManageCourse_f)
        self.AddCourse_b.clicked.connect(self.AddCourse_f)
        self.ManageSubject_b.clicked.connect(self.ManageSubject_f)
        self.AddSubject_b.clicked.connect(self.AddSubject_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendance_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedback_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedback_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeave_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeave_f)

        self.Delete_b.clicked.connect(self.DeleteCourse_F)
        self.Update_b.clicked.connect(self.UpdateCourse_F)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr = mydb.cursor()
        query = "SELECT * FROM Course"
        mycurr.execute(query)

        result = mycurr.fetchall()
        self.ManageCourse_t.setRowCount(0)
        for row_number, row_data in enumerate(result):
            print(row_number)
            self.ManageCourse_t.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                print(data)
                self.ManageCourse_t.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def DeleteCourse_F(self):
        Sid = int(self.DelUpd_tb.text())
        list = [Sid]
        values = tuple(list)
        query = "DELETE FROM Course WHERE C_ID = %s"
        cur = mydb.cursor()
        exe = cur.execute(query, values)
        mydb.commit()

        CourseM = ManageCourse()
        widget.addWidget(CourseM)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def UpdateCourse_F(self):
        Get_ID.Access_ID2 = int(self.DelUpd_tb.text())
        CourseU = UpdateCourse()
        widget.addWidget(CourseU)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class UpdateCourse(Get_ID, SideBar, QtWidgets.QMainWindow):
    def __init__(self):
        super(UpdateCourse, self).__init__()
        loadUi("AdminEditCourse.ui", self)
        self.Home_b.clicked.connect(self.Home)
        self.ManageStaff_b.clicked.connect(self.ManageStaff_f)
        self.AddStaff_b.clicked.connect(self.AddStaff_f)
        self.ManageStudent_b.clicked.connect(self.ManageStudent_f)
        self.AddStudent_b.clicked.connect(self.AddStudent_f)
        self.ManageCourse_b.clicked.connect(self.ManageCourse_f)
        self.AddCourse_b.clicked.connect(self.AddCourse_f)
        self.ManageSubject_b.clicked.connect(self.ManageSubject_f)
        self.AddSubject_b.clicked.connect(self.AddSubject_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendance_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedback_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedback_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeave_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeave_f)

        self.UpdateCourse_b.clicked.connect(self.UpdateCourse_F)
        print(self.Access_ID2)

        mycurr = mydb.cursor()
        query = "SELECT C_Name FROM Course where C_ID = %s"
        C_ID = self.Access_ID2
        values = [C_ID]
        mycurr.execute(query, values)
        result = mycurr.fetchall()
        print(result)
        C_Name = result[0][0]
        self.CourseName_tb.setText(C_Name)

    def UpdateCourse_F(self):
        Course = self.CourseName_tb.text()
        query = "Update Course set C_Name = %s where C_ID = %s"
        values = [Course, self.Access_ID2]
        cur = mydb.cursor()
        cur.execute(query, values)
        mydb.commit()

        CourseM = ManageCourse()
        widget.addWidget(CourseM)
        widget.setCurrentIndex(widget.currentIndex() + 1)


##################################  ADD COURSE PAGE  ##################################################
class AddCourse(Get_ID, SideBar, QtWidgets.QMainWindow):
    def __init__(self):
        super(AddCourse, self).__init__()
        loadUi("AdminAddCourse.ui", self)
        self.Home_b.clicked.connect(self.Home)
        self.ManageStaff_b.clicked.connect(self.ManageStaff_f)
        self.AddStaff_b.clicked.connect(self.AddStaff_f)
        self.ManageStudent_b.clicked.connect(self.ManageStudent_f)
        self.AddStudent_b.clicked.connect(self.AddStudent_f)
        self.ManageCourse_b.clicked.connect(self.ManageCourse_f)
        self.AddCourse_b.clicked.connect(self.AddCourse_f)
        self.ManageSubject_b.clicked.connect(self.ManageSubject_f)
        self.AddSubject_b.clicked.connect(self.AddSubject_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendance_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedback_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedback_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeave_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeave_f)

        self.AddCourse_b_2.clicked.connect(self.AddCourse_F)

    def AddCourse_F(self):
        Course = self.CourseName_tb.text()
        query = "INSERT INTO Course(C_Name) VALUES(%s)"
        list = [Course]
        values = tuple(list)
        cur = mydb.cursor()
        cur.execute(query, values)
        mydb.commit()

        CourseM = ManageCourse()
        widget.addWidget(CourseM)
        widget.setCurrentIndex(widget.currentIndex() + 1)


##################################  MANAGE SUBJECT PAGE  ##################################################
class ManageSubject(Get_ID, SideBar, QtWidgets.QMainWindow):
    def __init__(self):
        super(ManageSubject, self).__init__()
        loadUi("AdminManageSubject.ui", self)
        self.ManageSubject_t.verticalHeader().setVisible(False)
        self.Home_b.clicked.connect(self.Home)
        self.ManageStaff_b.clicked.connect(self.ManageStaff_f)
        self.AddStaff_b.clicked.connect(self.AddStaff_f)
        self.ManageStudent_b.clicked.connect(self.ManageStudent_f)
        self.AddStudent_b.clicked.connect(self.AddStudent_f)
        self.ManageCourse_b.clicked.connect(self.ManageCourse_f)
        self.AddCourse_b.clicked.connect(self.AddCourse_f)
        self.ManageSubject_b.clicked.connect(self.ManageSubject_f)
        self.AddSubject_b.clicked.connect(self.AddSubject_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendance_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedback_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedback_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeave_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeave_f)

        self.Delete_b.clicked.connect(self.DeleteSubject_F)
        self.Update_b.clicked.connect(self.UpdateSubject_F)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr = mydb.cursor()
        query = "SELECT Subject.Sub_ID, Subject.Sub_Name, Staff.Sf_Name, Course.C_Name FROM ((Subject INNER JOIN Course ON Subject.C_ID = Course.C_ID) INNER JOIN Staff ON Subject.Sf_ID = Staff.Sf_ID)"
        mycurr.execute(query)

        result = mycurr.fetchall()
        self.ManageSubject_t.setRowCount(0)
        for row_number, row_data in enumerate(result):
            print(row_number)
            self.ManageSubject_t.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                print(data)
                self.ManageSubject_t.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def DeleteSubject_F(self):
        Sid = int(self.DelUpd_tb.text())
        list = [Sid]
        values = tuple(list)
        query = "DELETE FROM Subject WHERE Sub_ID = %s"
        cur = mydb.cursor()
        exe = cur.execute(query, values)
        mydb.commit()

        SubjectM = ManageSubject()
        widget.addWidget(SubjectM)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def UpdateSubject_F(self):
        Get_ID.Access_ID2 = int(self.DelUpd_tb.text())
        SubjectU = UpdateSubject()
        widget.addWidget(SubjectU)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class UpdateSubject(Get_ID, SideBar, QtWidgets.QMainWindow):
    def __init__(self):
        print("Hello")
        super(UpdateSubject, self).__init__()
        loadUi("AdminEditSubject.ui", self)
        self.Home_b.clicked.connect(self.Home)
        self.ManageStaff_b.clicked.connect(self.ManageStaff_f)
        self.AddStaff_b.clicked.connect(self.AddStaff_f)
        self.ManageStudent_b.clicked.connect(self.ManageStudent_f)
        self.AddStudent_b.clicked.connect(self.AddStudent_f)
        self.ManageCourse_b.clicked.connect(self.ManageCourse_f)
        self.AddCourse_b.clicked.connect(self.AddCourse_f)
        self.ManageSubject_b.clicked.connect(self.ManageSubject_f)
        self.AddSubject_b.clicked.connect(self.AddSubject_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendance_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedback_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedback_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeave_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeave_f)

        self.UpdateSubject_b.clicked.connect(self.UpdateSubject_F)
        print(self.Access_ID2)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr = mydb.cursor()
        query = "SELECT Sub_Name, Sf_ID, C_ID FROM Subject where Sub_ID = %s"
        Sub_ID = self.Access_ID2
        values = [Sub_ID]
        mycurr.execute(query, values)
        result = mycurr.fetchall()
        print(result)

        Sub_Name = result[0][0]
        self.SubjectName_tb.setText(Sub_Name)
        Sf_ID = result[0][1]
        C_ID = result[0][2]

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr2 = mydb.cursor()
        query2 = "SELECT Sf_Name FROM Staff"
        mycurr2.execute(query2)
        Stafflist = []
        # Dump results into a list called customerlist
        Stafflist = [row[0] for row in mycurr2.fetchall()]
        for i in Stafflist:
            self.Staff_cmb.addItem(str(i))

        # mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr4 = mydb.cursor()
        query4 = "SELECT Sf_ID FROM Staff"
        mycurr4.execute(query4)
        Stafflist4 = []
        # Dump results into a list called customerlist
        Stafflist4 = [row[0] for row in mycurr4.fetchall()]
        print(Stafflist4)
        print(Sf_ID)
        index4 = Stafflist4.index(Sf_ID)
        print('The index of i:', index4)
        self.Staff_cmb.setCurrentText(Stafflist[index4])
        print(str(index4))
        print(Stafflist[index4])


        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr1 = mydb.cursor()
        query1 = "SELECT C_Name FROM Course"
        mycurr1.execute(query1)
        Courselist = []
        # Dump results into a list called customerlist
        Courselist = [row[0] for row in mycurr1.fetchall()]
        print(Courselist)
        for i in Courselist:
            self.Course_cmb.addItem(str(i))

        #mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr3 = mydb.cursor()
        query3 = "SELECT C_ID FROM Course"
        mycurr3.execute(query3)
        Courselist3 = []
        # Dump results into a list called customerlist
        Courselist3 = [row[0] for row in mycurr3.fetchall()]
        print(Courselist3)
        print(C_ID)
        index2 = Courselist3.index(C_ID)
        print('The index of i:', index2)
        self.Course_cmb.setCurrentText(Courselist[index2])
        print(str(index2))
        print(Courselist[index2])

    def UpdateSubject_F(self):
        print("Hello")
        Subject = self.SubjectName_tb.text()
        Staff = self.Staff_cmb.currentText()
        Course = self.Course_cmb.currentText()

        query1 = "SELECT Sf_ID FROM Staff WHERE SF_Name = %s"
        list1 = [Staff]
        values1 = tuple(list1)
        print(values1)
        cur1 = mydb.cursor()
        cur1.execute(query1, values1)
        Sf_ID = cur1.fetchone()
        print(Sf_ID)

        query2 = "SELECT C_ID FROM Course WHERE C_Name = %s"
        list2 = [Course]
        values2 = tuple(list2)
        cur2 = mydb.cursor()
        print(values2)
        cur2.execute(query2, values2)
        C_ID = cur2.fetchone()

        query3 = "Update Subject set Sub_Name = %s, Sf_ID = %s, C_ID = %s where Sub_ID = %s"
        values3 = [Subject, Sf_ID[0], C_ID[0], self.Access_ID2]
        cur3 = mydb.cursor()
        cur3.execute(query3, values3)
        mydb.commit()

        SubjectM = ManageSubject()
        widget.addWidget(SubjectM)
        widget.setCurrentIndex(widget.currentIndex() + 1)


##################################  ADD SUBJECT PAGE  ##################################################
class AddSubject(Get_ID, SideBar, QtWidgets.QMainWindow):
    def __init__(self):
        super(AddSubject, self).__init__()
        loadUi("AdminAddSubject.ui", self)
        self.Home_b.clicked.connect(self.Home)
        self.ManageStaff_b.clicked.connect(self.ManageStaff_f)
        self.AddStaff_b.clicked.connect(self.AddStaff_f)
        self.ManageStudent_b.clicked.connect(self.ManageStudent_f)
        self.AddStudent_b.clicked.connect(self.AddStudent_f)
        self.ManageCourse_b.clicked.connect(self.ManageCourse_f)
        self.AddCourse_b.clicked.connect(self.AddCourse_f)
        self.ManageSubject_b.clicked.connect(self.ManageSubject_f)
        self.AddSubject_b.clicked.connect(self.AddSubject_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendance_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedback_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedback_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeave_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeave_f)

        self.AddSubject_b_2.clicked.connect(self.AddSubject_F)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr1 = mydb.cursor()
        query1 = "SELECT C_Name FROM Course"
        mycurr1.execute(query1)
        Courselist = []
        # Dump results into a list called customerlist
        Courselist = [row[0] for row in mycurr1.fetchall()]
        for i in Courselist:
            self.Course_cmb.addItem(str(i))

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr2 = mydb.cursor()
        query2 = "SELECT Sf_Name FROM Staff"
        mycurr2.execute(query2)
        Stafflist = []
        # Dump results into a list called customerlist
        Stafflist = [row[0] for row in mycurr2.fetchall()]
        for i in Stafflist:
            self.Staff_cmb.addItem(str(i))

    def AddSubject_F(self):
        Subject = self.SubjectName_tb.text()

        Staff = self.Staff_cmb.currentText()
        Course = self.Course_cmb.currentText()

        query1 = "SELECT Sf_ID FROM Staff WHERE SF_Name = %s"
        list1 = [Staff]
        values1 = tuple(list1)
        cur1 = mydb.cursor()
        cur1.execute(query1, values1)
        Sf_ID = cur1.fetchone()

        query2 = "SELECT C_ID FROM Course WHERE C_Name = %s"
        list2 = [Course]
        values2 = tuple(list2)
        cur2 = mydb.cursor()
        cur2.execute(query2, values2)
        C_ID = cur2.fetchone()

        values3 = (Subject, Sf_ID[0], C_ID[0])
        query3 = "INSERT INTO Subject(Sub_Name, Sf_ID, C_ID) VALUES(%s, %s, %s)"
        cur3 = mydb.cursor()
        cur3.execute(query3, values3)
        print("Hello")
        mydb.commit()

        SubjectM = ManageSubject()
        widget.addWidget(SubjectM)
        widget.setCurrentIndex(widget.currentIndex() + 1)

        mydb.commit()


##################################  VIEW ATTENDANCE PAGE  ##################################################
class ViewAttendance(Get_ID, SideBar,QtWidgets.QMainWindow):
    def __init__(self):
        super(ViewAttendance, self).__init__()
        loadUi("AdminAttendance.ui", self)
        self.Home_b.clicked.connect(self.Home)
        self.ManageStaff_b.clicked.connect(self.ManageStaff_f)
        self.AddStaff_b.clicked.connect(self.AddStaff_f)
        self.ManageStudent_b.clicked.connect(self.ManageStudent_f)
        self.AddStudent_b.clicked.connect(self.AddStudent_f)
        self.ManageCourse_b.clicked.connect(self.ManageCourse_f)
        self.AddCourse_b.clicked.connect(self.AddCourse_f)
        self.ManageSubject_b.clicked.connect(self.ManageSubject_f)
        self.AddSubject_b.clicked.connect(self.AddSubject_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendance_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedback_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedback_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeave_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeave_f)

        self.EnterSubject_b.clicked.connect(self.GetDate_F)
        self.FetchAttendance_b.clicked.connect(self.FetchAttd_F)

        print("1")

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycur = mydb.cursor()
        query = "SELECT Sub_Name FROM Subject"
        mycur.execute(query)

        Subjectlist = [row[0] for row in mycur.fetchall()]
        for i in Subjectlist:
            self.Subject_cmb.addItem(str(i))


    def GetDate_F(self):
        sub = self.Subject_cmb.currentText()
        print(sub)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycur = mydb.cursor()
        query = "SELECT Attendance.A_Date From Attendance INNER JOIN Subject ON Subject.Sub_ID = Attendance.Sub_ID WHERE Subject.Sub_Name = %s"
        values = [sub]
        mycur.execute(query, values)

        Datelist = [row[0] for row in mycur.fetchall()]
        self.Date_cmb.clear()
        for i in Datelist:
            self.Date_cmb.addItem(str(i))

    def FetchAttd_F(self):
        sub = self.Subject_cmb.currentText()
        date = self.Date_cmb.currentText()
        values = [sub, date]
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycur = mydb.cursor()
        query = "SELECT Student.St_name, AttendanceReport.AR_Status FROM (((AttendanceReport INNER JOIN Attendance ON AttendanceReport.A_ID = Attendance.A_ID) INNER JOIN Student ON Student.St_ID = AttendanceReport.St_ID) INNER JOIN Subject ON Subject.Sub_ID = Attendance.Sub_ID) WHERE Subject.Sub_Name = %s AND Attendance.A_Date = %s"
        mycur.execute(query, values)
        table = mycur.fetchall()
        print(table)

        self.ViewAttendance_t.setRowCount(0)
        for row_number, row_data in enumerate(table):
            # print(row_number)
            self.ViewAttendance_t.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                # print(data)
                self.ViewAttendance_t.setItem(row_number, column_number, QTableWidgetItem(str(data)))


##################################  STUDENT FEEDBACK PAGE  ##################################################
class StudentFeedback(Get_ID, SideBar, QtWidgets.QMainWindow):
    def __init__(self):
        super(StudentFeedback, self).__init__()
        loadUi("AdminStudentFeedback.ui", self)
        self.Home_b.clicked.connect(self.Home)
        self.ManageStaff_b.clicked.connect(self.ManageStaff_f)
        self.AddStaff_b.clicked.connect(self.AddStaff_f)
        self.ManageStudent_b.clicked.connect(self.ManageStudent_f)
        self.AddStudent_b.clicked.connect(self.AddStudent_f)
        self.ManageCourse_b.clicked.connect(self.ManageCourse_f)
        self.AddCourse_b.clicked.connect(self.AddCourse_f)
        self.ManageSubject_b.clicked.connect(self.ManageSubject_f)
        self.AddSubject_b.clicked.connect(self.AddSubject_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendance_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedback_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedback_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeave_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeave_f)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr = mydb.cursor()
        query = "SELECT Student.St_Name, St_Feedback.Fdb_Message, St_Feedback.Fdb_Reply FROM St_Feedback INNER JOIN Student ON St_Feedback.St_ID = Student.St_ID"
        mycurr.execute(query)

        result = mycurr.fetchall()
        self.StudentFeedback_t.setRowCount(0)
        for row_number, row_data in enumerate(result):
            # print(row_number)
            self.StudentFeedback_t.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                # print(data)
                self.StudentFeedback_t.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.StudentFeedback_t.cellClicked.connect(self.Get_Row)

    def Get_Row(self):
        try:
            rowCount = self.StudentFeedback_t.rowCount()
            for row in range(rowCount):
                if self.StudentFeedback_t.item(row, 0).isSelected():
                    rowNum = row + 1
                    Get_ID.Access_ID2 = rowNum
                    print(self.Access_ID2)

            St_Reply = StudentReply()
            widget.addWidget(St_Reply)
            widget.setCurrentIndex(widget.currentIndex() + 1)

        except:
            print("Please click on match number.")


##################################  STUDENT FEEDBACK REPLY ###########################################
class StudentReply(Get_ID, SideBar, QtWidgets.QMainWindow):
    def __init__(self):
        super(StudentReply, self).__init__()
        loadUi("StudentReply.ui", self)
        self.Home_b.clicked.connect(self.Home)
        self.ManageStaff_b.clicked.connect(self.ManageStaff_f)
        self.AddStaff_b.clicked.connect(self.AddStaff_f)
        self.ManageStudent_b.clicked.connect(self.ManageStudent_f)
        self.AddStudent_b.clicked.connect(self.AddStudent_f)
        self.ManageCourse_b.clicked.connect(self.ManageCourse_f)
        self.AddCourse_b.clicked.connect(self.AddCourse_f)
        self.ManageSubject_b.clicked.connect(self.ManageSubject_f)
        self.AddSubject_b.clicked.connect(self.AddSubject_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendance_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedback_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedback_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeave_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeave_f)

        self.SendReply_b.clicked.connect(self.StudentReply_F)
        print(self.Access_ID2)

        mycurr = mydb.cursor()
        query = "SELECT Student.St_Name, St_Feedback.Fdb_Message, St_Feedback.Fdb_Reply FROM St_Feedback INNER JOIN Student ON St_Feedback.St_ID = Student.St_ID WHERE St_FeedBack.Fdb_ID = %s"
        Fdb_ID = self.Access_ID2
        values = [Fdb_ID]
        mycurr.execute(query, values)
        result = mycurr.fetchall()
        print(result)
        St_Name = result[0][0]
        self.Name_l_2.setText(St_Name)
        Fdb_Message = result[0][1]
        self.Feedback_tb.setText(Fdb_Message)
        Fdb_Reply = result[0][2]
        self.Reply_tb.setText(Fdb_Reply)

    def StudentReply_F(self):
        print("DD")
        FdbReply = self.Reply_tb.toPlainText()
        print("DD")
        query = "Update st_feedback set  Fdb_Reply = %s where  Fdb_ID = %s"
        values = [FdbReply, self.Access_ID2]
        print("g", values)
        cur = mydb.cursor()
        cur.execute(query, values)
        mydb.commit()

        St_Feedback = StudentFeedback()
        widget.addWidget(St_Feedback)
        widget.setCurrentIndex(widget.currentIndex() + 1)


##################################  STAFF FEEDBACK PAGE  ##################################################
class StaffFeedback(Get_ID, SideBar,QtWidgets.QMainWindow):
    def __init__(self):
        super(StaffFeedback, self).__init__()
        loadUi("AdminStaffFeedback.ui", self)
        self.Home_b.clicked.connect(self.Home)
        self.ManageStaff_b.clicked.connect(self.ManageStaff_f)
        self.AddStaff_b.clicked.connect(self.AddStaff_f)
        self.ManageStudent_b.clicked.connect(self.ManageStudent_f)
        self.AddStudent_b.clicked.connect(self.AddStudent_f)
        self.ManageCourse_b.clicked.connect(self.ManageCourse_f)
        self.AddCourse_b.clicked.connect(self.AddCourse_f)
        self.ManageSubject_b.clicked.connect(self.ManageSubject_f)
        self.AddSubject_b.clicked.connect(self.AddSubject_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendance_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedback_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedback_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeave_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeave_f)


        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr = mydb.cursor()
        query = "SELECT Staff.Sf_Name, Sf_Feedback.Fdb_Message, Sf_Feedback.Fdb_Reply FROM Sf_Feedback INNER JOIN Staff ON Sf_Feedback.Sf_ID = Staff.Sf_ID"
        mycurr.execute(query)

        result = mycurr.fetchall()
        self.StaffFeedback_t.setRowCount(0)
        for row_number, row_data in enumerate(result):
            #print(row_number)
            self.StaffFeedback_t.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                #print(data)
                self.StaffFeedback_t.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.StaffFeedback_t.cellClicked.connect(self.Get_Row)

    def Get_Row(self):
        try:
            rowCount = self.StaffFeedback_t.rowCount()
            for row in range(rowCount):
                if self.StaffFeedback_t.item(row, 0).isSelected():
                    rowNum = row + 1
                    Get_ID.Access_ID2 = rowNum
                    print(self.Access_ID2)

            Sf_Reply = StaffReply()
            widget.addWidget(Sf_Reply)
            widget.setCurrentIndex(widget.currentIndex() + 1)

        except:
            print("Please click on match number.")


##################################  STAFF FEEDBACK REPLY ###########################################

class StaffReply(Get_ID, SideBar, QtWidgets.QMainWindow):
    def __init__(self):
        super(StaffReply, self).__init__()
        loadUi("StaffReply.ui", self)
        self.Home_b.clicked.connect(self.Home)
        self.ManageStaff_b.clicked.connect(self.ManageStaff_f)
        self.AddStaff_b.clicked.connect(self.AddStaff_f)
        self.ManageStudent_b.clicked.connect(self.ManageStudent_f)
        self.AddStudent_b.clicked.connect(self.AddStudent_f)
        self.ManageCourse_b.clicked.connect(self.ManageCourse_f)
        self.AddCourse_b.clicked.connect(self.AddCourse_f)
        self.ManageSubject_b.clicked.connect(self.ManageSubject_f)
        self.AddSubject_b.clicked.connect(self.AddSubject_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendance_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedback_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedback_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeave_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeave_f)

        self.SendReply_b.clicked.connect(self.StaffReply_F)


        print(self.Access_ID2)

        mycurr = mydb.cursor()
        query = "SELECT Staff.Sf_Name, Sf_Feedback.Fdb_Message, Sf_Feedback.Fdb_Reply FROM Sf_Feedback INNER JOIN Staff ON Sf_Feedback.Sf_ID = Staff.Sf_ID WHERE Sf_FeedBack.Fdb_ID = %s"
        Fdb_ID = self.Access_ID2
        print("DD", Fdb_ID)
        values = [Fdb_ID]
        mycurr.execute(query, values)
        result = mycurr.fetchall()
        print(result)
        Sf_Name = result[0][0]
        self.Name_l_2.setText(Sf_Name)
        Fdb_Message = result[0][1]
        self.Feedback_tb.setText(Fdb_Message)
        Fdb_Reply = result[0][2]
        self.Reply_tb.setText(Fdb_Reply)

    def StaffReply_F(self):
        # SfName = self.Name_l_2.text()
        # FdbMessage = self.Feedback_tb.text()
        FdbReply = self.Reply_tb.toPlainText()
        query = "Update sf_feedback set Fdb_Reply = %s where  Fdb_ID = %s"
        values = [FdbReply, self.Access_ID2]
        cur = mydb.cursor()
        cur.execute(query, values)
        mydb.commit()

        Sf_Feedback = StaffFeedback()
        widget.addWidget(Sf_Feedback)
        widget.setCurrentIndex(widget.currentIndex() + 1)


##################################  STUDENT LEAVE PAGE  ##################################################
class StudentLeave(Get_ID, SideBar,QtWidgets.QMainWindow):
    def __init__(self):
        super(StudentLeave, self).__init__()
        loadUi("AdminStudentLeave.ui", self)
        self.Home_b.clicked.connect(self.Home)
        self.ManageStaff_b.clicked.connect(self.ManageStaff_f)
        self.AddStaff_b.clicked.connect(self.AddStaff_f)
        self.ManageStudent_b.clicked.connect(self.ManageStudent_f)
        self.AddStudent_b.clicked.connect(self.AddStudent_f)
        self.ManageCourse_b.clicked.connect(self.ManageCourse_f)
        self.AddCourse_b.clicked.connect(self.AddCourse_f)
        self.ManageSubject_b.clicked.connect(self.ManageSubject_f)
        self.AddSubject_b.clicked.connect(self.AddSubject_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendance_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedback_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedback_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeave_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeave_f)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr = mydb.cursor()
        query = "SELECT Student.St_Name, St_Leave.Leave_Date, St_Leave.Leave_Message, St_Leave.Leave_Status FROM St_Leave INNER JOIN Student ON St_Leave.St_ID = Student.St_ID"
        mycurr.execute(query)

        result = mycurr.fetchall()
        self.StudentLeave_t.setRowCount(0)
        for row_number, row_data in enumerate(result):
            # print(row_number)
            self.StudentLeave_t.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                # print(data)
                self.StudentLeave_t.setItem(row_number, column_number, QTableWidgetItem(str(data)))


        self.StudentLeave_t.cellClicked.connect(self.Get_Row)

    def Get_Row(self):
        try:
            rowCount = self.StudentLeave_t.rowCount()
            for row in range(rowCount):
                if self.StudentLeave_t.item(row, 0).isSelected():
                    rowNum = row + 1
                    self.Access_ID2 = rowNum
                    print(self.Access_ID2)
            self.Popup()

        except:
            print("Please click on match number.")

    def Popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Leave Confirmation")
        msg.setText("Do you want to allow this Leave Request ?")
        msg.setIcon(QMessageBox.Information)

        a = QPushButton("Accecpt", self)
        r = QPushButton("Reject", self)

        msg.addButton(a, msg.AcceptRole)
        msg.addButton(r, msg.RejectRole)

        x = msg.exec_()

        if x == msg.AcceptRole:
            print("Accepted")
            query = "UPDATE St_Leave set Leave_Status = %s WHERE Leave_ID = %s"
            values = ["Accepted", self.Access_ID2]
            print(values)
            cur = mydb.cursor()
            cur.execute(query, values)
            mydb.commit()

            StudentL = StudentLeave()
            widget.addWidget(StudentL)
            widget.setCurrentIndex(widget.currentIndex() + 1)


        elif x == msg.RejectRole:
            print("Rejected")
            query = "UPDATE St_Leave set Leave_Status = %s WHERE Leave_ID = %s"
            values = ["Rejected", self.Access_ID2]
            print(values)
            cur = mydb.cursor()
            cur.execute(query, values)
            mydb.commit()

            StudentL = StudentLeave()
            widget.addWidget(StudentL)
            widget.setCurrentIndex(widget.currentIndex() + 1)


##################################  STAFF LEAVE PAGE  ##################################################
class StaffLeave(Get_ID, SideBar,QtWidgets.QMainWindow):
    def __init__(self):
        super(StaffLeave, self).__init__()
        loadUi("AdminStaffLeave.ui", self)
        self.Home_b.clicked.connect(self.Home)
        self.ManageStaff_b.clicked.connect(self.ManageStaff_f)
        self.AddStaff_b.clicked.connect(self.AddStaff_f)
        self.ManageStudent_b.clicked.connect(self.ManageStudent_f)
        self.AddStudent_b.clicked.connect(self.AddStudent_f)
        self.ManageCourse_b.clicked.connect(self.ManageCourse_f)
        self.AddCourse_b.clicked.connect(self.AddCourse_f)
        self.ManageSubject_b.clicked.connect(self.ManageSubject_f)
        self.AddSubject_b.clicked.connect(self.AddSubject_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendance_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedback_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedback_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeave_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeave_f)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr = mydb.cursor()
        query = "SELECT Staff.Sf_Name, Sf_Leave.Leave_Date, Sf_Leave.Leave_Message, Sf_Leave.Leave_Status FROM Sf_Leave INNER JOIN Staff ON Sf_Leave.Sf_ID = Staff.Sf_ID"
        mycurr.execute(query)

        result = mycurr.fetchall()
        self.StaffLeave_t.setRowCount(0)
        for row_number, row_data in enumerate(result):
            #print(row_number)
            self.StaffLeave_t.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                #print(data)
                self.StaffLeave_t.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.StaffLeave_t.cellClicked.connect(self.Get_Row)

    def Get_Row(self):
        try:
            rowCount = self.StaffLeave_t.rowCount()
            for row in range(rowCount):
                if self.StaffLeave_t.item(row, 0).isSelected():
                    rowNum = row + 1
                    self.Access_ID2 = rowNum
                    print(self.Access_ID2)
            self.Popup()

        except:
            print("Please click on match number.")


    def Popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Leave Confirmation")
        msg.setText("Do you want to allow this Leave Request ?")
        msg.setIcon(QMessageBox.Information)

        a = QPushButton("Accecpt", self)
        r = QPushButton("Reject", self)

        msg.addButton(a, msg.AcceptRole)
        msg.addButton(r, msg.RejectRole)

        x = msg.exec_()

        if x == msg.AcceptRole:
            print("Accepted")
            query = "UPDATE Sf_Leave set Leave_Status = %s WHERE Leave_ID = %s"
            values = ["Accepted", self.Access_ID2]
            print(values)
            cur = mydb.cursor()
            cur.execute(query, values)
            mydb.commit()

            StaffL = StaffLeave()
            widget.addWidget(StaffL)
            widget.setCurrentIndex(widget.currentIndex() + 1)


        elif x == msg.RejectRole:
            print("Rejected")
            query = "UPDATE Sf_Leave set Leave_Status = %s WHERE Leave_ID = %s"
            values = ["Rejected", self.Access_ID2]
            print(values)
            cur = mydb.cursor()
            cur.execute(query, values)
            mydb.commit()

            StaffL = StaffLeave()
            widget.addWidget(StaffL)
            widget.setCurrentIndex(widget.currentIndex() + 1)

#########################################################################
#########################################################################
#                              Staff Section
#########################################################################
#########################################################################


class SideBarSf(QtWidgets.QMainWindow):
    def HomeSf(self):
        staffHP = StaffHome()
        widget.addWidget(staffHP)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def TakeAttendanceSf_f(self):
        AttendanceSf = TakeAttendanceSf_f()
        widget.addWidget(AttendanceSf)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def ViewAttendanceSf_f(self):
        TakeAttendance = UpdateAttendanceSf()
        widget.addWidget(TakeAttendance)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def StaffLeaveSf_f(self):
        LeaveSf = StaffLeaveSf()
        widget.addWidget(LeaveSf)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def StaffFeedbackSf_f(self):
        FeedbackSf = StaffFeedbackSf()
        widget.addWidget(FeedbackSf)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class StaffHome(Get_ID, SideBarSf, QtWidgets.QMainWindow):
    def __init__(self):
        super(StaffHome, self).__init__()
        loadUi("StaffHome.ui", self)
        self.TakeAttendance_b.clicked.connect(self.TakeAttendanceSf_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendanceSf_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeaveSf_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedbackSf_f)

        self.Logout_b.clicked.connect(self.Home_f)

        print(self.Access_ID)

    def Home_f(self):
        Logout = AdminLogin()
        widget.addWidget(Logout)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class TakeAttendanceSf_f(Get_ID, SideBarSf, QtWidgets.QMainWindow):
    def __init__(self):
        super(TakeAttendanceSf_f, self).__init__()
        loadUi("StaffTakeAttendance.ui", self)
        self.Home_b.clicked.connect(self.HomeSf)
        self.TakeAttendance_b.clicked.connect(self.TakeAttendanceSf_f)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendanceSf_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeaveSf_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedbackSf_f)
        self.SaveAttendance_b.clicked.connect(self.SaveAttd_F)

        values = [self.Access_ID]
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycur = mydb.cursor()
        query = "SELECT Sub_Name FROM Subject WHERE Sf_ID = %s"
        mycur.execute(query, values)

        Subjectlist = [row[0] for row in mycur.fetchall()]
        for i in Subjectlist:
            self.Subject_cmb.addItem(str(i))

        self.FetchAttendance_b.clicked.connect(self.FetchAttd_F)

        self.TakeAttendance_t.cellClicked.connect(self.Get_Row)

    def FetchAttd_F(self):
        date = self.StaffDateEdit_de.date()
        date2 = str(date.toPyDate())
        print(date2)
        print(type(date2))

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        Subject = self.Subject_cmb.currentText()
        query = "SELECT Sub_ID FROM Subject WHERE Sub_Name = %s"
        values = [Subject]
        cur = mydb.cursor()
        cur.execute(query, values)
        Sub_ID = cur.fetchone()

        # Creating a Attendance Record
        values = [Sub_ID[0], date2]
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycur = mydb.cursor()
        query = "INSERT INTO Attendance (Sub_ID, A_Date) VALUES (%s, %s)"
        mycur.execute(query, values)
        mydb.commit()

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        Subject = self.Subject_cmb.currentText()
        query = "SELECT C_ID FROM Subject WHERE Sub_Name = %s"
        values = [Subject]
        cur = mydb.cursor()
        cur.execute(query, values)
        C_ID = cur.fetchone()

        # Insert Student Record in AttendanceReport
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr = mydb.cursor()
        query = "SELECT St_ID From Student WHERE C_ID = %s"
        values = [C_ID[0]]
        print(values)
        mycurr.execute(query, values)
        result = mycurr.fetchall()

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr = mydb.cursor()
        query = "select * from Attendance WHERE A_Date = %s ORDER BY A_ID DESC LIMIT 1"
        values = [date2]
        mycurr = mydb.cursor()
        mycurr.execute(query, values)
        result1 = mycurr.fetchone()

        Get_ID.Access_ID2 = result1[0]

        for i in range(len(result)):
            values = [result1[0], result[i][0], 'NaN']
            print(values)


            mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
            mycur = mydb.cursor()
            query = "INSERT INTO AttendanceReport (A_ID, St_ID, AR_Status) VALUES (%s, %s, %s)"
            mycur.execute(query, values)
            mydb.commit()

            self.DisplayTable(result1[0])

    def DisplayTable(self, x):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr = mydb.cursor()
        values = [x]
        query = "SELECT Student.St_Name, AttendanceReport.AR_Status FROM AttendanceReport INNER JOIN Student ON AttendanceReport.St_ID = Student.St_ID WHERE AttendanceReport.A_ID = %s"
        mycurr.execute(query, values)

        table = mycurr.fetchall()

        print(len(table))
        self.TakeAttendance_t.setRowCount(0)
        for row_number, row_data in enumerate(table):
            # print(row_number)
            self.TakeAttendance_t.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                # print(data)
                self.TakeAttendance_t.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def Get_Row(self):
        try:
            rowCount = self.TakeAttendance_t.rowCount()
            for row in range(rowCount):
                if self.TakeAttendance_t.item(row, 0).isSelected():
                    print(self.TakeAttendance_t.item(row, 0).text())
                    Get_ID.Access_Name = self.TakeAttendance_t.item(row, 0).text()



            self.Popup()
        except:
            print("Please click on match number.")



    def Popup(self):

        query = "SELECT St_ID FROM Student WHERE St_Name = %s"
        values = [self.Access_Name]
        cur = mydb.cursor()
        cur.execute(query, values)
        result = cur.fetchone()

        msg = QMessageBox()
        msg.setWindowTitle("Attendance Record")
        msg.setText("Please mark the Attendance Status for {}".format(self.Access_Name))
        msg.setIcon(QMessageBox.Information)

        a = QPushButton("Present", self)
        r = QPushButton("Absent", self)

        msg.addButton(a, msg.AcceptRole)
        msg.addButton(r, msg.RejectRole)

        x = msg.exec_()

        if x == msg.AcceptRole:
            print("Marked Present")
            query = "UPDATE AttendanceReport set AR_Status = %s WHERE A_ID = %s AND St_ID = %s"
            values = ["Present", self.Access_ID2, result[0]]
            print(values)
            cur = mydb.cursor()
            cur.execute(query, values)
            mydb.commit()

            self.DisplayTable(self.Access_ID2)


        elif x == msg.RejectRole:
            print("Mark Absent")
            query = "UPDATE AttendanceReport set AR_Status = %s WHERE A_ID = %s AND St_ID = %s"
            values = ["Absent", self.Access_ID2, result[0]]
            print(values)
            cur = mydb.cursor()
            cur.execute(query, values)
            mydb.commit()

            self.DisplayTable(self.Access_ID2)
    def SaveAttd_F(self):
        AttendanceSf = TakeAttendanceSf_f()
        widget.addWidget(AttendanceSf)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class UpdateAttendanceSf(Get_ID, SideBarSf, QtWidgets.QMainWindow):
    def __init__(self):
        super(UpdateAttendanceSf, self).__init__()
        loadUi("StaffViewUpdateAttendance.ui", self)
        self.Home_b.clicked.connect(self.HomeSf)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendanceSf_f)
        self.TakeAttendance_b.clicked.connect(self.TakeAttendanceSf_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeaveSf_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedbackSf_f)

        self.EnterSubject_b.clicked.connect(self.GetDate_F)
        self.FetchAttendance_b.clicked.connect(self.FetchAttd_F)
        self.ViewAttendance_t.cellClicked.connect(self.Get_Row)
        self.SaveAttendance_b.clicked.connect(self.SaveAttd_F)

        print("1")

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycur = mydb.cursor()
        query = "SELECT Sub_Name FROM Subject WHERE Sf_ID = %s"
        values = [self.Access_ID]
        mycur.execute(query, values)

        Subjectlist = [row[0] for row in mycur.fetchall()]
        for i in Subjectlist:
            self.Subject_cmb.addItem(str(i))

    def GetDate_F(self):
        sub = self.Subject_cmb.currentText()
        print(sub)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycur = mydb.cursor()
        query = "SELECT Attendance.A_Date From Attendance INNER JOIN Subject ON Subject.Sub_ID = Attendance.Sub_ID WHERE Subject.Sub_Name = %s"
        values = [sub]
        mycur.execute(query, values)

        Datelist = [row[0] for row in mycur.fetchall()]
        self.Date_cmb.clear()
        for i in Datelist:
            self.Date_cmb.addItem(str(i))

    def FetchAttd_F(self):
        sub = self.Subject_cmb.currentText()
        date = self.Date_cmb.currentText()
        values = [sub, date]
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycur = mydb.cursor()
        query = "SELECT Student.St_name, AttendanceReport.AR_Status FROM (((AttendanceReport INNER JOIN Attendance ON AttendanceReport.A_ID = Attendance.A_ID) INNER JOIN Student ON Student.St_ID = AttendanceReport.St_ID) INNER JOIN Subject ON Subject.Sub_ID = Attendance.Sub_ID) WHERE Subject.Sub_Name = %s AND Attendance.A_Date = %s"
        mycur.execute(query, values)
        table = mycur.fetchall()
        print(table)

        self.ViewAttendance_t.setRowCount(0)
        for row_number, row_data in enumerate(table):
            # print(row_number)
            self.ViewAttendance_t.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                # print(data)
                self.ViewAttendance_t.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def Get_Row(self):
        try:
            rowCount = self.ViewAttendance_t.rowCount()
            for row in range(rowCount):
                if self.ViewAttendance_t.item(row, 0).isSelected():
                    print(self.ViewAttendance_t.item(row, 0).text())
                    Get_ID.Access_Name = self.ViewAttendance_t.item(row, 0).text()
            self.Popup()
        except:
            print("Please click on match number.")

    def Popup(self):

        sub = self.Subject_cmb.currentText()
        date = self.Date_cmb.currentText()
        values = [date, sub]
        query = "SELECT Attendance.A_ID FROM Attendance INNER JOIN Subject ON Attendance.Sub_ID = Subject.Sub_ID WHERE A_Date = %s AND SUB_Name = %s"
        cur = mydb.cursor()
        cur.execute(query, values)
        result = cur.fetchone()


        query = "SELECT St_ID FROM Student WHERE St_Name = %s"
        values = [self.Access_Name]
        cur = mydb.cursor()
        cur.execute(query, values)
        result1 = cur.fetchone()

        msg = QMessageBox()
        msg.setWindowTitle("Attendance Record")
        msg.setText("Please mark the Attendance Status for {}".format(self.Access_Name))
        msg.setIcon(QMessageBox.Information)

        a = QPushButton("Present", self)
        r = QPushButton("Absent", self)

        msg.addButton(a, msg.AcceptRole)
        msg.addButton(r, msg.RejectRole)

        x = msg.exec_()

        if x == msg.AcceptRole:
            print("Marked Present")
            query = "UPDATE AttendanceReport set AR_Status = %s WHERE A_ID = %s AND St_ID = %s"
            values = ["Present", result[0], result1[0]]
            print(values)
            cur = mydb.cursor()
            cur.execute(query, values)
            mydb.commit()

            self.FetchAttd_F()

        elif x == msg.RejectRole:
            print("Mark Absent")
            query = "UPDATE AttendanceReport set AR_Status = %s WHERE A_ID = %s AND St_ID = %s"
            values = ["Absent", result[0], result1[0]]
            print(values)
            cur = mydb.cursor()
            cur.execute(query, values)
            mydb.commit()

            self.FetchAttd_F()

    def SaveAttd_F(self):
        TakeAttendance = UpdateAttendanceSf()
        widget.addWidget(TakeAttendance)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class StaffLeaveSf(Get_ID, SideBarSf, QtWidgets.QMainWindow):
    def __init__(self):
        print("kapil")
        super(StaffLeaveSf, self).__init__()
        loadUi("StaffApplyLeave.ui", self)
        self.Home_b.clicked.connect(self.HomeSf)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendanceSf_f)
        self.TakeAttendance_b.clicked.connect(self.TakeAttendanceSf_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeaveSf_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedbackSf_f)

        self.ApplyForLeave_b.clicked.connect(self.ApplyForLeave_Sf)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr = mydb.cursor()
        query = "SELECT Leave_ID, Leave_Date, Leave_Message, Leave_Status FROM Sf_Leave"
        mycurr.execute(query)

        result = mycurr.fetchall()
        self.LeaveHistory_t.setRowCount(0)
        for row_number, row_data in enumerate(result):
            #print(row_number)
            self.LeaveHistory_t.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                #print(data)
                self.LeaveHistory_t.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def ApplyForLeave_Sf(self):
        date = self.LeaveApplyDateEdit_de.date()
        date2 = str(date.toPyDate())
        print(date2)
        print(type(date2))
        Reason = self.LeaveReason_te.toPlainText()
        values = (self.Access_ID, date2, Reason)

        print(values)

        query = "INSERT INTO Sf_Leave(Sf_ID, Leave_Date, Leave_Message) VALUES(%s, %s, %s)"

        cur = mydb.cursor()
        cur.execute(query, values)
        mydb.commit()

        LeaveSf = StaffLeaveSf()
        widget.addWidget(LeaveSf)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class StaffFeedbackSf(Get_ID, SideBarSf, QtWidgets.QMainWindow):
    def __init__(self):
        super(StaffFeedbackSf, self).__init__()
        loadUi("StaffFeedback.ui", self)
        self.Home_b.clicked.connect(self.HomeSf)

        self.ViewAttendance_b.clicked.connect(self.ViewAttendanceSf_f)
        self.TakeAttendance_b.clicked.connect(self.TakeAttendanceSf_f)
        self.StaffLeave_b.clicked.connect(self.StaffLeaveSf_f)
        self.StaffFeedback_b.clicked.connect(self.StaffFeedbackSf_f)

        self.EnterFeedback_b.clicked.connect(self.FeedbackAdd_Sf)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr = mydb.cursor()
        query = "SELECT Fdb_Message, Fdb_Reply FROM Sf_Feedback"
        mycurr.execute(query)

        result = mycurr.fetchall()
        self.FeedbackHistory_t.setRowCount(0)
        for row_number, row_data in enumerate(result):
            print(row_number)
            self.FeedbackHistory_t.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                print(data)
                self.FeedbackHistory_t.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def FeedbackAdd_Sf(self):
        Message = self.FeedbackText_te.toPlainText()
        query = "INSERT INTO Sf_Feedback(Sf_ID, Fdb_Message) VALUES(%s, %s)"

        values = (self.Access_ID, Message)

        cur = mydb.cursor()
        cur.execute(query, values)
        mydb.commit()

        FeedbackSf = StaffFeedbackSf()
        widget.addWidget(FeedbackSf)
        widget.setCurrentIndex(widget.currentIndex() + 1)

#########################################################################
#########################################################################
#                              Student Section
#########################################################################
#########################################################################

class SideBarSt(QtWidgets.QMainWindow):


    def HomeSt(self):
        studentHP = StudentHome()
        widget.addWidget(studentHP)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def ViewAttendanceSt_f(self):
        AttendanceSt = ViewAttendanceSt()
        widget.addWidget(AttendanceSt)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def StudentFeedbackSt_f(self):
        FeedbackSt = StudentFeedbackSt()
        widget.addWidget(FeedbackSt)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def StudentLeaveSt_f(self):
        LeaveSt = StudentLeaveSt()
        widget.addWidget(LeaveSt)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class StudentHome(Get_ID, SideBarSt, QtWidgets.QMainWindow):
    def __init__(self):
        super(StudentHome, self).__init__()
        loadUi("StudentHome.ui", self)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendanceSt_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedbackSt_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeaveSt_f)
        self.ViewUpdateAttendanceLogout_b.clicked.connect(self.Home_f)

        print(self.Access_ID)

    def Home_f(self):
        Logout = AdminLogin()
        widget.addWidget(Logout)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ViewAttendanceSt(Get_ID, SideBarSt, QtWidgets.QMainWindow):
    def __init__(self):
        super(ViewAttendanceSt, self).__init__()
        loadUi("StudentViewAttendance.ui", self)
        self.Home_b.clicked.connect(self.HomeSt)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendanceSt_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedbackSt_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeaveSt_f)

        self.FetchAttendance_b.clicked.connect(self.FetchAttdSt_F)

        values = [self.Access_ID]
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycur = mydb.cursor()
        query = "SELECT Subject.Sub_Name FROM ((Subject INNER JOIN Course ON Subject.C_ID = Course.C_ID) INNER JOIN Student ON Course.C_ID = Student.C_ID) WHERE St_ID = %s"
        mycur.execute(query, values)

        Subjectlist = [row[0] for row in mycur.fetchall()]

        for i in Subjectlist:
            self.Subject_cmb.addItem(str(i))

    def FetchAttdSt_F(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr = mydb.cursor()
        Subject = self.Subject_cmb.currentText()
        values = [self.Access_ID, Subject]
        print(values)
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        cur = mydb.cursor()
        query = "SELECT Attendance.A_Date, AttendanceReport.AR_Status FROM ((AttendanceReport INNER JOIN Attendance ON AttendanceReport.A_ID = Attendance.A_ID) INNER JOIN Subject ON Attendance.Sub_ID = Subject.Sub_ID) WHERE AttendanceReport.St_ID = %s AND Subject.Sub_Name = %s"
        cur.execute(query, values)

        table = cur.fetchall()
        print(table)

        self.TakeAttendance_t.setRowCount(0)
        for row_number, row_data in enumerate(table):
            # print(row_number)
            self.TakeAttendance_t.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                # print(data)
                self.TakeAttendance_t.setItem(row_number, column_number, QTableWidgetItem(str(data)))


class StudentFeedbackSt(Get_ID, SideBarSt, QtWidgets.QMainWindow):
    def __init__(self):
        super(StudentFeedbackSt, self).__init__()
        loadUi("StudentFeedback.ui", self)
        self.Home_b.clicked.connect(self.HomeSt)

        self.ViewAttendance_b.clicked.connect(self.ViewAttendanceSt_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedbackSt_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeaveSt_f)

        self.EnterFeedback_b.clicked.connect(self.FeedbackAdd_St)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr = mydb.cursor()
        query = "SELECT Fdb_Message, Fdb_Reply FROM St_Feedback"
        mycurr.execute(query)

        result = mycurr.fetchall()
        self.FeedbackHistory_t.setRowCount(0)
        for row_number, row_data in enumerate(result):
            print(row_number)
            self.FeedbackHistory_t.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                print(data)
                self.FeedbackHistory_t.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def FeedbackAdd_St(self):

        Message = self.FeedbackText_te.toPlainText()
        query = "INSERT INTO St_Feedback(St_ID, Fdb_Message) VALUES(%s, %s)"
        values = (self.Access_ID, Message)
        cur = mydb.cursor()
        cur.execute(query, values)
        mydb.commit()

        FeedbackSt = StudentFeedbackSt()
        widget.addWidget(FeedbackSt)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class StudentLeaveSt(Get_ID, SideBarSt, QtWidgets.QMainWindow):
    def __init__(self):
        super(StudentLeaveSt, self).__init__()
        loadUi("StudentApplyLeave.ui", self)
        self.Home_b.clicked.connect(self.HomeSt)
        self.ViewAttendance_b.clicked.connect(self.ViewAttendanceSt_f)
        self.StudentFeedback_b.clicked.connect(self.StudentFeedbackSt_f)
        self.StudentLeave_b.clicked.connect(self.StudentLeaveSt_f)

        self.ApplyForLeave_b.clicked.connect(self.ApplyForLeave_St)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="STMS")
        mycurr = mydb.cursor()
        query = "SELECT Leave_ID, Leave_Date, Leave_Message, Leave_Status FROM St_Leave"
        mycurr.execute(query)

        result = mycurr.fetchall()
        self.LeaveHistory_t.setRowCount(0)
        for row_number, row_data in enumerate(result):
            print(row_number)
            self.LeaveHistory_t.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                print(data)
                self.LeaveHistory_t.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def ApplyForLeave_St(self):
        date = self.LeaveApplyDateEdit_de.date()
        date2 = str(date.toPyDate())
        print(date2)
        print(type(date2))
        Reason = self.LeaveReason_te.toPlainText()
        values = (self.Access_ID, date2, Reason)

        print(values)

        query = "INSERT INTO St_Leave(St_ID, Leave_Date, Leave_Message) VALUES(%s, %s, %s)"

        cur = mydb.cursor()
        cur.execute(query, values)
        mydb.commit()

        LeaveSt = StudentLeaveSt()
        widget.addWidget(LeaveSt)
        widget.setCurrentIndex(widget.currentIndex() + 1)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainwindow = AdminLogin()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(1920)
    widget.setFixedHeight(1029)
    widget.show()
    app.exec_()