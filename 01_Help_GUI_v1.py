from tkinter import * 
from functools import partial
import random


class Converter:
    def __init__(self, parent):

        background_color = "#ffadf0"  # pink

        # Main screen GUI
        self.converter_frame = Frame(width=600, height=600, bg=background_color, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,text="Temperature Converter", font=("Arial","16","bold"),bg=background_color,padx=10,pady=10)
        self.temp_converter_label.grid(row=0)

        self.help_button = Button(self.converter_frame, text="Help", font=("Arial","14"), 
        command=self.help,
        padx=10, pady=10)
        self.help_button.grid(row=2)

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

class Help:
    def __init__(self, partner):

        background = "light blue"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # Set up GUI frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions", font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="", justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(column=0, row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg=background, command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help():
        print("whee, it's friday")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Converter(root)
    root.mainloop()
