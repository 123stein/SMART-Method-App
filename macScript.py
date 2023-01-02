from tkinter import *
import tkmacosx as osx

window = Tk()
window.title("SMART Method App")

specificLabel = Label(window, text="Specific")
specificLabel.grid(row=0, column=0)  # S
measurableLabel = Label(window, text="Measurable")
measurableLabel.grid(row=1, column=0)  # M
attractiveLabel = Label(window, text="Attractive")
attractiveLabel.grid(row=2, column=0)  # A
RealisticLabel = Label(window, text="Realistic")
RealisticLabel.grid(row=3, column=0)  # R
timeboundLabel = Label(window, text="Time")
timeboundLabel.grid(row=4, column=0)  # T

specificEntry = Entry(window)
specificEntry.grid(row=0, column=1)  # S
measurableEntry = Entry(window)
measurableEntry.grid(row=1, column=1)  # M
atq = IntVar()
attractiveEntry = Checkbutton(window, variable=atq)
attractiveEntry.grid(row=2, column=1)  # A
rlq = IntVar()
RealisticEntry = Checkbutton(window, variable=rlq)
RealisticEntry.grid(row=3, column=1)  # R
timeboundEntry = Entry(window)
timeboundEntry.grid(row=4, column=1)  # T

specificHelp = Button(window, text="?", command=lambda: tkinter.messagebox.showinfo("Help",
                                                                                    'What is your specific goal?\ne.g. go to gym instead of "do sport"'))
specificHelp.grid(row=0, column=2)  # S
measurableHelp = Button(window, text="?", command=lambda: tkinter.messagebox.showinfo("Help",
                                                                                      'How can you measure your goal?\ne.g. 2x/week instead of "more"'))
measurableHelp.grid(row=1, column=2)  # M
attractiveHelp = Button(window, text="?", command=lambda: tkinter.messagebox.showinfo("Help",
                                                                                      'Is it somethong that you want to achieve?\ne.g. I will feel better if I achieve [...] because [...]'))
attractiveHelp.grid(row=2, column=2)  # A
timeboundHelp = Button(window, text="?", command=lambda: tkinter.messagebox.showinfo("Help",
                                                                                     "until when will your goal be active (don't say for ever, at least not yet)\ne.g. febuary -> you will do your goal until febuary"))
timeboundHelp.grid(row=4, column=2)  # T
RealisticHelp = Button(window, text="?", command=lambda: tkinter.messagebox.showinfo("Help",
                                                                                     'Is it possible for you? What do you do so it is possible?\ne.g. Do I have time for that hour in the gym, do I have to get up earlier?'))
RealisticHelp.grid(row=3, column=2)  # R


def giveGoal():
    if (atq.get(), rlq.get()) == (1, 1):
        tkinter.messagebox.showinfo(title="Now get to achieve your goals!", message=f"Your goal is to {specificEntry.get()} {measurableEntry.get()} until {timeboundEntry.get()}")
    elif (atq.get(), rlq.get()) == (0, 1):
        tkinter.messagebox.showinfo(title="Think about it...", message="You must want to achieve your goal!")
    elif (atq.get(), rlq.get()) == (1, 0):
        tkinter.messagebox.showinfo(title="Im sure it was a great goal!", message="It is fine if this is something that you cannot do, if possible try to but otherwise choose something else!")
    elif (atq.get(), rlq.get()) == (0, 0):
        tkinter.messagebox.showinfo(title="Come on... what was the goal?", message="You should rethink your goal if you cannnot and do not want to achieve that goal!")


submitButton = osx.Button(window, text="Give me my goal!", background="#007AFF", activebackground="#FFFFFF",
                          activeforeground="#000000", bd=0, focusthickness=0, command=giveGoal)
submitButton.grid(row=5, column=1, padx=50, pady=30)

window.mainloop()
