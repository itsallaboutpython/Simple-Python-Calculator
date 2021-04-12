from tkinter import *
from functools import partial
import time
import os
import sys
import threading
from playsound import playsound


class Calculator(Tk):
    def __init__(self, output_bg, output_fg, button_bg, button_fg):
        super().__init__()

        # Constants
        self.OUTPUT_FONT = ("Calibri", 30)
        self.OUTPUT_BG = output_bg
        self.OUTPUT_FG = output_fg
        self.BUTTON_FONT = ("Calibri", 20)
        self.BUTTON_BG = button_bg
        self.BUTTON_FG = button_fg
        self.BUTTON_WIDTH = 6
        self.BUTTON_HEIGHT=0
        self.CLIP = "beep.mp3"

        self.Initialize()
        self.geometry('400x400')
        self.title("Calculator")
        self.configure(bg='grey')
        self.button_list = [self.button0, self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8, self.button9, self.button_add, self.button_subtract, self.button_multiply, self.button_divide, self.button_equal, self.button_dot]

        # Keyboard bindings
        self.bind("<Key-0>", self.key_press)
        self.bind("<Key-1>", self.key_press)
        self.bind("<Key-2>", self.key_press)
        self.bind("<Key-3>", self.key_press)
        self.bind("<Key-4>", self.key_press)
        self.bind("<Key-5>", self.key_press)
        self.bind("<Key-6>", self.key_press)
        self.bind("<Key-7>", self.key_press)
        self.bind("<Key-8>", self.key_press)
        self.bind("<Key-9>", self.key_press)
        self.bind("<Key-plus>", self.key_press)
        self.bind("<Key-minus>", self.key_press)
        self.bind("<Key-asterisk>", self.key_press)
        self.bind("<Key-x>", self.key_press)
        self.bind("<Key-slash>", self.key_press)
        self.bind("<Key-equal>", self.key_press)
        self.bind("<Return>", self.enter_key_press)
        self.bind("<Key-BackSpace>", self.backspace)
        self.bind("<Key-Delete>", self.delete)
        self.bind("<Key-Escape>", exit)

    def backspace(self, event):
        self.output_entry.configure(state=NORMAL)
        text = self.output_entry.get()
        if text != "" or text != None:
            self.output_entry.delete(len(text)-1, len(text))
        self.output_entry.configure(state=DISABLED)

    def delete(self, event):
        self.output_entry.configure(state=NORMAL)
        text = self.output_entry.get()
        if text != "" or text != None:
            self.output_entry.delete(0, len(text))
        self.output_entry.configure(state=DISABLED)

    def key_press(self, event):
        for button in self.button_list:
            if event.char in button["text"]:
                button.configure(bg="white", relief="sunken")
                self.update_idletasks()
                time.sleep(0.1)
                button.invoke()
                button.configure(bg=self.BUTTON_BG, relief="raised")
            elif event.char == "*" or event.char == "x":
                self.button_multiply.configure(bg="white", relief="sunken")
                self.update_idletasks()
                time.sleep(0.1)
                self.button_multiply.invoke()
                self.button_multiply.configure(bg=self.BUTTON_BG, relief="raised")
                break
    
    def enter_key_press(self, event):
        self.button_equal.configure(bg="white", relief="sunken")
        self.update_idletasks()
        time.sleep(0.1)
        self.button_equal.invoke()
        self.button_equal.configure(bg=self.BUTTON_BG, relief="raised")

    def play_sound(self):
        playsound(self.CLIP)

    def sum(self, num1, num2):
        return num1+num2

    def subtract(self, num1, num2):
        return num1-num2

    def multiply(self, num1, num2):
        return num1*num2

    def divide(self, num1, num2):
        return num1/num2

    def print_number(self, number):
        clip_thread = threading.Thread(target=self.play_sound)
        clip_thread.start()
        self.output_entry.configure(state=NORMAL)
        self.output_entry.insert(END, number)
        self.output_entry.configure(state=DISABLED)

    def print_result(self):
        expression = self.output_entry.get()
        self.output_entry.configure(state=NORMAL)
        self.output_entry.delete(0, len(expression))
        output = ''
        nums = []
        if "+" in expression:
            nums = expression.split('+')
            try:
                num1 = int(nums[0])
                num2 = int(nums[1])
            except:
                num1 = float(nums[0])
                num2 = float(nums[1])
            self.output_entry.insert(END, str( self.sum( num1, num2) ) )
        elif "-" in expression:
            nums = expression.split("-")
            try:
                num1 = int(nums[0])
                num2 = int(nums[1])
            except:
                num1 = float(nums[0])
                num2 = float(nums[1])
            self.output_entry.insert(END,  str( self.subtract( num1, num2) ) ) 
        elif "x" in expression:
            nums = expression.split("x")
            try:
                num1 = int(nums[0])
                num2 = int(nums[1])
            except:
                num1 = float(nums[0])
                num2 = float(nums[1])
            self.output_entry.insert(END,  str( self.multiply( num1, num2 ) ) ) 
        elif "/" in expression:
            nums = expression.split("/")
            try:
                num1 = int(nums[0])
                num2 = int(nums[1])
            except:
                num1 = float(nums[0])
                num2 = float(nums[1])
            self.output_entry.insert(END, str( self.divide( num1, num2 ) ) )
        
        self.output_entry.configure(state=DISABLED)

    def Initialize(self):

        # Creating frames
        self.output_frame = Frame(self)
        self.output_frame.configure(width=400, height=100)
        self.output_frame.grid(row=0, column=0, sticky=NSEW)

        self.button_frame = Frame(self)
        self.button_frame.configure(width=400, height=300)
        self.button_frame.grid(row=1, column=0, sticky=NSEW)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=4)
        self.grid_columnconfigure(0, weight=1)

        self.output_entry = Entry(self.output_frame, font=self.OUTPUT_FONT, state=DISABLED, disabledbackground=self.OUTPUT_BG)
        self.output_entry.configure(bg=self.OUTPUT_BG, fg=self.OUTPUT_FG)
        self.output_entry.pack(fill=BOTH, expand=True)

        self.button1 = Button(self.button_frame, font=self.BUTTON_FONT, text="1", command=partial(self.print_number, "1"))
        self.button1.configure(bg=self.BUTTON_BG, fg=self.BUTTON_FG, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button1.grid(row=0, column=0, sticky=NSEW)

        self.button2 = Button(self.button_frame, font=self.BUTTON_FONT, text="2", command=partial(self.print_number, "2"))
        self.button2.configure(bg=self.BUTTON_BG, fg=self.BUTTON_FG, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button2.grid(row=0, column=1, sticky=NSEW)

        self.button3 = Button(self.button_frame, font=self.BUTTON_FONT, text="3", command=partial(self.print_number, "3"))
        self.button3.configure(bg=self.BUTTON_BG, fg=self.BUTTON_FG, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button3.grid(row=0, column=2, sticky=NSEW)

        self.button_add = Button(self.button_frame, font=self.BUTTON_FONT, text="+", command=partial(self.print_number, "+"))
        self.button_add.configure(bg=self.BUTTON_BG, fg=self.BUTTON_FG, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button_add.grid(row=0, column=3, sticky=NSEW)

        self.button4 = Button(self.button_frame, font=self.BUTTON_FONT, text="4", command=partial(self.print_number, "4"))
        self.button4.configure(bg=self.BUTTON_BG, fg=self.BUTTON_FG, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button4.grid(row=1, column=0, sticky=NSEW)

        self.button5 = Button(self.button_frame, font=self.BUTTON_FONT, text="5", command=partial(self.print_number, "5"))
        self.button5.configure(bg=self.BUTTON_BG, fg=self.BUTTON_FG, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button5.grid(row=1, column=1, sticky=NSEW)

        self.button6 = Button(self.button_frame, font=self.BUTTON_FONT, text="6", command=partial(self.print_number, "6"))
        self.button6.configure(bg=self.BUTTON_BG, fg=self.BUTTON_FG, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button6.grid(row=1, column=2, sticky=NSEW)

        self.button_subtract = Button(self.button_frame, font=self.BUTTON_FONT, text="-", command=partial(self.print_number, "-"))
        self.button_subtract.configure(bg=self.BUTTON_BG, fg=self.BUTTON_FG, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button_subtract.grid(row=1, column=3, sticky=NSEW)

        self.button7 = Button(self.button_frame, font=self.BUTTON_FONT, text="7", command=partial(self.print_number, "7"))
        self.button7.configure(bg=self.BUTTON_BG, fg=self.BUTTON_FG, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button7.grid(row=2, column=0, sticky=NSEW)

        self.button8 = Button(self.button_frame, font=self.BUTTON_FONT, text="8", command=partial(self.print_number, "8"))
        self.button8.configure(bg=self.BUTTON_BG, fg=self.BUTTON_FG, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button8.grid(row=2, column=1, sticky=NSEW)

        self.button9 = Button(self.button_frame, font=self.BUTTON_FONT, text="9", command=partial(self.print_number, "9"))
        self.button9.configure(bg=self.BUTTON_BG, fg=self.BUTTON_FG, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button9.grid(row=2, column=2, sticky=NSEW)

        self.button_multiply = Button(self.button_frame, font=self.BUTTON_FONT, text="X", command=partial(self.print_number, "x"))
        self.button_multiply.configure(bg=self.BUTTON_BG, fg=self.BUTTON_FG, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button_multiply.grid(row=2, column=3, sticky=NSEW)

        self.button_dot = Button(self.button_frame, font=self.BUTTON_FONT, text=".", command=partial(self.print_number, "."))
        self.button_dot.configure(bg=self.BUTTON_BG, fg=self.BUTTON_FG, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button_dot.grid(row=3, column=0, sticky=NSEW)

        self.button0 = Button(self.button_frame, font=self.BUTTON_FONT, text="0", command=partial(self.print_number, "0"))
        self.button0.configure(bg=self.BUTTON_BG, fg=self.BUTTON_FG, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button0.grid(row=3, column=1, sticky=NSEW)

        self.button_equal = Button(self.button_frame, font=self.BUTTON_FONT, text="=", command=self.print_result)
        self.button_equal.configure(bg=self.BUTTON_BG, fg=self.BUTTON_FG, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button_equal.grid(row=3, column=2, sticky=NSEW)

        self.button_divide = Button(self.button_frame, font=self.BUTTON_FONT, text="/", command=partial(self.print_number, "/"))
        self.button_divide.configure(bg=self.BUTTON_BG, fg=self.BUTTON_FG, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        self.button_divide.grid(row=3, column=3, sticky=NSEW)

        self.button_frame.grid_rowconfigure(0, weight=1)
        self.button_frame.grid_rowconfigure(1, weight=1)
        self.button_frame.grid_rowconfigure(2, weight=1)
        self.button_frame.grid_rowconfigure(3, weight=1)

        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)
        self.button_frame.grid_columnconfigure(3, weight=1)


if __name__ == '__main__':
    help_message = """
    Usage:
    python main.py [OPTIONS]

    Options:
    -h | --help : To display this help message
    -t <theme_name> | --theme <theme_name> : To set theme

    Themes:
    Light
    Dark
    Default
    Default-opposite
    """

    theme_names = '''
    Themes:
    Light
    Dark
    Default
    Default-opposite
    '''

    themes_list = ['light', 'dark', 'default', 'default-opposite']
    OUTPUT_BG = 'bisque'
    OUTPUT_FG = 'black'
    BUTTON_BG = 'pink'
    BUTTON_FG = 'black'

    try:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            print(help_message)
            sys.exit(0)
        elif sys.argv[1] == "-t" or sys.argv[1] == "--theme":
            try:
                if sys.argv[2]:
                    if sys.argv[2].lower() in themes_list:
                        if sys.argv[2].lower() == 'light':
                            OUTPUT_BG = 'white'
                            BUTTON_BG = 'grey'
                        elif sys.argv[2].lower() == 'dark':
                            OUTPUT_BG = 'grey'
                            OUTPUT_FG = 'white'
                            BUTTON_BG = 'black'
                            BUTTON_FG = 'white'
                        elif sys.argv[2].lower() == 'default':
                            pass
                        elif sys.argv[2].lower() == 'default-opposite':
                            OUTPUT_BG = 'pink'
                            BUTTON_BG = 'bisque'
                        else:
                            print("Invalid theme name....exiting")
                            exit(0)
                    else:
                        print(theme_names)
                        exit(0)
            except:
                pass
    except:
        pass


    app = Calculator(OUTPUT_BG, OUTPUT_FG, BUTTON_BG, BUTTON_FG)
    app.mainloop()
