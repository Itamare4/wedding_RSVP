# -*- coding: UTF-8 -*-

from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService
import xlrd
from xlutils.copy import copy
import time

__author__ = "Itamar Eliakim"
__copyright__ = "Copyright 2019, Yael and Itamar"
__version__ = "0.0.1"
__email__ = "itamare@gmail.com"
__website__ = "www.ItamarEliakim.com"

# Defines
COUNTRY_AREA_CODE = "+972"
FILENAME = "Wedding.xlsx"
COUPLE_NAME = "יעל ואיתמר"
WEBSITE_ADDRESS = "www.YaelItamar.tk"
IP_ADDRESS = "192.168.0.4"
DEBUG = True

# INVITATION TEMPLATES
INVITE = "אורחים יקרים! הוזמנתם לחתונה של " + COUPLE_NAME + " ב5/9💏\nהאירוע יתקיים בשטח חקלאי סמוך לקיבוץ חולדה בשעה 19:30.\nאנא השיבו להודעה זו את מספר אורחים המגיעים לאירוע או 0-לא מגיע."
INVITE_REMINDER = "עדיין לא אישרת הגעה לחתונה של " + COUPLE_NAME + " ב5/9, השיבו להודעה זו את מספר האורחים המגיעים או 0-לא מגיע"
TRANSPORTATION = "להוראות הגעה והסעות - " + WEBSITE_ADDRESS
THANK_YOU = "אז אחרי שקצת עיכלנו,\nחשוב לנו להגיד פשוט תודה!\nשהייתם, רקדתם ושמחתם איתנו :)\nאוהבים ומעריכים, " + COUPLE_NAME

class Wedding():
    def __init__(self):
        self.loc = (FILENAME)
        self.ip = IPv4Address(IP_ADDRESS)
        self.session = AirmoreSession(self.ip)

        self.was_accepted = self.session.request_authorization()
        if (self.was_accepted):
            print("Connection Established")
        else:
            print("Connection Error! please verify ip address")
            exit()
            
        self.service = MessagingService(self.session)

        #Open Excel
        self.rb = xlrd.open_workbook(self.loc)
        self.sheet = self.rb.sheet_by_index(0)
        self.wb = copy(self.rb)
        self.w_sheet = self.wb.get_sheet(0)

        self.createGuestListDict()
        self.sendInvitationList()
        self.checkRecieve()

        self.createArrivedGuestsDict()
        self.sendThankYou()

    def getConfirmedGuests(self):
        column_sum = 0
        for row in range(self.sheet.nrows):
            try:
                column_sum += self.sheet.cell_value(row, 4)
            except:
                pass
        return int(column_sum)

    def createArrivedGuestsDict(self):
        arrived_guests = 0
        self.guest_dict = {}
        for i in range(1, self.sheet.nrows):
            try:
                if ((self.sheet.cell_value(i, 12)>0) and (len(self.sheet.cell_value(i, 2))==10)): #Person did not response and phone number is defined in list
                        phone_number = self.sheet.cell_value(i, 2)
                        phone_number = COUNTRY_AREA_CODE + phone_number[1:len(phone_number)]
                        self.guest_dict[phone_number] = i
                        arrived_guests += self.sheet.cell_value(i, 10)
            except:
                pass

        print("Total Arrived Guests - ", arrived_guests)


    def createGuestListDict(self):
        not_resp = 0
        self.guest_dict = {}
        for i in range(0, self.sheet.nrows):
            if ((self.sheet.cell_value(i, 9)=="לא הגיב") and (len(self.sheet.cell_value(i, 2))==10)): #Person did not response and phone number is defined in list
                    phone_number = self.sheet.cell_value(i, 2)
                    phone_number = COUNTRY_AREA_CODE + phone_number[1:len(phone_number)]
                    self.guest_dict[phone_number] = i
                    not_resp += 1

        print("Total Rows - ", self.sheet.nrows, "Did not responed - ", not_resp, " confirmed guests - ", self.getConfirmedGuests())

    def checkRecieve(self):
        while True:
            messages = self.service.fetch_message_history()
            for i in range(0,20):           #Check only last 20 messages
                #Update person with the retuned number of SMS
                try:
                    print(messages[i].phone)
                    print("Recieved Message from - ", messages[i].phone, " number of confirmed guests - ", int(messages[i].content))
                    if ((messages[i].phone in self.guest_dict) and (self.sheet.cell_value(self.guest_dict[messages[i].phone], 9)=="לא הגיב")):
                        print("Guest Confirmed!! Recieved Message from - ", messages[i].phone, " number of confirmed guests - ", int(messages[i].content))
                        self.w_sheet.write(self.guest_dict[messages[i].phone], 10, messages[i].content)
                        self.w_sheet.write(self.guest_dict[messages[i].phone], 9, "מגיע")
                        if (int(messages[i].content)>0):
                            print("Send Transportation")
                            print(messages[i].phone, TRANSPORTATION) if DEBUG else self.service.send_message(messages[i].phone, TRANSPORTATION)
                        self.wb.save('Wedding.xlsx')
                except:
                    pass
                time.sleep(0.2)

    def sendThankYou(self):
        print("Do you want to send THANK YOU SMS? \n")
        choice = input().lower()
        if (choice=="yes"):
            print ("Sending SMS")
            #Send SMS
            for i in self.guest_dict:
                print("Send SMS to - ", i)
                name = self.sheet.cell_value(self.guest_dict[i], 0)
                msg_to_send = name + ",\n" + THANK_YOU
                print(msg_to_send) if DEBUG else self.service.send_message(i, msg_to_send)
                time.sleep(2)

    def sendInvitationList(self):
        print("Do you want to send INVITATION SMS? \n")
        choice = input().lower()
        if (choice=="yes"):
            print ("Sending SMS")
            for i in self.guest_dict:
                print("Send SMS to - ", i)
                print(INVITE_REMINDER) if DEBUG else self.service.send_message(i, INVITE)
                time.sleep(1)

    def sendInvitationReminderAllList(self):
        print("Do you want to send INVITATION REMINDER SMS? \n")
        choice = input().lower()
        if (choice=="yes"):
            print ("Sending SMS")
            for i in self.guest_dict:
                print("Send SMS to - ", i)
                print(INVITE_REMINDER) if DEBUG else self.service.send_message(i, INVITE_REMINDER)
                time.sleep(1)

if __name__ == "__main__":
    wedding = Wedding()
