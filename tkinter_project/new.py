from tkinter import *


def click():
    entered_text=textentry.get()
    output.delete(0.0, END)
    try:
        definition = my_compdictionary[entered_text]
    except:
        definition = "Error"
    output.insert(END, definition)

def close_window():
    window.destroy()
    exit()

window =Tk()
window.title("My new Form")
window.geometry("500x500")

#My Photo
photo1 = PhotoImage(file="photo.gif")
l=Label (window, image=photo1)
l.place( relwidth=1, relheight=1)
#create lable

Label(window, text="Kirya_Comunication_LTD ", bg="black", fg="white", font="none 12 bold") .grid(row=0, column=1, sticky=W)

#create a text entry box
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)
#add a submit button
Button(window, text="SUBMIT", height=5 , width=30, command=click) .grid(row=3, column=0, sticky=W)


#create a text box
output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

#create dictionary
my_compdictionary = {
    'algorithem': 'ciphers', 'bug': 'bug of code'
}


#create lable

Label(window, text="click to exit :", bg="black", fg="white", font="none 12 bold") .grid(row=6, column=0, sticky=W)

#create a button
#add a submit button
Button(window, text="EXIT", height=5, width=30, command=close_window) .grid(row=7, column=0, sticky=W)










window.mainloop()