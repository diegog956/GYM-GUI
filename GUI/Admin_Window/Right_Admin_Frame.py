import customtkinter as ctk
import tkinter as tk
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
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)

        for i in range(20):
            self.grid_rowconfigure(i, weight=1)

        # Name
        name_entry = ctk.CTkEntry(self, font=('Helvetica', 20))
        name_entry.grid(row=3, column=1, sticky='ew')

        # Last Name
        last_name_entry = ctk.CTkEntry(self, font=('Helvetica', 20))
        last_name_entry.grid(row=4, column=1, sticky='ew')

        # Birthday
        date_entry = tkc.DateEntry(self, year=2024, background='darkblue', foreground='white',
                                   month=6, day=6)
        date_entry.grid(row=5, column=1, sticky='nsew')

        # Phone
        phone_entry = ctk.CTkEntry(self, font=('Helvetica', 20))
        phone_entry.grid(row=6, column=1, sticky='ew')

        # Address
        address_entry = ctk.CTkEntry(self, font=('Helvetica', 20))
        address_entry.grid(row=7, column=1, sticky='ew')

        # Email
        email_entry = ctk.CTkEntry(self, font=('Helvetica', 20))
        email_entry.grid(row=8, column=1, sticky='ew')

        # Gender

        # Bloodtype

        # MemberType
