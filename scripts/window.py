from tkinter import *

class Window():

    bot = False

    def __init__(self):
        frame = Tk()
        frame.title("IG BOT")
        frame.geometry('360x420')

        self.create_temp(frame)
        self.start_frame(frame)

    def create_temp(self, frame):
        title = Label(frame, text="Instagram bot v.1.0")
        title.grid(column=0, row=0)

        author = Label(frame, text="by 5a 65 76 63 6f 72 65")
        author.grid(column=0, row=1)

        btn = Button(frame, text="Start bot", command=self.enable_bot)
        btn.grid(column=0, row=2)

    def start_frame(self, frame):
        frame.mainloop()

    def enable_bot(self):
        if(self.bot == True):
            self.bot = False
        else:
            self.bot = True

    def getBot(self):
        return self.bot