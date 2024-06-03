import time
from datetime import datetime, date, timedelta
from monthdelta import monthdelta
import customtkinter as ctk
import pywinstyles
from PIL import Image
import tkinter as tk
from GUI.Access_Window.Access_Frame import Access_Frame
import re
from GUI.Admin_Window.Admin_Frame import Admin_Frame


class Central_Frame(ctk.CTkFrame):

    def __init__(self, app: ctk.CTkFrame, master1: ctk.CTk):
        super().__init__(app, bg_color='black', corner_radius=0, fg_color='#343434')
        self.master1 = master1
        self.app = app
        # Set the Frame opacity:
        pywinstyles.set_opacity(self, value=0.97)

        # Configure GRID:
        # Columns = 1
        self.grid_columnconfigure(0, weight=1)

        # Rows = 100
        for i in range(0, 100):
            self.grid_rowconfigure(i, weight=1)

        # Set the logo image on central frame
        self.image = ctk.CTkImage(dark_image=Image.open('GUI/Access_Window/assets/logo_gym.png'), size=(250, 250))
        self.aux_label = ctk.CTkLabel(self, image=self.image, text='', padx=0, pady=0, corner_radius=32)
        self.aux_label.grid(row=0, column=0, rowspan=20, sticky='s')

        # "Welcome" label text
        self.welcome_text = ctk.CTkLabel(self, text='WELCOME', font=("Arial", 36, "bold"), fg_color='#343434')
        self.welcome_text.grid(row=21, column=0, sticky='nswe', padx=10)

        # "nice to see you again!" label text
        self.nice_see_you_text = ctk.CTkLabel(self, text="It's nice to see you again!",
                                              font=("Times New Roman", 24, "italic"), fg_color='#343434')
        self.nice_see_you_text.grid(row=22, column=0, sticky='e', padx=10)

        # "Enter your access code:" label text
        self.enter_id_text = ctk.CTkLabel(self, text='Enter your access code:', font=('Helvetica', 25),
                                          fg_color='#343434')
        self.enter_id_text.grid(row=40, column=0, sticky='w', padx=10)

        # ID Entry
        self.entry_id = ctk.CTkEntry(self, placeholder_text='', height=100, font=('Helvetica', 54), justify='center')
        self.entry_id.bind('<Return>', self.check_access)  # Bind to Key 'Enter'
        self.entry_id.grid(row=41, column=0, sticky='we', rowspan=1, padx=10, pady=10)

        # Send Button
        self.check_access_button = ctk.CTkButton(self, text='Let me in!', command=self.check_access, height=35,
                                                 font=('Helvetica', 20), fg_color="#106A43", hover_color='#2CC985')
        self.check_access_button.grid(row=44, column=0, sticky='nswe', rowspan=5, padx=10, pady=10)

        # Admin Access

        # "Admin User" text label
        self.admin_user_text = ctk.CTkLabel(self, text='Admin user')
        self.admin_user_text.grid(row=69, column=0, sticky='', pady=0, padx=0)

        # User Entry
        self.admin_user_entry = ctk.CTkEntry(self, placeholder_text='')
        self.admin_user_entry.grid(row=70, column=0, rowspan=2)

        # "Password" label text
        self.admin_password_text = ctk.CTkLabel(self, text='Password')
        self.admin_password_text.grid(row=72, column=0, sticky='', pady=0, padx=0)

        # Password Entry
        self.admin_password_entry = ctk.CTkEntry(self, placeholder_text='', show="*")
        self.admin_password_entry.grid(row=73, column=0, rowspan=2)

        # Login Button
        self.admin_access_button = ctk.CTkButton(self, text='Login', fg_color="#106A43", hover_color='#2CC985',
                                                 command=self.admin_access)
        self.admin_access_button.grid(row=75, column=0)

        # Bind focus events to maintain focus on Entry_ID
        self.check_access_button.bind('<ButtonPress>', self.focus_to_entry)  # Bind ButtonPress event
        self.entry_id.bind('<FocusOut>', self.focus_to_entry)  # Bind FocusOut event

        self.admin_frame = None
    def focus_to_entry(self, event=None) -> None:
        # Check if the clicked widget is another entry (assuming you have multiple)
        if isinstance(event.widget, tk.Entry) and event.widget != self.entry_id:
            return None  # Do nothing if clicking on another entry

        # Otherwise, set focus back to the original entry
        self.entry_id.focus_set()

    def check_access(self, event=None) -> None:
        if bool(re.search('\s+', self.entry_id.get())) or self.entry_id.get().isalpha() or self.entry_id.get() == '':

            no_text_or_string_label = ctk.CTkLabel(self, text='Wrong! ID must have only numbers.',
                                                   font=('Helvetica', 12),
                                                   fg_color='#343434', text_color='red')
            no_text_or_string_label.grid(row=42, column=0, sticky='e', padx=10)
            self.entry_id.delete(0, tk.END)
            no_text_or_string_label.after(2000, lambda: no_text_or_string_label.destroy())
            pass
        else:

            # Create the green/red access frame
            access_frame = Access_Frame(self.app, self.entry_id.get())
            access_frame.grid(row=1, column=0, columnspan=3, sticky='nsew')

            # Set the opacity of the access frame on 0
            pywinstyles.set_opacity(access_frame, value=0)

            # Set a variable that will increase proportionally
            transparency = 0

            pywinstyles.set_opacity(self, value=0.3)

            while transparency < 1.0:
                # Increase the transparency 1% every 2 milliseconds until transparency equals to 1
                transparency += 0.01
                pywinstyles.set_opacity(access_frame, value=transparency)
                # Refresh the page
                access_frame.update()
                time.sleep(0.002)

            # After 3 seconds this frame is destroyed
            access_frame.after(3000, lambda: access_frame.destroy())
            self.after(3000, lambda: pywinstyles.set_opacity(self, value=0.97))

            # Remove the ID from the screen
            self.entry_id.delete(0, tk.END)



    def admin_access(self):
        user = self.admin_user_entry.get()
        password = self.admin_password_entry.get()

        print(user, password)

        if user == '1' and password == '1':
            self.destroy()
            self.app.grid_rowconfigure(0, weight=1)
            self.app.grid_rowconfigure(1, weight=8)
            self.app.grid_rowconfigure(2, weight=1)

            # Columns
            self.app.grid_columnconfigure(0, weight=1)
            self.app.grid_columnconfigure(1, weight=4)
            self.app.grid_columnconfigure(2, weight=1)

            self.admin_frame = Admin_Frame(self.app)
            pywinstyles.set_opacity(self.admin_frame, 0.97)
            self.admin_frame.grid(column=1, row=1, sticky='nsew')

            back_button = ctk.CTkButton(self.admin_frame, text='Volver', command=self.back_main_frame)
            back_button.place(x=10,y=10)


        else:
            pass

    def back_main_frame(self):
        self.admin_frame.destroy()

        self.app.grid_rowconfigure(0, weight=3)
        self.app.grid_rowconfigure(1, weight=1)
        self.app.grid_rowconfigure(2, weight=3)

        # Columns
        self.app.grid_columnconfigure(0, weight=5)
        self.app.grid_columnconfigure(1, weight=2)
        self.app.grid_columnconfigure(2, weight=5)

        from GUI.Access_Window.Image_Frame import Image_Frame
        Image_Frame.create_image_frame(self.app)


        # central_frame = Central_Frame(self, self.master1)
        # central_frame.grid(row=0, column=1, rowspan=3, sticky='nsew')