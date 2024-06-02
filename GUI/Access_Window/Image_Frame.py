import customtkinter as ctk
from PIL import Image
from GUI.Access_Window.Central_Frame import Central_Frame


class Image_Frame(ctk.CTkFrame):

    def __init__(self, app: ctk.CTk):
        super().__init__(app)

        # Grid Configuration
        # Row/s
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=3)

        # Columns
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=5)

        # Background Image
        self.image = ctk.CTkImage(dark_image=Image.open('GUI/Access_Window/assets/background-image.jpg'))
        self.aux_label = ctk.CTkLabel(self, image=self.image, text='')
        self.aux_label.grid(row=0, column=0, columnspan=3, rowspan=3, sticky='nswe')

        # Central Frame
        self.central_frame = Central_Frame(self)
        self.central_frame.grid(row=0, column=1, rowspan=3,sticky='nsew')

        # Bind the dimension changes resizing the frame
        self.bind("<Configure>", self.bg_image_resizer)

        # Store the original image for resizing purposes
        self.original_image = Image.open(r'GUI/Access_Window/assets/background-image.jpg')

    def bg_image_resizer(self, event) -> None:
        # Opens the images setting the width and height of the app with the window one and put it on the same label
        i = ctk.CTkImage(dark_image=self.original_image, size=(self.winfo_width(), self.winfo_height()))
        self.aux_label.configure(text="", image=i)
