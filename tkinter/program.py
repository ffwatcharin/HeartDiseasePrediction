import customtkinter as ctk
import tkinter as tk
import joblib
import pandas as pd

ctk.set_appearance_mode('Scolumnstem')
ctk.set_default_color_theme('green')

appWidth, appHeight = 1200, 600

heart_prediction = joblib.load('my_ml_model_eiei.joblib')

ui_font_big = ('Cascadia Code', 22, 'bold')
ui_font_small = ('Cascadia Code', 18, 'bold')

class App(ctk.CTk):

    def __init__(self, fg_color: str | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.title('Tesla Model Linear')
        self.geometry(f'{appWidth}x{appHeight}')

        self.nameTitle = ctk.CTkLabel(
            self, text='Heart Disease Prediction', font=ui_font_big)
        self.nameTitle.grid(row=0, column=2, padx=10, pady=10)

        #age
        self.ageLabel = ctk.CTkLabel(
            self, text='Age', font=ui_font_small)
        self.ageLabel.grid(row=1, column=0, padx=10, pady=10)
        self.ageEntry = ctk.CTkEntry(self,
                                      placeholder_text="Enter age krub")
        self.ageEntry.grid(row=2, column=0, padx=5, pady=5)
        
        #gender label
        self.genderLabel = ctk.CTkLabel(self, text='Gender', font=ui_font_small)
        self.genderLabel.grid(row=3, column=0, padx=10, pady=10)
        #gender button
        self.genderVar = tk.StringVar(value='None')

        self.nameEntry = ctk.CTkEntry(self,
                                      placeholder_text="Enter name krub")
        self.nameEntry.place(x=150, y=80)
        self.genderVar = tk.StringVar(value="Prefer\
                                         not to say")


if __name__ == "__main__":
    app = App()
    app.mainloop()
