from gtts import gTTS
from tkinter import *
import playsound

txt = ""
txt2 = ""

language_list = ["English", "Hindi", "Marathi", "Japanese"]
language_list = ["en", "hi", "mr", "ja"]


def clicked():
	myobj = gTTS(text=txt.get(), lang=variable1.get(), slow=False)
	myobj.save("converted.mp3")
	playsound.playsound("converted.mp3",True)

window = Tk()
window.title("Text To Speech Project by SAURABH")
window.geometry('600x400')

variable1 = StringVar(window)
variable1.set("select-lang")


lbl2 = Label(window, text="	Text to speech", font=('lato black',17,'bold'),fg="blue")
lbl2.grid(column=0, row=0)
lbl2 = Label(window, text="	using python", font=('lato black',17,'bold'),fg="blue")
lbl2.grid(column=0, row=1)

lbl2 = Label(window, text="", font=('lato black', 20,'bold'),fg="red")
lbl2.grid(column=0, row=2)

lbl2 = Label(window, text="Enter Text", font=('lato black', 20,'bold'),fg="red")
lbl2.grid(column=0, row=3)


txt = Entry(window, textvariable=txt, font=('lato black', 12, 'normal'))
txt.grid(column=1, row=3)

lbl2 = Label(window, text="Select Language", font=('lato black', 20,'bold'))
lbl2.grid(column=0, row=4)

txt2 = OptionMenu(window, variable1,  language_list)
txt2.grid(column=1, row=4)

lbl2 = Label(window, text="", font=('lato black', 18,'bold'),fg="red")
lbl2.grid(column=0, row=5)



btn = Button(window, font=('lato', 13, 'bold'), text="Play Sound",padx=2,pady=2,bg="red",fg="white",command=lambda:clicked())
btn.grid(column=0, row=6)

window.mainloop()
