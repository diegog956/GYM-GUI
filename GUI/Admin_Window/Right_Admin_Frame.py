import datetime

import customtkinter as ctk
import tkinter as tk

import pywinstyles
import tkcalendar as tkc


class Right_Admin_Frame(ctk.CTkFrame):

    def __init__(self, app, controller):
        super().__init__(app, border_width=2, border_color='#2CC985')
        self.app = app
        self.controller = controller
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.add_member_onto_right_frame()

    def add_member_onto_right_frame(self):

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)

        for i in range(20):
            self.grid_rowconfigure(i, weight=1)

        # Name
        name_label = ctk.CTkLabel(self, text='Name:', font=('Helvetica', 15))
        name_label.grid(row=3, column=0, sticky= 'nse', padx=25)

        name_entry = ctk.CTkEntry(self, font=('Helvetica', 20))
        name_entry.grid(row=3, column=1, sticky='ew')

        # Last Name

        lastname_label = ctk.CTkLabel(self, text='Last name:', font=('Helvetica', 15))
        lastname_label.grid(row=4, column=0, sticky='nse', padx=25)

        last_name_entry = ctk.CTkEntry(self, font=('Helvetica', 20))
        last_name_entry.grid(row=4, column=1, sticky='ew')

        # Birthday
        birthday_label = ctk.CTkLabel(self, text='Birthday:', font=('Helvetica', 15))
        birthday_label.grid(row=5, column=0, sticky='nse', padx=25)

        date_entry = tkc.DateEntry(self, year=datetime.date.today().year, background='#106A43', foreground='white',
                                   month=datetime.date.today().month, day=datetime.date.today().day,
                                   font=('Helvetica', 19), maxdate=datetime.date.today(), border_color='#2CC985',
                                   selectbackground='#106A43', relief='raised')
        date_entry.grid(row=5, column=1, sticky='ew')

        # Phone

        phone_label = ctk.CTkLabel(self, text='Phone:', font=('Helvetica', 15))
        phone_label.grid(row=6, column=0, sticky='nse', padx=25)

        phone_entry = ctk.CTkEntry(self, font=('Helvetica', 20))
        phone_entry.grid(row=6, column=1, sticky='ew')

        # Address

        address_label = ctk.CTkLabel(self, text='Address:', font=('Helvetica', 15))
        address_label.grid(row=7, column=0, sticky='nse', padx=25)

        address_entry = ctk.CTkEntry(self, font=('Helvetica', 20))
        address_entry.grid(row=7, column=1, sticky='ew')

        # Email
        email_label = ctk.CTkLabel(self, text='Email:', font=('Helvetica', 15))
        email_label.grid(row=8, column=0, sticky='nse', padx=25)

        email_entry = ctk.CTkEntry(self, font=('Helvetica', 20))
        email_entry.grid(row=8, column=1, sticky='ew')

        # Gender

        gender_label = ctk.CTkLabel(self, text='Gender:', font=('Helvetica', 15))
        gender_label.grid(row=9, column=0, sticky='nse', padx=25)

        gender_choice = ctk.StringVar(value='Male')

        gender_frame = ctk.CTkFrame(self)

        gender_frame.grid_columnconfigure((0,1,2),weight=1)
        pywinstyles.set_opacity(gender_frame, value=0.97)

        gender_frame.grid(row=9, column=1, sticky='we')

        Male_gender_radiobutton = ctk.CTkRadioButton(gender_frame, text='Male', value='Male', variable=gender_choice,
                                                     border_color='#106A43', hover_color='#2CC985')
        Male_gender_radiobutton.grid(row=0, column=0, sticky='ew')

        Female_gender_radiobutton = ctk.CTkRadioButton(gender_frame, text='Female', value='Female', variable=gender_choice, border_color='#106A43', hover_color='#2CC985')
        Female_gender_radiobutton.grid(row=0, column=1, sticky='ew')

        Other_gender_radiobutton = ctk.CTkRadioButton(gender_frame, text='Other', value='Other', variable=gender_choice, border_color='#106A43', hover_color='#2CC985')
        Other_gender_radiobutton.grid(row=0, column=2, sticky='ew')

        # Bloodtype
        bloodtype_label = ctk.CTkLabel(self, text='Blood type:', font=('Helvetica', 15))
        bloodtype_label.grid(row=10, column=0, sticky='nse', padx=25)

        bloodtype = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

        bloodtype_combobox = ctk.CTkComboBox(self, values=bloodtype, button_color='#106A43',
                                             button_hover_color='#2CC985')
        bloodtype_combobox.grid(row=10, column=1, sticky='ew')

        # MemberType

        bloodtype_label = ctk.CTkLabel(self, text='Member type:', font=('Helvetica', 15))
        bloodtype_label.grid(row=11, column=0, sticky='nse', padx=25)

        membertype = ["Member", "Instructor", "Maintenance", "Cleaning"]

        membertype_combobox = ctk.CTkComboBox(self, values=membertype, button_color='#106A43',
                                             button_hover_color='#2CC985')
        membertype_combobox.grid(row=11, column=1, sticky='ew')


        # Cancel

        add_button = ctk.CTkButton(self, fg_color='#106A43', text='Cancel')
        add_button.grid(row=18, column=1, sticky='nsw')

        # Add

        add_button = ctk.CTkButton(self, fg_color='#106A43', text='Add member')
        add_button.grid(row=18, column=1, sticky='nse')