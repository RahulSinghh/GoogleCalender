from Calender import Calender
from Database import Database

class User:

    def __init__(self, userName, userEmail):
        self.userName = userName
        self.userEmail = userEmail
        calender = Calender()
