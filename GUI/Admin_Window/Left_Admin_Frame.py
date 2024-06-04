import customtkinter as ctk
from PIL import Image


class Left_Admin_Frame(ctk.CTkFrame):

    def __init__(self, app: ctk.CTkFrame, back_main_frame):
        super().__init__(app)
        self.back_main_frame = back_main_frame
        for i in range(20):
            self.grid_rowconfigure(i, weight=1)

        self.grid_columnconfigure(0, weight=1)

        #

        # Set the logo image on central frame
        self.image = ctk.CTkImage(dark_image=Image.open('GUI/Access_Window/assets/logo_gym.png'), size=(250, 250))
        self.aux_label = ctk.CTkLabel(self, image=self.image, text='', padx=10, pady=10, corner_radius=0)
        self.aux_label.grid(row=0, column=0, rowspan=9)

        self.menu_add_member_button = ctk.CTkButton(self, text='Add Member', command=None,
                                                    font=('Roboto', 20), fg_color="#106A43", hover_color='#2CC985')
        self.menu_add_member_button.grid(row=10, column=0, sticky='nsew', pady=5, padx=5)

        self.pay_button = ctk.CTkButton(self, text='Add Routine', command=None,
                                        font=('Helvetica', 20), fg_color="#106A43", hover_color='#2CC985')
        self.pay_button.grid(row=11, column=0, sticky='nsew', pady=5, padx=5)

        self.pay_button = ctk.CTkButton(self, text='Register Payment', command=None,
                                        font=('Helvetica', 20), fg_color="#106A43", hover_color='#2CC985')
        self.pay_button.grid(row=12, column=0, sticky='nsew', pady=5, padx=5)

        self.statistics_button = ctk.CTkButton(self, text='Statistics', command=None,
                                               font=('Helvetica', 20), fg_color="#106A43", hover_color='#2CC985')
        self.statistics_button.grid(row=13, column=0, sticky='nsew', pady=5, padx=5)

        self.menu_back_button = ctk.CTkButton(self, text='Log Out', command=self.back_main_frame,
                                              font=('Helvetica', 20), fg_color="#106A43", hover_color='#2CC985')
        self.menu_back_button.grid(row=19, column=0, sticky='nsew', pady=5, padx=5)

    def change(self):
        pass