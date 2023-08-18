import sys
import random
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox, QLineEdit
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.uic import loadUi
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Best@276", database="IPL")
mycursor = mydb.cursor()


##################################  MAIN PAGE  ##################################################
class MainClass(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainClass, self).__init__()
        loadUi("tourn1.ui", self)
        self.register_button.clicked.connect(self.Open_register)
        self.signin_button.clicked.connect(self.Open_signin)

    def Open_register(self):
        register = Register()
        widget.addWidget(register)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Open_signin(self):
        signin = Signin()
        widget.addWidget(signin)
        widget.setCurrentIndex(widget.currentIndex() + 1)


##########################################  REGISTER PAGE  ################################################
class Register(QtWidgets.QMainWindow):
    def __init__(self):
        super(Register, self).__init__()
        loadUi("tourn2.ui", self)
        self.pushButton_back.clicked.connect(self.Open_back)
        self.Button_register.clicked.connect(self.record_registration)

    def Open_back(self):
        back_to_main = MainClass()
        widget.addWidget(back_to_main)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def record_registration(self):

        uid = self.lineEdit_uid.text()
        name = self.lineEdit_name.text()
        email = self.lineEdit_email.text()
        contact = self.lineEdit_contact.text()
        if self.lineEdit_password.text() == self.lineEdit_cpassword.text():
            password = self.textEdit_password.text()
        else:
            self.passwd_error()

        if self.RB_admin.isChecked():
            query = "INSERT INTO admin (AdminId,Name,Email_ID,Contact_no,Password) VALUES (%s,%s,%s,%s,%s)"
        elif self.RB_owner.isChecked():
            query = "INSERT INTO owner (OwnerId,Name,Email_ID,Contact_no,Password) VALUES (%s,%s,%s,%s,%s)"
        elif self.RB_generaluser.isChecked():
            query = "INSERT INTO generaluser (UserId,Name,Email_ID,Contact_no,Password) VALUES (%s,%s,%s,%s,%s)"
        else:
            # self.passwd_error()
            pass

        value = (uid, name, email, contact, password)
        mycursor.execute(query, value)
        mydb.commit()
        print("Account successfully created with user_id :", uid)

        signin_page_open = Signin()
        widget.addWidget(signin_page_open)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def passwd_error(self):
        print("Password not matching!")
        msg = QMessageBox()
        msg.setWindowTitle("Error message!")
        msg.setText("Password not matching!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()


#########################################  SIGN IN PAGE  ############################################
class Signin(QtWidgets.QMainWindow):
    def __init__(self):
        super(Signin, self).__init__()
        loadUi("tourn3.ui", self)
        self.pushButton_back.clicked.connect(self.Open_back)
        self.pushButton_login.clicked.connect(self.record_signin)

    def record_signin(self):
        print("Sign in Button clicked successfully!")
        uid = self.lineEdit_uid.text()
        password = self.lineEdit_password.text()

        cur = mydb.cursor()

        if self.RB_admin.isChecked():
            query = "SELECT * FROM admin WHERE AdminID=%s and Password=%s"
        elif self.RB_owner.isChecked():
            query = "SELECT * FROM owner WHERE OwnerID=%s and Password=%s"
        elif self.RB_generaluser.isChecked():
            query = "SELECT * FROM generaluser WHERE UserID=%s and Password=%s"
        else:
            # self.passwd_error()
            pass

        exe = cur.execute(query, (uid, password))

        if (len(cur.fetchall()) > 0):
            if self.RB_admin.isChecked():
                HomePage_A = AdminHP()
                widget.addWidget(HomePage_A)
                widget.setCurrentIndex(widget.currentIndex() + 1)

            elif self.RB_owner.isChecked():
                HomePage_O = OwnerHP()
                widget.addWidget(HomePage_O)
                widget.setCurrentIndex(widget.currentIndex() + 1)

            elif self.RB_generaluser.isChecked():
                HomePage_U = GeneralUserHP()
                widget.addWidget(HomePage_U)
                widget.setCurrentIndex(widget.currentIndex() + 1)

            else:
                pass

            print("Successfully logged in")
        else:
            print("Fields doenst match! Try Again.")

    def Open_back(self):
        back_to_main = MainClass()
        widget.addWidget(back_to_main)
        widget.setCurrentIndex(widget.currentIndex() + 1)


##########################################  ADMIN HOME PAGE  #############################################
class AdminHP(QtWidgets.QMainWindow):
    def __init__(self):
        super(AdminHP, self).__init__()
        loadUi("tourn4a.ui", self)
        self.pushButton_logout.clicked.connect(self.Logout)
        self.pushButton_teams.clicked.connect(self.Open_teamsA)
        self.pushButton_players.clicked.connect(self.Open_PlayersA)
        self.pushButton_pt.clicked.connect(self.Open_PointsTableA)

        self.pushButton_schedule.clicked.connect(self.Open_ScheduleA)
        self.pushButton_auction.clicked.connect(self.Open_Auction)

    def Logout(self):
        back_to_main = MainClass()
        widget.addWidget(back_to_main)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Open_teamsA(self):
        openA = TEAMS_A()
        widget.addWidget(openA)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Open_PlayersA(self):
        openPlayers = Players_A()
        widget.addWidget(openPlayers)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Open_PointsTableA(self):
        openPointsTable = PointsTable_A()
        widget.addWidget(openPointsTable)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Open_ScheduleA(self):
        openSchedule = Schedule_A()
        widget.addWidget(openSchedule)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Open_Auction(self):
        msg = QMessageBox()
        msg.setWindowTitle("Action can't performed!")
        msg.setText("Auction page is currently under maintenance!")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()


##########################################  OWNER HOME PAGE  #############################################
class OwnerHP(QtWidgets.QMainWindow):
    def __init__(self):
        super(OwnerHP, self).__init__()
        loadUi("tourn4o.ui", self)
        self.pushButton_logout.clicked.connect(self.Logout)
        self.pushButton_teams.clicked.connect(self.Connect_to_teamsOU)
        self.pushButton_players.clicked.connect(self.Open_PlayersA)
        self.pushButton_pt.clicked.connect(self.Open_PointsTableA)
        self.pushButton_schedule.clicked.connect(self.Open_ScheduleA)
        self.pushButton_auction.clicked.connect(self.Open_Auction)

    def Logout(self):
        back_to_main = MainClass()
        widget.addWidget(back_to_main)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Connect_to_teamsOU(self):
        teamsOU = TEAMS_OU('Owner')
        widget.addWidget(teamsOU)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Open_PlayersA(self):
        openPlayers = Players_OU('Owner')
        widget.addWidget(openPlayers)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Open_PointsTableA(self):
        openPointsTable = PointsTable_OU('Owner')
        widget.addWidget(openPointsTable)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Open_ScheduleA(self):
        openSchedule = Schedule_OU('Owner')
        widget.addWidget(openSchedule)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Open_Auction(self):
        msg = QMessageBox()
        msg.setWindowTitle("Action can't performed!")
        msg.setText("Auction page is currently under maintenance!")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()


###################################### GENERAL USER HOME PAGE  ############################################
class GeneralUserHP(QtWidgets.QMainWindow):
    def __init__(self):
        super(GeneralUserHP, self).__init__()
        loadUi("tourn4u.ui", self)
        self.pushButton_logout.clicked.connect(self.Logout)
        self.pushButton_teams.clicked.connect(self.Connect_to_teamsOU)
        self.pushButton_players.clicked.connect(self.Open_PlayersOU)
        self.pushButton_pt.clicked.connect(self.Open_PointsTableOU)
        self.pushButton_schedule.clicked.connect(self.Open_ScheduleOU)

    def Logout(self):
        back_to_main = MainClass()
        widget.addWidget(back_to_main)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Connect_to_teamsOU(self):
        teamsOU = TEAMS_OU('GeneralUser')
        widget.addWidget(teamsOU)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Open_PlayersOU(self):
        openPlayers = Players_OU('GeneralUser')
        widget.addWidget(openPlayers)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Open_PointsTableOU(self):
        openPointsTable = PointsTable_OU('GeneralUser')
        widget.addWidget(openPointsTable)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Open_ScheduleOU(self):
        openSchedule = Schedule_OU('GeneralUser')
        widget.addWidget(openSchedule)
        widget.setCurrentIndex(widget.currentIndex() + 1)


###################################### TEAMS ADMIN PAGE  ############################################
class TEAMS_A(QtWidgets.QMainWindow):
    def __init__(self):
        super(TEAMS_A, self).__init__()
        loadUi("teamsA.ui", self)
        self.pushButton_back.clicked.connect(self.Home)
        self.pushButton_update.clicked.connect(self.Update)

        # displayquery = "SELECT Team,Owner,Captian,Coach,Home_Ground FROM Team"
        # self.tableWidget_teamA.setRowCount(50)
        # tablerow = 0
        # for row in mycurr.execute(displayquery):
        # 	self.tableWidget_teamA.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
        # 	self.tableWidget_teamA.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[0]))
        # 	self.tableWidget_teamA.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[0]))
        # 	self.tableWidget_teamA.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[0]))
        # 	self.tableWidget_teamA.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[0]))
        # 	tablerow+=1

        try:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Best@276", database="IPL")
            mycurr = mydb.cursor()
            # mycurr.execute("SELECT Team,Owner,Captian,Coach,Home_Ground FROM {}".format(team))
            mycurr.execute("SELECT Team,Owner,Captian,Coach,Home_Ground FROM team")

            result = mycurr.fetchall()
            self.tableWidget_teamA.setRowCount(0)
            for row_number, row_data in enumerate(result):
                print(row_number)
                self.tableWidget_teamA.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget_teamA.setItem(row_number, column_number, QTableWidgetItem(str(data)))

            mydb.commit()

        except:
            print("Cannot display Teams Table")

    def Home(self):
        backbutton = AdminHP()
        widget.addWidget(backbutton)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Update(self):
        try:
            mycurr = mydb.cursor()
            rowCount = self.tableWidget_teamA.rowCount()
            print(rowCount)
            columnCount = self.tableWidget_teamA.columnCount()
            print(columnCount)
            for row in range(rowCount):
                rowNum = row + 1
                rowData = []
                for column in range(columnCount):
                    widgetItem = self.tableWidget_teamA.item(row, column)
                    if (widgetItem and widgetItem.text()):
                        rowData.append(widgetItem.text())
                    else:
                        rowData.append('NULL')
                rowData.append(rowNum)
                print(rowData)
                # query = "INSERT INTO Team (Team, Owner, Captian, Coach, Home_Ground) VALUES(%s, %s, %s, %s, %s)"
                query = "UPDATE Team SET Team = %s, Owner = %s, Captian = %s, Coach = %s, Home_Ground = %s WHERE Team_ID = %s"
                mycurr.execute(query, rowData)
            mydb.commit()

            msg = QMessageBox()
            msg.setWindowTitle("Success!")
            msg.setText("Teams Table Updated Successfully!")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()

        except:
            msg = QMessageBox()
            msg.setWindowTitle("Information!")
            msg.setText("Data Insertion Failed!")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()


# TeamID = [self.tableWidget_teamA.item(row,0).text() for row in range(self.tableWidget_teamA)]


###################################### TEAMS OWNER/GEN.USER PAGE  ############################################
class TEAMS_OU(QtWidgets.QMainWindow):
    def __init__(self, s):
        super(TEAMS_OU, self).__init__()
        loadUi("teamsOU.ui", self)
        self.UserType = s
        print(self.UserType)
        self.pushButton_back.clicked.connect(self.Back_to_HP)

        # try:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Best@276", database="IPL")
        mycurr = mydb.cursor()
        # mycurr.execute("SELECT Team,Owner,Captian,Coach,Home_Ground FROM {}".format(team))
        mycurr.execute("SELECT Owner,Captian,Coach,Home_Ground FROM team")

        result = mycurr.fetchall()
        self.tableWidget_teamsOU.setRowCount(0)
        for row_number, row_data in enumerate(result):
            print(row_number)
            self.tableWidget_teamsOU.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_teamsOU.setItem(row_number, column_number + 1, QTableWidgetItem(str(data)))

        mydb.commit()

    # except:
    # 	print("Unable to display table content")

    def Back_to_HP(self):
        if self.UserType == 'Owner':
            back = OwnerHP()
        else:
            back = GeneralUserHP()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)


##################################  PLAYERS ADMIN PAGE  ##################################################
class Players_A(QtWidgets.QMainWindow):
    def __init__(self):
        super(Players_A, self).__init__()
        loadUi("PlayersA.ui", self)
        self.pushButton_back.clicked.connect(self.Home)
        self.pushButton_update.clicked.connect(self.Update)

    def Home(self):
        backbutton = AdminHP()
        widget.addWidget(backbutton)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Update(self):
        msg = QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setText("Players Data Updated Successfully!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()


###################################### PLAYERS OWNER/GEN.USER PAGE  ############################################
class Players_OU(QtWidgets.QMainWindow):
    def __init__(self, s):
        super(Players_OU, self).__init__()
        loadUi("PlayersOU.ui", self)
        self.UserType = s
        self.pushButton_back.clicked.connect(self.Back_to_HP)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Best@276", database="IPL")
        mycurr = mydb.cursor()
        # mycurr.execute("SELECT Team,Owner,Captian,Coach,Home_Ground FROM {}".format(team))
        mycurr.execute("SELECT Name,Team,Role,Matches,Runs,Wickets FROM Player")

        result = mycurr.fetchall()
        self.tableWidget_playersOU.setRowCount(0)
        for row_number, row_data in enumerate(result):
            print(row_number)
            self.tableWidget_playersOU.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_playersOU.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        mydb.commit()

    def Back_to_HP(self):
        if self.UserType == 'Owner':
            back = OwnerHP()
        else:
            back = GeneralUserHP()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)


##################################  POINTS TABLE ADMIN PAGE  ##################################################
class PointsTable_A(QtWidgets.QMainWindow):
    def __init__(self):
        super(PointsTable_A, self).__init__()
        loadUi("PointsTable_A.ui", self)
        self.pushButton_back.clicked.connect(self.Home)
        # self.pushButton_qualifier.setVisible(False)
        self.pushButton_update.clicked.connect(self.Update)
        self.pushButton_qualifier.clicked.connect(self.Qualifier)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Best@276", database="IPL")
        mycurr = mydb.cursor()
        mycursor = mydb.cursor()
        # mycurr.execute("SELECT Team,Owner,Captian,Coach,Home_Ground FROM {}".format(team))
        mycurr.execute("SELECT Team_name,Matches,Won,Lost,Points FROM PointsTable ORDER BY Points DESC")

        result = mycurr.fetchall()
        self.tableWidget_PTA.setRowCount(0)
        for row_number, row_data in enumerate(result):
            print(row_number)
            self.tableWidget_PTA.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_PTA.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        mycursor.execute("Select Sum(Matches) From PointsTable")
        result = mycursor.fetchone()

        mydb.commit()

        matches = result[0]

        if matches == 112.0:
            print("Successful 112")
            self.pushButton_qualifier.setVisible(True)
        else:
            print("Failed to load value")
            self.pushButton_qualifier.setVisible(False)

    def Home(self):
        backbutton = AdminHP()
        widget.addWidget(backbutton)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Update(self):
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Best@276", database="IPL")
            mycurr = mydb.cursor()
            rowCount = self.tableWidget_PTA.rowCount()
            print(rowCount)
            columnCount = self.tableWidget_PTA.columnCount()
            print(columnCount)

            c = mydb.cursor()
            # for i in range(rowCount):
            TeamId = []
            c.execute("Select Team_ID from PointsTable ORDER BY Points")
            result = c.fetchall()
            # TeamId.append(result)
            for row in result:
                TeamId.append(row[0])
            mydb.commit()
            print(TeamId)
            print(TeamId[1])

            for row in range(rowCount):
                rowData = []
                for column in range(columnCount):
                    widgetItem = self.tableWidget_PTA.item(row, column)
                    if (widgetItem and widgetItem.text()):
                        rowData.append(widgetItem.text())
                    else:
                        rowData.append('NULL')
                rowData.append(TeamId[row])
                print(rowData)
                # query = "INSERT INTO Team (Team, Owner, Captian, Coach, Home_Ground) VALUES(%s, %s, %s, %s, %s)"
                # (SELECT Team_ID from PointsTable WHERE @row_number:= %s)
                query = "UPDATE PointsTable SET Team_name = %s, Matches = %s, Won = %s, Lost = %s, Points = %s WHERE Team_ID = %s"
                mycurr.execute(query, rowData)
            mydb.commit()

            msg = QMessageBox()
            msg.setWindowTitle("Success!")
            msg.setText("Points Table Updated Successfully!")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()

            db = mysql.connector.connect(host="localhost", user="root", passwd="Best@276", database="IPL")
            mycursor = db.cursor()
            mycursor.execute("Select Sum(Matches) From PointsTable")
            result = mycursor.fetchone()
            db.commit()

            print(result)
            print(type(result))
            matches = result[0]
            print(type(matches))
            print(matches)
            # string1 = " "
            # matches = ' '.join(map(str,result))
            # print(matches)
            # print(type(matches))

            # a = matches.
            # matches = result(0)
            # if matches == 112.0:
            # 	print("Successful 112")
            # 	self.pushButton_qualifier.setVisible(True)
            # else:
            # 	print("Failed to load value")

            call_page_again = PointsTable_A()
            widget.addWidget(call_page_again)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Warning!")
            msg.setText("Please fill all the fields!")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()

    def Qualifier(self):
        qualifier = Qualifier_A()
        widget.addWidget(qualifier)
        widget.setCurrentIndex(widget.currentIndex() + 1)


###################################### POINTS TABLE OWNER/GEN.USER PAGE  ############################################
class PointsTable_OU(QtWidgets.QMainWindow):
    def __init__(self, s):
        super(PointsTable_OU, self).__init__()
        loadUi("PointsTable_OU.ui", self)
        self.UserType = s
        self.pushButton_back.clicked.connect(self.Back_to_HP)
        self.pushButton_qualifier.clicked.connect(self.Qualifier)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Best@276", database="IPL")
        mycursor = mydb.cursor()
        mycursor.execute("Select Sum(Matches) From PointsTable")
        result = mycursor.fetchone()
        mydb.commit()

        matches = result[0]
        if matches == 112.0:
            print("Successful 112")
            self.pushButton_qualifier.setVisible(True)
        else:
            print("Failed to load value")
            self.pushButton_qualifier.setVisible(False)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Best@276", database="IPL")
        mycurr = mydb.cursor()
        # mycurr.execute("SELECT Team_name,Matches,Won,Lost,Tied,Points FROM {}".format(team))
        mycurr.execute("SELECT Team_name,Matches,Won,Lost,Points FROM pointstable")

        result = mycurr.fetchall()
        self.tableWidget_PTOU.setRowCount(0)
        for row_number, row_data in enumerate(result):
            print(row_number)
            self.tableWidget_PTOU.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_PTOU.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        mydb.commit()

    def Back_to_HP(self):
        if self.UserType == 'Owner':
            back = OwnerHP()
        else:
            back = GeneralUserHP()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Qualifier(self):
        qualifier = Qualifier_OU(self.UserType)
        widget.addWidget(qualifier)
        widget.setCurrentIndex(widget.currentIndex() + 1)


##################################  SCHEDULE TABLE ADMIN PAGE  ##################################################
class Schedule_A(QtWidgets.QMainWindow):
    def __init__(self):
        super(Schedule_A, self).__init__()
        loadUi("Schedule_A.ui", self)
        self.pushButton_back.clicked.connect(self.Home)
        self.pushButton_update.clicked.connect(self.Update)
        # self.pushButton_st.setEnabled(False)
        self.pushButton_st.clicked.connect(self.SchTournament)

        ########################Displaying Table##############################
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Best@276", database="IPL")
        mycurr = mydb.cursor()
        # mycurr.execute("SELECT Team_name,Matches,Won,Lost,Tied,Points FROM {}".format(team))
        mycurr.execute("SELECT Match_no,Day,Date,Time,Venue,Team_1,Team_2 FROM schedule")

        result = mycurr.fetchall()
        self.tableWidget_scheduleA.setRowCount(0)
        for row_number, row_data in enumerate(result):
            print(row_number)
            self.tableWidget_scheduleA.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_scheduleA.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        mydb.commit()

    #####################################################################

    def Home(self):
        backbutton = AdminHP()
        widget.addWidget(backbutton)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Update(self):
        msg = QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setText("Schedule Table Updated Successfully!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def SchTournament(self):
        # back_to_main = MainClass()
        # widget.addWidget(back_to_main)
        # widget.setCurrentIndex(widget.currentIndex()+1)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Best@276", database="IPL")
        mycurr = mydb.cursor()

        team_1 = 'MI'
        team_2 = 'CSK'
        team_3 = 'RCB'
        team_4 = 'DC'
        team_5 = 'SRH'
        team_6 = 'PBKS'
        team_7 = 'RR'
        team_8 = 'KKR'
        time = '7:30 pm IST'

        TeamName = {team_1, team_2, team_3, team_4, team_5, team_6, team_7, team_8}
        Teamlist = list(TeamName)
        # Teamlist = [team_1,team_2,team_3,team_4,team_5,team_6,team_7,team_8]

        # NoOfTeams = len(Teamlist)
        NoOfTeams = 8
        # rowCount = (NoOfTeams)*(NoOfTeams - 1)/2
        # columnCount = self.tableWidget_scheduleA.columnCount()
        # print(columnCount)

        for row in range(NoOfTeams - 1):
            # rowNum = row + 1
            # rowData = []
            for column in range(row + 1, NoOfTeams):
                query = "INSERT INTO Schedule (Time, Team_1, Team_2) VALUES (%s, %s, %s)"
                data = (time, Teamlist[row], Teamlist[column])
                # query = "UPDATE Team SET Team = %s, Owner = %s, Captian = %s, Coach = %s, Home_Ground = %s WHERE Team_ID = %s"
                mycurr.execute(query, data)
        mydb.commit()

        # for(i=0;i<no_of_teams-1;i++)
        #           {
        #                   for(j=i+1;j<no_of_teams;j++)
        #                   {
        #                       String tourn_id;
        #                       tourn_id = tournamentthree.jTextField37.getText();
        # 	//System.out.println("Match "+a+":   "+teamname.get(i)+"   v/s   "+teamname.get(j));
        # 	String Input = ("insert into schedule(Tournament_id,Team_1,Team_2) values('"+tourn_id+"','"+teamname.get(i)+"','"+teamname.get(j)+"');");

        #                       ps.execute(Input);
        #                   }
        #           }

        msg = QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setText("Tournament Scheduled Successfully!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

        updatepage = Schedule_A()
        widget.addWidget(updatepage)
        widget.setCurrentIndex(widget.currentIndex() + 1)


###################################### SCHEDULE TABLE OWNER/GEN.USER PAGE  ############################################
class Schedule_OU(QtWidgets.QMainWindow):
    def __init__(self, s):
        super(Schedule_OU, self).__init__()
        loadUi("Schedule_OU.ui", self)
        self.UserType = s
        self.pushButton_back.clicked.connect(self.Back_to_HP)

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Best@276", database="IPL")
        mycurr = mydb.cursor()
        # mycurr.execute("SELECT Team_name,Matches,Won,Lost,Tied,Points FROM {}".format(team))
        mycurr.execute("SELECT Match_no,Day,Date,Time,Venue,Team_1,Team_2 FROM schedule")

        result = mycurr.fetchall()
        self.tableWidget_scheduleOU.setRowCount(0)
        for row_number, row_data in enumerate(result):
            print(row_number)
            self.tableWidget_scheduleOU.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_scheduleOU.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        mydb.commit()

    def Back_to_HP(self):
        if self.UserType == 'Owner':
            back = OwnerHP()
        else:
            back = GeneralUserHP()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)


##################################  QUALIFIER TABLE ADMIN PAGE  ##################################################
class Qualifier_A(QtWidgets.QMainWindow):
    def __init__(self):
        super(Qualifier_A, self).__init__()
        loadUi("Qualifier_A.ui", self)
        self.pushButton_back.clicked.connect(self.Home)
        self.pushButton_update.clicked.connect(self.Update)
        self.pushButton_final.clicked.connect(self.Final)

    def Home(self):
        backbutton = PointsTable_A()
        widget.addWidget(backbutton)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Update(self):
        msg = QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setText("Qualifier Table Updated Successfully!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def Final(self):
        final_button = Final_A()
        widget.addWidget(final_button)
        widget.setCurrentIndex(widget.currentIndex() + 1)


###################################### QUALIFIER TABLE OWNER/GEN.USER PAGE  ############################################
class Qualifier_OU(QtWidgets.QMainWindow):
    def __init__(self, s):
        super(Qualifier_OU, self).__init__()
        loadUi("Qualifier_OU.ui", self)
        self.UserType = s
        self.pushButton_back.clicked.connect(self.Back)
        self.pushButton_final.clicked.connect(self.Final)

    def Back(self):
        back = PointsTable_OU(self.UserType)
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Final(self):
        back = Final_OU(self.UserType)
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)


##################################  FINAL PAGE ADMIN PAGE  ##################################################
class Final_A(QtWidgets.QMainWindow):
    def __init__(self):
        super(Final_A, self).__init__()
        loadUi("Final_A.ui", self)
        self.pushButton_back.clicked.connect(self.Home)
        self.pushButton_save.clicked.connect(self.Save)

    def Home(self):
        backbutton = Qualifier_A()
        widget.addWidget(backbutton)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Save(self):
        msg = QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setText("Finalists Data Saved Successfully!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

        Home_Page = AdminHP()
        widget.addWidget(Home_Page)
        widget.setCurrentIndex(widget.currentIndex() + 1)


###################################### FINAL PAGE OWNER/GEN.USER PAGE  ############################################
class Final_OU(QtWidgets.QMainWindow):
    def __init__(self, s):
        super(Final_OU, self).__init__()
        loadUi("Final_OU.ui", self)
        self.UserType = s
        self.pushButton_back.clicked.connect(self.Home)
        self.pushButton_home.clicked.connect(self.Home_Page)

    def Home(self):
        backbutton = Qualifier_OU(self.UserType)
        widget.addWidget(backbutton)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Home_Page(self):
        if self.UserType == 'Owner':
            back = OwnerHP()
        else:
            back = GeneralUserHP()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mainwindow = MainClass()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(740)
    widget.setFixedHeight(570)
    widget.show()
    app.exec_()