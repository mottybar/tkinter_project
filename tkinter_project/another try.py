from tkinter import *

import pyodbc
conn = pyodbc.connect(
 'Driver={SQL Server};'
 'Server=MOTTYBAR20-PC\SQLEXPRESS;'
 'Database=ACDB;'
 'Trusted_Connection=yes;')

def Read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dbo.customers')
    for row in cursor:
        print(f'row = {row}')
    print()

    

def Create_Customer(AddNewClientWin,customeridentry,firstnameentry,lastnameentry,BODentry,joindateentry,cityentry,stateentry,streetentry,monthlydiscountentry,mainphonenumentry,secphonenumentry,faxentry,packidentry):
    inserted = Label(AddNewClientWin,  text="Record inserted successfully", fg="black", bg="green")
    exception = Label(AddNewClientWin, text="Failed to insert the record", fg="black", bg="red",padx=8)
    label1=Label(AddNewClientWin, fg="black", bg="white")
    list_of_rows=list()
    try:
        customeridentryget=customeridentry.get()
        firstnameentryget=firstnameentry.get()
        lastnameentryget=lastnameentry.get()
        BODentryget=BODentry.get()
        joindateentryget=joindateentry.get()
        cityentryget=cityentry.get()
        stateentryget=stateentry.get()
        streetentryget=streetentry.get()
        mainphonenumentryget=mainphonenumentry.get()
        secphonenumentryget=secphonenumentry.get()
        faxentryget=faxentry.get()
        monthlydiscountentryget=monthlydiscountentry.get()
        packidentryget=packidentry.get()
        cursor = conn.cursor()
        cursor.execute("SET IDENTITY_INSERT customers ON")
        cursor.execute("insert into dbo.customers(Customer_id,First_Name,Last_Name,Birth_Date,Join_Date,City,State,Street,main_phone_num,secondary_phone_num,fax,monthly_discount,pack_id) values(?,?,?,?,?,?,?,?,?,?,?,?,?);",
                   (customeridentryget, firstnameentryget, lastnameentryget, BODentryget, joindateentryget,cityentryget,stateentryget,streetentryget,mainphonenumentryget,secphonenumentryget,faxentryget,monthlydiscountentryget,packidentryget))
        conn.commit()
        cursor.execute('SELECT * FROM dbo.customers where customer_id=?;',
                   (customeridentryget))

        for row in cursor:
            list_of_rows.append(str(row))
        label1.config(text=("\n".join(list_of_rows)))
        label1.place(x=0,y=310)
        inserted.place(x=0, y=0)
    except:
        exception.place(x=0,y=0)




def Create_Package(packidentry,speedentry,startdatentry,monthlypaymententry,sectoridentry):
    print("Create")
    packidentryget=packidentry.get()
    speedentryget=speedentry.get()
    startdatentryget=startdatentry.get()
    monthlypaymententryget=monthlypaymententry.get()
    sectoridentryget=sectoridentry.get()
    cursor = conn.cursor()
    cursor.execute("SET IDENTITY_INSERT packages ON")
    cursor.execute("insert into dbo.packages(pack_id,speed,strt_date,monthly_payment,sector_id) values(?,?,?,?,?);",
                (packidentryget,speedentryget,startdatentryget,monthlypaymententryget,sectoridentryget))
    conn.commit()
    Read(conn)






def Aboutwin():

    about=Tk()
    about.geometry('250x300')
    var = StringVar(about)
    msg = Message(about, text="Welcome to Kirya_Comunication_LTD, contact us at +972 545111111 ").place(relx=0.1, rely=0.3, relwidth= 0.7)



def OpenUpdateNewPackageWin():
    UpdateNewPackageWin=Tk()
    UpdateNewPackageWin.title('Kirya_Comunication_LTD')
    UpdateNewPackageWin.geometry('250x300')
    gradeidlabel=Label(UpdateNewPackageWin, text='Grade ID:')
    gradeidlabel.place(relx=0.1, rely=0.1,relwidth=0.32)
    gradenemelabel=Label(UpdateNewPackageWin, text='Grade name:')
    gradenemelabel.place(relx=0.1, rely=0.15,relwidth=0.32)
    maxpricelabel=Label(UpdateNewPackageWin, text='Max price:')
    maxpricelabel.place(relx=0.1, rely=0.20,relwidth=0.32)
    minpricelabel=Label(UpdateNewPackageWin, text='Min price:')
    minpricelabel.place(relx=0.1, rely=0.25,relwidth=0.32)



    gradenidentry= Entry(UpdateNewPackageWin)
    gradenidentry.place(relx=0.45, rely=0.1,relwidth=0.32)
    gradenameentry= Entry(UpdateNewPackageWin)
    gradenameentry.place(relx=0.45, rely=0.15,relwidth=0.32)
    maxpriceentry= Entry(UpdateNewPackageWin)
    maxpriceentry.place(relx=0.45, rely=0.2,relwidth=0.32)
    minpriceentry= Entry(UpdateNewPackageWin)
    minpriceentry.place(relx=0.45, rely=0.25,relwidth=0.32)


    updatepackage = Button(UpdateNewPackageWin, text='create')
    updatepackage.place(relx=0.1, rely=0.85,relwidth=0.32)
    quit=Button(UpdateNewPackageWin, text="quit",command=UpdateNewPackageWin.destroy)
    quit.place(relx=0.45, rely=0.85,relwidth=0.32)

def OpenAddNewPackageWin():
    addNewPackagewin=Tk()
    addNewPackagewin.title('Kirya_Comunication_LTD')
    addNewPackagewin.geometry('400x400')
    packidlabel=Label(addNewPackagewin, text='Pack ID:')
    packidlabel.place(relx=0.1, rely=0.1,relwidth=0.32)
    speedlabel=Label(addNewPackagewin, text='Speed:')
    speedlabel.place(relx=0.1, rely=0.15,relwidth=0.32)
    startdatelabel=Label(addNewPackagewin, text='Start date:')
    startdatelabel.place(relx=0.1, rely=0.20,relwidth=0.32)
    monthlypaymentlabel=Label(addNewPackagewin, text='Monthly payment:')
    monthlypaymentlabel.place(relx=0.1, rely=0.25,relwidth=0.32)
    sectoridlabel=Label(addNewPackagewin, text='Sector ID:')
    sectoridlabel.place(relx=0.1, rely=0.3,relwidth=0.32)


    packidentry= Entry(addNewPackagewin)
    packidentry.place(relx=0.45, rely=0.1,relwidth=0.32)
    speedentry= Entry(addNewPackagewin)
    speedentry.place(relx=0.45, rely=0.15,relwidth=0.32)
    startdatentry= Entry(addNewPackagewin)
    startdatentry.place(relx=0.45, rely=0.2,relwidth=0.32)
    monthlypaymententry= Entry(addNewPackagewin)
    monthlypaymententry.place(relx=0.45, rely=0.25,relwidth=0.32)
    sectoridentry= Entry(addNewPackagewin)
    sectoridentry.place(relx=0.45, rely=0.3,relwidth=0.32)

    createpackage = Button(addNewPackagewin, text='create',command=lambda: Create_Package(packidentry,speedentry,startdatentry,monthlypaymententry,sectoridentry))
    createpackage.place(relx=0.1, rely=0.85,relwidth=0.32)
    Quit=Button(addNewPackagewin, text="Quit",command=addNewPackagewin.destroy)
    Quit.place(relx=0.45, rely=0.85,relwidth=0.32)


def OpenAddNewClientWin():
    AddNewClientWin = Tk()
    AddNewClientWin.title('Kirya_Comunication_LTD')
    AddNewClientWin.geometry('400x400')



    customeridlabel = Label(AddNewClientWin, text= 'Customer ID:')
    customeridlabel.place(relx=0.1, rely=0.1,relwidth=0.32)
    firstnamelabel = Label(AddNewClientWin, text="FirstName:")
    firstnamelabel.place(relx=0.1, rely=0.15,relwidth=0.32)
    lastnamelabel = Label(AddNewClientWin, text="Lastname:")
    lastnamelabel.place(relx=0.1, rely=0.2,relwidth=0.32)
    DOBlabel = Label(AddNewClientWin, text="Date of birth:")
    DOBlabel.place(relx=0.1, rely=0.25,relwidth=0.32)
    joindatelabel = Label(AddNewClientWin, text="Join date:")
    joindatelabel.place(relx=0.1, rely=0.3,relwidth=0.32)
    cityabel = Label(AddNewClientWin, text="City")
    cityabel.place(relx=0.1, rely=0.35,relwidth=0.32)
    statelabel = Label(AddNewClientWin, text="State:")
    statelabel.place(relx=0.1, rely=0.4,relwidth=0.32)
    streetlabel = Label(AddNewClientWin, text="Street:")
    streetlabel.place(relx=0.1, rely=0.45,relwidth=0.32)
    mainphonelabel = Label(AddNewClientWin, text="Main phone:")
    mainphonelabel.place(relx=0.1, rely=0.5,relwidth=0.32)
    secondphonelabel = Label(AddNewClientWin, text="Other phone:")
    secondphonelabel.place(relx=0.1, rely=0.55,relwidth=0.32)
    faxlabel = Label(AddNewClientWin, text="Fax:")
    faxlabel.place(relx=0.1, rely=0.6,relwidth=0.32)
    monthlydiscount = Label(AddNewClientWin, text="Monthly discount:")
    monthlydiscount.place(relx=0.1, rely=0.65,relwidth=0.32)
    packidlabel = Label(AddNewClientWin, text="Pack ID")
    packidlabel.place(relx=0.1, rely=0.7,relwidth=0.32)


    customeridentry=Entry(AddNewClientWin)
    customeridentry.place(relx=0.45, rely=0.1,relwidth=0.32)
    firstnameentry = Entry(AddNewClientWin)
    firstnameentry.place(relx=0.45, rely=0.15,relwidth=0.32)
    lastnameentry = Entry(AddNewClientWin)
    lastnameentry.place(relx=0.45, rely=0.2,relwidth=0.32)
    BODentry=Entry(AddNewClientWin)
    BODentry.place(relx=0.45, rely=0.25,relwidth=0.32)
    joindateentry = Entry(AddNewClientWin)
    joindateentry.place(relx=0.45, rely=0.3,relwidth=0.32)
    cityentry = Entry(AddNewClientWin)
    cityentry.place(relx=0.45, rely=0.35,relwidth=0.32)
    stateentry = Entry(AddNewClientWin)
    stateentry.place(relx=0.45, rely=0.4,relwidth=0.32)
    streetentry = Entry(AddNewClientWin)
    streetentry.place(relx=0.45, rely=0.45,relwidth=0.32)
    mainphonenumentry = Entry(AddNewClientWin)
    mainphonenumentry.place(relx=0.45, rely=0.5,relwidth=0.32)
    secphonenumentry = Entry(AddNewClientWin)
    secphonenumentry.place(relx=0.45, rely=0.55, relwidth=0.32)
    faxentry = Entry(AddNewClientWin)
    faxentry.place(relx=0.45, rely=0.6,relwidth=0.32)
    monthlydiscountentry = Entry(AddNewClientWin)
    monthlydiscountentry.place(relx=0.45, rely=0.65,relwidth=0.32)
    packidentry = Entry(AddNewClientWin)
    packidentry.place(relx=0.45, rely=0.7,relwidth=0.32)
    createcustomer = Button(AddNewClientWin, text='create',command=lambda : Create_Customer(AddNewClientWin,customeridentry,firstnameentry,lastnameentry,BODentry,joindateentry,cityentry,stateentry,streetentry,monthlydiscountentry,mainphonenumentry,secphonenumentry,faxentry,packidentry))
    createcustomer.place(relx=0.1, rely=0.85,relwidth=0.32)
    quit= Button(AddNewClientWin, text="quit",command=AddNewClientWin.destroy)
    quit.place(relx=0.45, rely=0.85,relwidth=0.32)

def OpenSearchwin():
    searchwin = Tk()
    searchwin.geometry('400x400')
    searchwin.title('Kirya_Comunication_LTD system')
    seatchentry =Entry(searchwin)
    seatchentry.place(relx=0.05,rely=0.1, relwidth=0.3)
    var = StringVar(searchwin)
    searchbutton = Button(searchwin, text="search")
    searchbutton.place(relx=0.37, rely=0.17,relwidth=0.3)

    listofquery = ["Costumers", "Packages", 'Grades', 'Sector' ]
    var.set("Select Query")
    droplist = OptionMenu(searchwin, var, *listofquery)
    droplist.config(width=10)
    droplist.place(relx=0.37, rely=0.08,relwidth=0.3)

    var2 = StringVar(searchwin)
    listofsubquery = ["subQuery1", "subQuery2", 'subQuery3', 'subQuery4', "subQuery5", 'subQuery6', 'subQuery7']
    var2.set("Select SubQuery")

    droplist = OptionMenu(searchwin, var2, *listofsubquery)
    droplist.config(width=10)
    droplist.place(relx=0.68, rely=0.08,relwidth=0.3)


    menubar = Menu(searchwin)
    file = Menu(menubar, tearoff=0)
    file.add_command(label="Add new client", command=OpenAddNewClientWin)
    file.add_command(label="Add new package", command=OpenAddNewPackageWin)
    file.add_command(label="Erase client")
    file.add_command(label='Update package', command=OpenUpdateNewPackageWin)
    file.add_command(label="Save")
    file.add_command(label="Save as...")
    file.add_separator()

    file.add_command(label="Exit", command=searchwin.destroy)

    menubar.add_cascade(label="File", menu=file)

    help = Menu(menubar, tearoff=0)
    help.add_command(label="About", command=Aboutwin)
    menubar.add_cascade(label="Help", menu=help)

    searchwin.config(menu=menubar)


    answer = Text(searchwin, width=80, height=13)
    answer.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.5)
    root.destroy()



root = Tk()
root.geometry('550x500')
root.title('Welcome to Kirya_Comunication_LTD system')
root.configure(bg='white')
Label(root, text="Welcome to Kirya_Comunication_LTD ", fg="green", font="none 20 bold") .place(x=10, y=0)

#photo = PhotoImage(file='1234.gif')
#label = Label(root, image=photo, bg='white')
#label.image = photo
#label.pack()
enter = Button(root, text='login', relief=RAISED, command=OpenSearchwin).place(relx=0.33, rely=0.7, relwidth=0.33)

root.mainloop()

