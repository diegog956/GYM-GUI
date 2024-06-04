import time
import customtkinter as ctk
import pywinstyles
from db.db import *
import datetime as dt
from PIL import Image


class Access_Frame(ctk.CTkFrame):

    def __init__(self, app: ctk.CTkFrame, id: int):
        super().__init__(app)
        self.id = id
        # Set the GRID configuration
        for i in range(7):
            self.grid_rowconfigure(i, weight=1)

        self.grid_columnconfigure(0, weight=7)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=7)

        self.access_info = get_access(id)

        if not self.access_info:

            self.access_denied()

        else:
            self.first_name = self.access_info[0][0]
            self.last_name = self.access_info[0][1]
            self.member_type = self.access_info[0][2]
            self.due_date = self.access_info[0][3]

            if self.check_due_date():

                self.access_denied()

            else:

                self.access_granted()

    def access_granted(self) -> None:
        # Set the green color

        self.configure(fg_color="#106A43")

        self.configure(border_width=2)
        self.configure(border_color='#2CC985')

        # "Access Granted" label text
        entry_access_granted_text = ctk.CTkLabel(self, text='ACCESS GRANTED', text_color='light gray',

                                                 font=('Roboto', 50))
        entry_access_granted_text.grid(row=1, column=1, rowspan=2, sticky='nsew')

        # Fullname

        entry_fullname_text = ctk.CTkLabel(self, text=f'\n{self.first_name} {self.last_name}', text_color='light gray',
                                           fg_color="#106A43", font=('Roboto', 20))
        entry_fullname_text.grid(row=3, column=1, sticky='wnse')

        dict_member_type = {
            1: 'Member',
            2: 'Instructor',
            3: 'Maintenance Staff',
            4: 'Cleaning Crew',
        }
        member_type = dict_member_type.get(self.member_type)

        entry_member_type_text = ctk.CTkLabel(self, text=member_type, text_color='light gray',
                                              fg_color="#106A43", font=('Roboto', 20))
        entry_member_type_text.grid(row=4, column=1, sticky='wnse')

        entry_due_date_text = ctk.CTkLabel(self, text=f'\nDue Date: {self.due_date}', text_color='light gray',
                                           fg_color="#106A43", font=('Roboto', 20))
        entry_due_date_text.grid(row=5, column=1, sticky='wnse')

    def access_denied(self) -> None:

        # Set the red color
        self.configure(fg_color="#ED4337")

        # "Access Denied" label text
        entry_fullname_text = ctk.CTkLabel(self, text='ACCESS DENIED', text_color='light white', fg_color="#ED4337",
                                           font=('Roboto', 50))
        entry_fullname_text.grid(row=1, column=1, rowspan=2, sticky='nsew')

    def check_due_date(self) -> bool:
        return datetime.date.today() >= self.due_date
